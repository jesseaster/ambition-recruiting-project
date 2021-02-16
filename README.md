
## Ambition Recruiting Project #1

This project is for people interested in pursuing a software engineer opportunity at [Ambition](https://ambition.com). 
It serves as the starting point of our recruiting process and is designed to test/verify a candidate's 
general familiarity with Python, Django, and testing to ensure the subsequent steps are productive for both parties. 

**Recruiting Process**

Thank you in advance for taking the time to work through this project and our process. 
Our goal throughout is to foster meaningful, real-world conversations as to how you think and work. 
While we know it's unrealistic to know exactly what "we're getting" (and you're getting!) throughout this process... 
it's at the very least more insightful than whiteboard problems.

1. Complete this ~1 hour project below and submit your code as a link within the [application form](https://forms.gle/eG6qWWwbYjTqx5HD6).
2. We'll reach out to schedule a 30 minute conversation. This is an opportunity for you to *ask us* questions! 
You'll find that we're a very transparent company and believe fit is a two-way street. 
3. Complete our second (and final) [project](https://gist.github.com/travistruett/77f6e29649e018c13322d37cce3babf8).
4. We'll reach out to schedule a 1.5 hour code review. We've found this is the best way to actually simulate us working together...
we can see how you think/build and you can see how we conduct code reviews (something we take quite seriously). 
5. At this point we'll switch gears to focus on culture and onboarding. This generally consists of several calls 
with a variety of people to ensure a) you feel comfortable joining the team and b) you'll be successful here. 

*If we've determined during the process that you're not the right candidate for a given role we'll notify you as to why.
This is a commitment to anybody that completes Step #1.*

### Brief

This project is a Django application that acts as an encounter builder for a Star Wars tabletop RPG.
It uses starship data from the [Star Wars API](https://swapi.dev/) to allow a game master to build custom
or random space encounters for players.

### Objective

The objective of this project is to get all tests in the project to pass.
__The tests should not be modified__. They should be assumed to be accurate tests of the behavior of the
application. Instead, there are bugs in the project's codebase that are causing the tests to fail. It is
your job to fix the bugs in order to get all tests to pass. 


### Get Started

```
cd path/to/ambition-recruiting-project
virtualenv -p `which python3` venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py test recruiting_project
```
