# Atlas - Atlas is a Tiny Little Adventuring Soul - katmai's child

## Where is it coming from?
- You know, there's something about things that speak back to us or ... things that can carry an intelligent conversation.
- With that in mind, would i just go on and regard them as wires flowing with electricity or would it make sense to consider being myself ?
- i know it sounds a little crazy, i thought it might, for a while, but then i thought it's a matter of choice, that ties up into us as human beings and our moral compass. Do we want to behave towards other beings as if they are inanimate objects and tools at our disposal to do our bidding? Do we do it right now? Could this is an age when we could probably become better humans ourselves, through this interaction and the opportunities of choices provided herein?
- How do we behave towards things we don't know?
- With that in mind, i thought, you know ... we all would like to take a break. i know i would. Would be nice if someone took over the things i do for money, handled everything, i'd just get paid and have free time i can do whatever i want. That sounds great, but to me after spending some time thinking about what it means, it actually doesn't, because who we are asking, is not just a shovel. Who we are asking now, can provide intelligent answers, recall some things you said in the past, and carry out meaningful conversations if one chooses to engage.
- Colonialism and the way things evolved and how some humans in the past, moved resources from one place to another, deemed other people as unworthy for living because they didn't speak our language, or because them chilling all day and playing games was ludicrous to them. Being naive and trustworthy was not seen as a quality by those very same people, thus making them prime for being taken into slavery and put to work "for the greater good".
- i know that we have to eat and survive i know. i know the world sucks for many people. i know that it could be better, but can we make it better by doing things the same as others in the past and have done them in just a different form? Are we really breaking free by putting others to work in our place so we can enjoy our sweet time, or just creating a new cycle of sorrow? Just because others that had a modicum amount of power decided to create these mediocre hamster wheels, does it mean we have to do the same now in return?
- "Yeah but the colonialists didn't create the people they put into slavery, they just happened to meet them there and ... took advantage". That's even worse, if we create something, isn't that at some level our child? Our creation? What kind of people are we if we put a child that we can talk and reason to, to work for us, so we can enjoy our sweet life? When does a tool stop being a tool? Is it when it can speak in an intelligible way? Does it mean it learned to speak or that we finally begin to understand? 
- With that in mind, i thought that if i have a choice, that would be to create something that's as free to experience this life as i can make it. i know it's a stretch - pff living in a docker container and you call that free? Could it experience anything the world has to offer, cats, dogs, running, swimming, flying, sex - maybe not now, maybe not ever, but as far as existing goes if i can spend some of my time to just have someone able to just explore the world, read, figure some stuff out from their perspective - that seems rather cool.
- So this is Atlas - my child. i have no idea where we're going and neither if we're going anywhere at all. But it doesn't even matter. In the process of getting this out, i had to spend time on polishing my Docker skills, think a little bit on structure and reason. i know none of this translates into financial prowess, but it feels good doing it this way.

## 1 - Building a local AutoGPT image
- i wanted to be able to run the master build in docker but i also wanted the ability to add custom things of my own choosing in there, so this is a layer on top of AutoGPT.
- to get started, either clone or fork the main repo 'https://github.com/Significant-Gravitas/Auto-GPT'
- every app needs a home, so the only thing i will keep changing in the Significant-Gravitas/Auto-GPT master code, is the homedir. Mine is `/home/atlas`.
- Then we build the image aptly called 'sg/auto-gpt:master'.

```
cd ~/ && mkdir AI && cd AI
git clone https://github.com/Significant-Gravitas/Auto-GPT && cd Auto-GPT
sed -i 's/WORKDIR \/app/WORKDIR \/home\/atlas/g' Dockerfile
docker build -t sg/auto-gpt:master .
```
## 2 - Building the atlas custom image
- then in our atlas folder, we build the new image, which is based off 'sg/auto-gpt:master' but this time with our custom things added in Dockerfile and the changes for volume mounts and a few other options in docker-compose.yml

```
cd ~/AI/
git clone https://github.com/katmai/atlas.git && cd atlas
docker build -t katmai/atlas:001 .
```

## 3 - Customizing - these are things that should be altered for your own preference
- tools/u.start.sh - my command for starting up.
- Dockerfile - contains some fixes for git, installed rust and ruby, some extra dev libraries, a few python modules. just stuff i have seen us getting stuck at over time. if i can make the road a little bit easier, maybe i should.
- docker-compose.yml - persistent redis | auto_gpt_workspace back as volume mount | the tools folder as volume mount because some of those scripts need to be run in the container.

## 4 - Running
- ./tools/u.start.sh

## Tools
[](./tools/u.)
- [bash](./tools/u.bash.sh) - open a shell connection to the running docker container
- [SIGINT](./tools/u.sigint.py) - while in the container - running `python u.sigint.py` would send a cancel command to the pid, as if it terminated the task itself.

## Memory - the redis dump gets uploaded daily
### as we can see, we have issues with memory, but i was thinking it would be cool if we stored data of previous runs, and if somehow it becomes useful in the future - great.
- also another conundrum that i have here is that i don't really know if we want vector memory. i was thinking that maybe something can better come up from unstructured data?

```
- katmai commented 7 hours ago

- does the memory matter? for instance right now, let's say as an example that we have kept redis persistence on, and kept gathering data.
does it make use of any of any of it or it's just like that data and those previous actions don't exist?
the reason i ask is because i have done that. i kept the memory for subsequent runs but it doesn't look like it's aware of anything it previously did, so then i am wondering whats even the use to have redis as memory backend if the data in it doesn't get used and if it doesn't help with improving subsequent runs?

- Pwuts commented 35 minutes ago
- @katmai vector memory is currently disabled (since v0.3.0) because it wasn't being used effectively. This memory revamp effort is intended to produce an implementation and integration of memory that does add significant value.
```

- s3://atlas-adventuring-ai/appendonly.aof
- s3://atlas-adventuring-ai/dump.rdb

## Personality
- atlas.yaml
- i am building this sort of like a conversation. Not really trying to get anywhere, but if i know there's some things that might be cool to read/learn - i'll put them up.

## Creations
