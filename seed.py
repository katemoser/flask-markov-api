"""Seed database for Markov"""

from app import db
from models import User, Seed, Like, Poem, Sign

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

# ###################### POEM SEED #################
# seed = Seed(
#     title="The Love Song of J. Alfred Prufrock",
#     text="""Let us go then, you and I,
# When the evening is spread out against the sky
# Like a patient etherized upon a table;
# Let us go, through certain half-deserted streets,
# The muttering retreats
# Of restless nights in one-night cheap hotels
# And sawdust restaurants with oyster-shells:
# Streets that follow like a tedious argument
# Of insidious intent
# To lead you to an overwhelming question ...
# Oh, do not ask, “What is it?”
# Let us go and make our visit.

# In the room the women come and go
# Talking of Michelangelo.

# The yellow fog that rubs its back upon the window-panes,
# The yellow smoke that rubs its muzzle on the window-panes,
# Licked its tongue into the corners of the evening,
# Lingered upon the pools that stand in drains,
# Let fall upon its back the soot that falls from chimneys,
# Slipped by the terrace, made a sudden leap,
# And seeing that it was a soft October night,
# Curled once about the house, and fell asleep.

# And indeed there will be time
# For the yellow smoke that slides along the street,
# Rubbing its back upon the window-panes;
# There will be time, there will be time
# To prepare a face to meet the faces that you meet;
# There will be time to murder and create,
# And time for all the works and days of hands
# That lift and drop a question on your plate;
# Time for you and time for me,
# And time yet for a hundred indecisions,
# And for a hundred visions and revisions,
# Before the taking of a toast and tea.

# In the room the women come and go
# Talking of Michelangelo.

# And indeed there will be time
# To wonder, “Do I dare?” and, “Do I dare?”
# Time to turn back and descend the stair,
# With a bald spot in the middle of my hair —
# (They will say: “How his hair is growing thin!”)
# My morning coat, my collar mounting firmly to the chin,
# My necktie rich and modest, but asserted by a simple pin —
# (They will say: “But how his arms and legs are thin!”)
# Do I dare
# Disturb the universe?
# In a minute there is time
# For decisions and revisions which a minute will reverse.

# For I have known them all already, known them all:
# Have known the evenings, mornings, afternoons,
# I have measured out my life with coffee spoons;
# I know the voices dying with a dying fall
# Beneath the music from a farther room.
#                So how should I presume?

# And I have known the eyes already, known them all—
# The eyes that fix you in a formulated phrase,
# And when I am formulated, sprawling on a pin,
# When I am pinned and wriggling on the wall,
# Then how should I begin
# To spit out all the butt-ends of my days and ways?
#                And how should I presume?

# And I have known the arms already, known them all—
# Arms that are braceleted and white and bare
# (But in the lamplight, downed with light brown hair!)
# Is it perfume from a dress
# That makes me so digress?
# Arms that lie along a table, or wrap about a shawl.
#                And should I then presume?
#                And how should I begin?

# Shall I say, I have gone at dusk through narrow streets
# And watched the smoke that rises from the pipes
# Of lonely men in shirt-sleeves, leaning out of windows? ...

# I should have been a pair of ragged claws
# Scuttling across the floors of silent seas.

# And the afternoon, the evening, sleeps so peacefully!
# Smoothed by long fingers,
# Asleep ... tired ... or it malingers,
# Stretched on the floor, here beside you and me.
# Should I, after tea and cakes and ices,
# Have the strength to force the moment to its crisis?
# But though I have wept and fasted, wept and prayed,
# Though I have seen my head (grown slightly bald) brought in upon a platter,
# I am no prophet — and here’s no great matter;
# I have seen the moment of my greatness flicker,
# And I have seen the eternal Footman hold my coat, and snicker,
# And in short, I was afraid.

# And would it have been worth it, after all,
# After the cups, the marmalade, the tea,
# Among the porcelain, among some talk of you and me,
# Would it have been worth while,
# To have bitten off the matter with a smile,
# To have squeezed the universe into a ball
# To roll it towards some overwhelming question,
# To say: “I am Lazarus, come from the dead,
# Come back to tell you all, I shall tell you all”—
# If one, settling a pillow by her head
#                Should say: “That is not what I meant at all;
#                That is not it, at all.”

# And would it have been worth it, after all,
# Would it have been worth while,
# After the sunsets and the dooryards and the sprinkled streets,
# After the novels, after the teacups, after the skirts that trail along the floor—
# And this, and so much more?—
# It is impossible to say just what I mean!
# But as if a magic lantern threw the nerves in patterns on a screen:
# Would it have been worth while
# If one, settling a pillow or throwing off a shawl,
# And turning toward the window, should say:
#                “That is not it at all,
#                That is not what I meant, at all.”

# No! I am not Prince Hamlet, nor was meant to be;
# Am an attendant lord, one that will do
# To swell a progress, start a scene or two,
# Advise the prince; no doubt, an easy tool,
# Deferential, glad to be of use,
# Politic, cautious, and meticulous;
# Full of high sentence, but a bit obtuse;
# At times, indeed, almost ridiculous—
# Almost, at times, the Fool.

# I grow old ... I grow old ...
# I shall wear the bottoms of my trousers rolled.

# Shall I part my hair behind?   Do I dare to eat a peach?
# I shall wear white flannel trousers, and walk upon the beach.
# I have heard the mermaids singing, each to each.

# I do not think that they will sing to me.

# I have seen them riding seaward on the waves
# Combing the white hair of the waves blown back
# When the wind blows the water white and black.
# We have lingered in the chambers of the sea
# By sea-girls wreathed with seaweed red and brown
# Till human voices wake us, and we drown.
# """,
#     author="T.S. Eliot",
#     submitted_by_user_id=user_id,
# )


# db.session.add(seed)
# db.session.commit()

seed1 = Seed(
    title="Sonnet 18",
    text="""Shall I compare thee to a summer’s day?
Thou art more lovely and more temperate.
Rough winds do shake the darling buds of May,
And summer’s lease hath all too short a date.
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimmed;
And every fair from fair sometime declines,
By chance or nature’s changing course untrimmed.
But thy eternal summer shall not fade
Nor lose possession of that fair thou ow’st,
Nor shall Death brag thou wand’rest in his shade,
When in eternal lines to time thou grow’st.
So long as men can breathe or eyes can see,
So long lives this, and this gives life to thee.
""",
    author="Shakespeare",
    submitted_by_user_id=user_id)

seed2 = Seed(
    title="Sonnet 27",
    text="""Weary with toil, I haste me to my bed,
The dear repose for limbs with travel tired,
But then begins a journey in my head
To work my mind when body’s work’s expired.
For then my thoughts, from far where I abide,
Intend a zealous pilgrimage to thee,
And keep my drooping eyelids open wide,
Looking on darkness which the blind do see;
Save that my soul’s imaginary sight
Presents thy shadow to my sightless view,
Which like a jewel hung in ghastly night
Makes black night beauteous and her old face new.
Lo, thus, by day my limbs, by night my mind,
For thee and for myself no quiet find.
""",
    author="Shakespeare",
    submitted_by_user_id=user_id)

seed3 = Seed(
    title="Sonnet 130",
    text="""My mistress’ eyes are nothing like the sun;
Coral is far more red than her lips’ red;
If snow be white, why then her breasts are dun;
If hairs be wires, black wires grow on her head.
I have seen roses damasked, red and white,
But no such roses see I in her cheeks;
And in some perfumes is there more delight
Than in the breath that from my mistress reeks.
I love to hear her speak, yet well I know
That music hath a far more pleasing sound.
I grant I never saw a goddess go;
My mistress, when she walks, treads on the ground.
And yet, by heaven, I think my love as rare
As any she belied with false compare.
""",
    author="Shakespeare",
    submitted_by_user_id=user_id)

seed4 = Seed(
    title="O Captain! My Captain!",
    text="""O Captain! my Captain! our fearful trip is done,
The ship has weather’d every rack, the prize we sought is won,
The port is near, the bells I hear, the people all exulting,
While follow eyes the steady keel, the vessel grim and daring;
But O heart! heart! heart!
O the bleeding drops of red,
Where on the deck my Captain lies,
Fallen cold and dead.

O Captain! my Captain! rise up and hear the bells;
Rise up—for you the flag is flung—for you the bugle trills,
For you bouquets and ribbon’d wreaths—for you the shores a-crowding,
For you they call, the swaying mass, their eager faces turning;
Here Captain! dear father!
This arm beneath your head!
It is some dream that on the deck,
You’ve fallen cold and dead.

My Captain does not answer, his lips are pale and still,
My father does not feel my arm, he has no pulse nor will,
The ship is anchor’d safe and sound, its voyage closed and done,
From fearful trip the victor ship comes in with object won;

Exult O shores, and ring O bells!
But I with mournful tread,
Walk the deck my Captain lies,
Fallen cold and dead.
""",
    author="Walt Whitman",
    submitted_by_user_id=user_id)

db.session.add(seed1)
db.session.add(seed2)
db.session.add(seed3)
db.session.add(seed4)
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


######################### HOROSCOPE SEED ###########

# add signs

astro_signs = [
    "aries",
    "taurus",
    "gemini",
    "cancer",
    "leo",
    "virgo",
    "libra",
    "scorpio",
    "sagittarius",
    "capricorn",
    "aquarius",
    "pisces"
]

for s in astro_signs:
    sign = Sign(
        name=s
    )

    db.session.add(sign)
    db.session.commit()
