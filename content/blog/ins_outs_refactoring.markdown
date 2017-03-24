Title: The ins and outs of refactoring 
Date: 2017-01-25
Category: blog
Tags: 8th light, apprenticeship, refactoring
Author: Hana Lee
Summary: Advantages of refactoring to more modular code 

The end goal of refactoring is to revise our software to be more reusable, more maintainable,
and better designed. Frequently, that task involves breaking down
large components of code into smaller pieces. For example, one of the most
common refactoring patterns is [Extract
Method](https://refactoring.com/catalog/extractMethod.html), which creates a new
method from duplicated functionality. Decomposing our code in this fashion introduces
indirection into the system and supports a modular design. 

The immediate benefits may not be obvious: we are introducing more parts to
maintain, and a reader of our code may be forced to "jump around" to
look up what's being referenced. But each part will be smaller and more
self-contained, which actually makes it simpler to navigate in the long run.

## The advantages of modularity

Modularity encourages robustness—that is, stability and adaptability to perturbations—in 
all sorts of complex systems, not only software. For example,
it is frequently seen in biological networks, where metabolic pathways remain
isolated from one another so that loss of functionality in one does not affect
the functioning of the rest. A bacterium that carries a mutation disabling its
ability to utilize lactose is still able to feed on and digest other sugars,
ensuring its survival.

Modularity also makes it easier to introduce novel behavior into the system
by creating variations in the interactions between existing components, instead of
building a new component from scratch. This type of organization gives an
evolutionary advantage in biology: organisms activate and
control sets of functionally related genes, which can be flexibly combined in
various ways to develop more complex features.

In software, a modular system means that a bug in one portion of the code will
have limited effects that remain isolated instead of bringing the whole
application to a halt. It also means that your code will be easier to test—and
if you follow a test-driven development (TDD) process, your code will naturally
tend to assume a modular organization, with isolatable parts. Adding new
features does not require as much new code to be written
since you can easily reuse existing code as building blocks. 

## Identifying problems 

So how do we go about refactoring our code to become more modular? There are
certain code smells, which point out areas that can be decomposed into
smaller components. [Long
Method](https://sourcemaking.com/refactoring/smells/long-method) and [Large
Class](https://sourcemaking.com/refactoring/smells/large-class) are some obvious
ones, as well as [Duplicate
Code](https://sourcemaking.com/refactoring/smells/duplicate-code). 

Another set
of clues to look for are violations of SOLID principles, particularly the Single
Responsiblity Principle (SRP) and Dependency Inversion Principle (DIP). A modular system
should consist of components that can be mixed and matched in various
combinations: thus, each component should have a clearly defined and singular
function (SRP). Moreover, its dependencies should be organized so that it can
remain as decoupled from other modules as possible (DIP).

To demonstrate, I'm going to take a look at some messy, gnarly code that I wrote
for a pair project during my apprenticeship: [a controller class for a Rails
application](https://github.com/hnlee/reviewr/blob/master/app/controllers/projects_controller.rb).

This class immediately stands out as a violation of SRP, since a lot of the
logic in its methods do not directly relate to the main responsibility of the
controller, which is to determine what views to render in response to HTTP
requests. For example, take a look at the `create` method:

```ruby

  def create
    project = Project.new(title: project_params[:title],
                          link: project_params[:link],
                          description: project_params[:description])
    emails = params[:emails]
    if project.save
      ProjectOwner.create(project_id: project.id,
                          user_id: current_user.id)
      emails.each do |email|
        user = User.find_or_create_by(email: email)
        ProjectInvite.create(project_id: project.id,
                             user_id: user.id)
        InviteMailer.invite_email(project, user).deliver_now
      end
      redirect_to user_path(current_user.id), { flash: { notice: "Project has been created" } } 
    else
      redirect_to new_project_path(user: project_params[:user_id]), { flash: { error: project.get_error_message } }
    end
  end

```

There is a lot of code in there that relates to creating a new project model and
sending out invite emails, which should be separate from the task of
rendering views.

Moreover, the code that manages sending out invite emails is almost fully
duplicated in another method, a clear code smell:

```ruby

  def update
    @project = Project.find_by_id(params[:id])
    @invited_reviewers = @project.get_invited_reviewers
    emails = params[:emails]
    if @project.update_attributes(project_params)
      if emails
        emails.each do |email|
          if !@invited_reviewers.find_by(email: email)
            user = User.find_or_create_by(email: email)
            ProjectInvite.create(project_id: @project.id,
                                 user_id: user.id)
            InviteMailer.invite_email(@project, user).deliver_now
          end
        end
      end
  ...
  end

```

Looking for indicators of bad design and thinking about where the natural
boundaries lie in your software help identify places where refactoring is
needed.

## Refactoring safely

At this stage, it may seem tempting to dive right in and start cutting and
pasting, but there's a process to refactoring that ensures you don't change the
behavior of the application while making your changes. (That's in the very
definition of refactoring, after all!) Martin Fowler, when
describing the Extract Method refactoring pattern, outlines the following steps:

1. Create a new method and name it for what the extracted method does.
2. Copy (not cut or move) the extracted code to the new method.
3. Look for variables that are local in scope to the old method.
4. If they are only used in the extracted code, then declare them as temporary
   variables in the new method.
5. If they are used in other parts of the old method, then pass them in as
   parameters to the new method.
6. Replace the extracted code in the old method with a call to the new method.

Of course, implicit to these steps is the assumption that you will run your test
suite after every step to make sure that the behavior of the application has not
changed.

This algorithm for refactoring reminds me of a phenomenon in evolution: a gene
undergoes duplication, interactions with the original gene switch over to the
new copy, and then the first gene gradually becomes nonfunctional, at which
point it is called a pseudogene. The main difference from refactoring is that
the evolutionary process takes many, many generations—a lot slower than simply
manipulating text in an editor!

Applying these steps to my example above, first I create a new method and
copy over the code I want to extract:

```ruby

def email_invited_reviewers
  emails.each do |email|
    user = User.find_or_create_by(email: email)
    ProjectInvite.create(project_id: project.id,
                         user_id: user.id)
    InviteMailer.invite_email(project, user).deliver_now
  end
end

```

Next, I look at the variables. Most of the variables aren't used
outside the `emails.each` block, but `emails` itself is defined in the original
method from `params`. So it should probably be passed in as a parameter to the
new method.

```ruby

def email_invited_reviewers(emails)
  emails.each do |email|
    user = User.find_or_create_by(email: email)
    ProjectInvite.create(project_id: project.id,
                         user_id: user.id)
    InviteMailer.invite_email(project, user).deliver_now
  end
end

```

Now I can return to the `create` method and replace that code with a call to
`email_invited_reviewers`:

```ruby

  def create
    project = Project.new(title: project_params[:title],
                          link: project_params[:link],
                          description: project_params[:description])
    emails = params[:emails]
    if project.save
      ProjectOwner.create(project_id: project.id,
                          user_id: current_user.id)
      email_invited_reviewers(emails)
      redirect_to user_path(current_user.id), { flash: { notice: "Project has been created" } } 
    else
      redirect_to new_project_path(user: project_params[:user_id]), { flash: { error: project.get_error_message } }
    end
  end

```

I can even go to the `update` method and replace it with a similar call. The
only wrinkle is that there is an extra conditional in the `update` method to
check whether the person has already been sent an email invite. One way to
handle that is by extracting another method to filter `emails` before passing it to
`email_invited_reviewers`.

```ruby

def filter_new_reviewers(emails, invited_reviewers)
  emails.select{|email| !invited_reviewers.find_by(email: email)}
end

```

Then we can replace the code in `update` with calls to both methods:

```ruby

  def update
    @project = Project.find_by_id(params[:id])
    @invited_reviewers = @project.get_invited_reviewers
    emails = params[:emails]
    if @project.update_attributes(project_params)
      if emails
        filtered_emails = filter_new_reviewers(emails, @invited_reviewers) 
        email_invited_reviewers(filtered_emails)
     end
  ...
  end

```

There's a lot more refactoring that could be done to improve the modularity of
this code. For example, the `email_invited_reviewers` and `filter_new_reviewers`
methods probably belong in new classes, one to handle email actions and another
to handle looking up data from models. Both the `create` and `update` controller
methods I've shown above could also use a few more method extractions, so that the
responsibilities for making new models or updating existing ones does not lie
with the controller. And that's not even getting into the rest of the methods
in this class...

That's one of the reasons that refactoring should be a continual process
throughout development. Ideally, we ought to refactor during every TDD cycle
("Red, Green, Refactor"), but if that doesn't happen, we should do it when we first notice a
problem, instead of leaving it for some future time that inevitably never comes. That's 
a lesson I learned quite personally during my apprenticeship!

## Takeaways

* Refactoring often involves breaking down large chunks of code into smaller
  pieces. That improves design because it promotes modularity.
* Modular systems are more robust and adaptable to change in general, not
  just in software.
* Identify areas for refactoring through code smells and violations of SOLID
  principles.
* The process of refactoring requires that the application behavior remains
  unchanged. Take it step by step, and don't forget to run your test suite
  often.
