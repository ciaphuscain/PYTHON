#THIS IS A PROGRAM WHICH WILL CREATE "NEW" STORIES BY FILLING IN BLOVKS WITH RANDOM ADJECTIVES
import random

'''storyblank=A Chaotic Zoo Day
One morning, Gerald, a ___ zookeeper, arrived at the ___ Metropolis Zoo in his ___, ___ uniform. The day was ___ bizarre.
He checked the ___ flamingos, dancing ___. A ___ monkey, Marvin, stole his ___ clipboard, tossing it into the ___ penguin pool. The ___ penguins glared as Gerald retrieved it, now ___.
A ___ roar led Gerald to a ___ tourist feeding ___ marshmallows to ___ lions. Gerald confiscated them, dodging a ___ lion’s claws.
At lunch, the ___ cafeteria served ___ soup. Gerald chose a ___ sandwich, but a ___ raccoon stole it.
By afternoon, a ___ ostrich nabbed a ___ megaphone, squawking ___ noises. A ___ sloth triggered the ___ sprinklers, soaking the ___ crowd.
At sunset, Gerald sat on a ___ bench, his ___ shoes squelching. “What a ___ day,” he laughed, watching Marvin juggle ___ bananas. Gerald loved his ___ job, ready for another ___ adventure.'''
list_of_adjectives=["bewildered", "vast", "frayed", "smeared", "erratic", "wild", "showy", "choreographed", "plumed", "slight", "bristly", "naughty", "squeaky", "treasured", "fuzzy", "agile", "verdant", "tropical", "wicked", "muddy", "toddling", "frosty", "drenched", "fishy", "booming", "regal", "oblivious", "sparkly", "puzzled", "ravenous", "tired", "syrupy", "cranky", "jagged", "oddball", "glowing", "toxic", "moldy", "sly", "hectic", "tornado", "bizarre", "frenzied", "glossy", "gibberish", "drowsy", "wobbly", "rusty", "unaware", "icy", "radiant", "bumpy", "squishy", "fantastic", "swiped", "slick", "relentless", "quirky", "thrilling", "shimmering", "tangled", "velvety", "scorching", "whimsical", "cluttered", "dazzling", "murky", "sprightly", "gnarled", "zesty", "cavernous", "plush", "rickety", "smoldering", "ethereal", "grimy", "jubilant", "warped", "buttery", "crackling", "somber", "twinkling", "gaudy", "slimy", "spirited", "hulking", "misty", "brazen", "craggy", "lustrous", "skittish", "pungent", "gilded", "lopsided", "vibrant", "sodden", "blistering", "pristine", "gleaming", "spiky"]
dictionary={}
b=1
for i in range(1,60):
    dictionary[f'adj{i}']=random.choice(list_of_adjectives)
    


print(f''' One sunny morning, Gerald, a {dictionary['adj1']} zookeeper, arrived at the {dictionary['adj2']} Metropolis Zoo. He wore his {dictionary['adj3']}, {dictionary['adj4']} uniform, ready for another {dictionary['adj5']} day. Little did he know, this day would be {dictionary['adj6']} bizarre.

First, Gerald checked on the {dictionary['adj7']} flamingos, who were staging a {dictionary['adj8']}, {dictionary['adj9']} dance-off. “Impressive, but {dictionary['adj10']} concerning,” Gerald muttered, scratching his {dictionary['adj11']} beard. Suddenly, a {dictionary['adj12']} monkey, named Marvin, swung from a {dictionary['adj13']} vine, snatching Gerald’s {dictionary['adj14']} clipboard.

“Marvin, you {dictionary['adj15']} fiend!” Gerald shouted, chasing the {dictionary['adj16']} primate through the {dictionary['adj17']}, {dictionary['adj18']} enclosure. Marvin, with a {dictionary['adj19']} grin, tossed the clipboard into the {dictionary['adj20']} penguin pool. The {dictionary['adj21']} penguins, unimpressed, gave Gerald {dictionary['adj22']} glares as he fished it out, now {dictionary['adj23']} and {dictionary['adj24']}.

Next, Gerald heard a {dictionary['adj25']} roar from the {dictionary['adj26']} lion exhibit. He sprinted over, finding a {dictionary['adj27']} tourist tossing {dictionary['adj28']} marshmallows to the {dictionary['adj29']} lions. “They looked {dictionary['adj30']}!” the tourist explained, shrugging. Gerald, with a {dictionary['adj31']} sigh, confiscated the {dictionary['adj32']} treats, narrowly avoiding a {dictionary['adj33']} lion’s {dictionary['adj34']} claws.

As lunchtime approached, Gerald noticed the {dictionary['adj35']} cafeteria was serving {dictionary['adj36']} soup. “Looks {dictionary['adj37']},” he whispered, opting for a {dictionary['adj38']} sandwich instead. But before he could take a bite, a {dictionary['adj39']} raccoon swiped it, scampering toward the {dictionary['adj40']} petting zoo.

By afternoon, the zoo was a {dictionary['adj41']} of {dictionary['adj42']} mishaps. A {dictionary['adj43']} ostrich had stolen a {dictionary['adj44']} megaphone, squawking {dictionary['adj45']} announcements. Meanwhile, a {dictionary['adj46']} sloth, dangling from a {dictionary['adj47']} branch, accidentally triggered the {dictionary['adj48']} sprinkler system, drenching the {dictionary['adj49']} crowd in {dictionary['adj50']} water.

As the {dictionary['adj51']} sun set, Gerald collapsed on a {dictionary['adj52']} bench, his {dictionary['adj53']} shoes squelching. “What a {dictionary['adj54']} ridiculous day,” he chuckled, watching Marvin juggle {dictionary['adj55']} bananas with {dictionary['adj56']} flair. Despite the {dictionary['adj57']} chaos, Gerald loved his {dictionary['adj58']} job. Tomorrow, he’d face another {dictionary['adj59']} adventure.''')