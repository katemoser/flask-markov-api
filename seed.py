"""Seed database for Markov"""

from app import db
from models import User, Seed, Like, Poem

db.drop_all()
db.create_all()

admin = User(
    username="kate",
    first_name="Kate",
    last_name="Moser"
)


db.session.add(admin)
db.session.commit()

new_user = User.query.all()[0]
user_id = new_user.id

seed = Seed(
    title="seed title",
    text="""One of my wishes is that those dark trees, 
So old and firm they scarcely show the breeze, 
Were not, as 'twere, the merest mask of gloom, 
But stretched away unto the edge of doom. 

I should not be withheld but that some day 
Into their vastness I should steal away, 
Fearless of ever finding open land, 
Or highway where the slow wheel pours the sand. 

I do not see why I should e'er turn back, 
Or those should not set forth upon my track 
To overtake me, who should miss me hdre 
And long to know if still I held them dg&r. 

They would not find me changed from him they 

knew 
Only more sure of all I thought was true. @ 

I dwell in a lonely house I know 

That vanished many a summer ago, 
And left no trace but the cellar walls, 
And a cellar in which the daylight falls, 

And the purple-stemmed wild raspberries grow. 

O'er ruined fences the grape-vines shield 
The woods come back to the mowing field; 
The orchard tree has grown one copse 
Of new wood and old where the woodpecker chops; 
The footpath down to the well is healed. 

I dwell with a strangely aching heart 

In that vanished abode there far apart 
On that disused and forgotten road 
That has no dust-bath now for the toad. 

Night comes; the black bats tumble and dart; 

The whippoorwill is coming to shout 
And hush and cluck and flutter about: 

I hear him begin far enough away 

Full many a time to say his say 
Before he arrives to say it out. @ 

I'm going out to clean the pasture spring; 
I'll only stop to rake the leaves away 
(And wait to watch the water clear, I may): 
I shan't be gone long. You come too. 

I'm going out to fetch the little calf 
That's standing by the mother. It's so young. 
It totters when she licks it with her tongue. 
I shan't be gone long. You come too. @

Oh, give us pleasure in the flowers to-day; 
And give us not to think so far away 
As the uncertain harvest; keep us here 
All simply in the springing of the year. 

Oh, give us pleasure in the orchard white, 
Like nothing else by day, like ghosts by night; 
And make us happy in the happy bees, 
The swarm dilating round the perfect trees. 

And make us happy in the darting bird 
That suddenly above the bees is heard, 
The meteor that thrusts in with needle bill, 
And off a blossom in mid air stands still. 

For this is love and nothing else is love, 
The which it is reserved for God above 
To sanctify to what far ends He will, 
But which it only needs that we fulfill.""",
    author="anonymous",
    submitted_by_user_id=user_id,
)


db.session.add(seed)
db.session.commit()

new_seed = Seed.query.all()[0]
seed_id = new_seed.id

poem = Poem(
    seed_id=seed_id,
    text="This is the poem text.",
    submitted_by_user_id=user_id
)

db.session.add(poem)
db.session.commit()

new_poem = Poem.query.all()[0]
poem_id = new_poem.id

print("**************************** poem_id:", poem_id)

like = Like(
    user_id=user_id,
    poem_id=poem_id,
)

db.session.add(like)
db.session.commit()
