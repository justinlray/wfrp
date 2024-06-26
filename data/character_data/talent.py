talent_dict = {
  'Template': ['Description', 'Source'],
  'Accute Hearing': ["Your	hearing	is	exceptionally	good.	You	gain	a	+20% bonus	on	Perception	Skill	Tests	that	involve	listening.", "Core 96"],
  'Aethyric Attunement' : [ "You are	well	attuned	to	the	Aethyr	and	can	more	easily manipulate	the	Winds	of	Magic.	You	gain	+10%	bonus	on Channelling	and	Magical	Sense	Skill	Tests.", "Core 96"],
  'Alley Cat': ["You are	at	home	on	the	streets.	You	gain	a	+10%	bonus	on	Concealment	and	Silent	Move	Skill	Tests	when	in	urban	locations.", "Core 96"],
  'Ambidextrous': ["You	can	use	either	hand	equally	well.	You	do	not	suffer the	normal	–20%	WS	or	BS	penalty	when	using	a	weapon	in your	secondary	hand", 'Core 97'],
  'Arcane Lore': ["You	have	studied	one	of	the	Empire’s	traditions	of	magic.	Arcane	Lore	is	unusual	in	that	it	is	not	one	talent,	but	many.	Such	is	the	study	and	focus	required	that	you	can	only	ever	know	one.	Each	Arcane	Lore	talent	is	a	separate	magical	proficiency,	with	the	specialty	noted	in	parenthesis.	Forexample,	Arcane	Lore	(Beasts)	is	a	different	talent	than	Arcane	Lore	(Fire).	The	most	common	Arcane	Lores,	known	as	the	Eight	Orders	of	Magic,	are	Beasts,	Death,	Fire,	the	Heavens,	Life,	Light,	Metal,	and	Shadow.	If	you	know	an	Arcane	Lore,	you	can	attempt	to	cast	any	spell	from	that	lore.	See	Chapter7: Magic	for	spell	lists	and	further	details.", 'Core 97'],
  'Armoured Casting': ["Your	prayers	help	you	cast	spells	while	wearing	armour.	Your	Casting	Roll	penalty	while	wearing	armour	is	reduced	by 3	when	you	cast	chaos	and	divine	spells.	Normally,	you’d	suffer	a	–3	penalty	for	wearing	a	mail	shirt,	for	example,	but	with	Armoured	Casting	this	penalty	would	be	reduced	to	0.", 'Core 97'],
  'Artistic':	["You	have	true	creative	talent.	You	gain	a	+20%	bonus	on	Trade	(Artist)	Tests	and	+10%	on	tests	to Evaluate objects	d’art.", 'Core 97'],
  'Contortionist': ["You	can	bend	and	manipulate	your	body	in	a	myriad	of	unnatural	ways.	You	gain	a	+10%	bonus	on	relevant	Performer	Skill	Tests	and	a	+20%	bonus	on	Agility	Tests	to	escape	from	bonds,	squeeze	through	narrow	openings,	and	so	on.", 'Core 97'],
  'Coolheaded': ["You	gain	a	permanent	+5%	bonus	to	your	Will	Power	Characteristic.	Modify	your	starting	profile	to	reflect	this	bonus.", 'Core 97'],
  'Dark Lore': ["You	have	embraced	one	of	the	forbidden	arts	of	sorcery. Dark	Lore	is	unusual	in	that	it	is	not	one	talent,	but	many.	Such	is	the	study	and	focus	required	that	you	can	only	ever	know	one.	Each	Dark	Lore	talent	is	a	separate	magical	proficiency,	with	the	specialty	noted	in	parenthesis.	Forexample,	Dark	Lore	(Chaos)	is	a	different	talent	than	DarkLore	(Necromancy).	The	most	common	Dark	Lores	are	Chaos	and	Necromancy.	Future	supplements	will	detail	additional	Dark	Lores,	including	those	of	the	Chaos	powers	Nurgle,	Slaanesh,	and	Tzeentch.	If	you	know	a	Dark	Lore,	you	can	attempt	to	cast	any	spell	from	that	lore.	See	Chapter 7: Magicfor	spell	lists	and	further	details.", 'Core 97'],
  'Dark Magic': ["You	know	how	to	manipulate	Dhar	(black	magic)	to	fuel	your	spells.	Using	Dark	Magic	gives	you	more	power,	but	is	much	more	dangerous.	When	you	cast	a	spell,	you	can	opt	to	use	the	energy	of	Dhar	to	fuel	it.	When	making	a	Casting	Roll	for	a	Dark	Magic	spell,	you	roll	an	extra	d10	and	drop	the	die	with	the	lowest	result.	However,	all	dice	count	for	the	purposes	of	Tzeentch’s	Curse.	For	example,	a	wizard	with	Magic	2	who	casts	a	dark	magic	spell	rolls	3d10	and	uses	the	highest	two	dice	for	his	Casting	Roll.	All	three	dice	are	used	to	determine	Tzeentch’s	Curse.	If	he	rolled	a	6,	6,	and	6,	the	Casting	Roll	would	be	12	(6+6),	but	the	spell	would	trigger	a	Major	Chaos	Manifestation.	You	must	use	Dark	Magic	when	casting	a	DarkLore	spell.	See	Chapter 7: Magic	for	more	information	on	spellcasting.", 'Core 97'],
  'Dealmaker': ["You are	a	slick-talking	businessman	who	knows	how	to	close	a	deal.	You	gain	a	+10%	bonus	on	Evaluate	and	Haggle	Skill	Tests.", 'Core 97'],
  'Disarm': ["If you hit with	a	melee attack, you may attempt to disarm your opponent instead of inflicting damage. Make an Opposed Agility Test. If you win, your opponent is disarmed and the weapon drops to the ground. It can be picked up with the ready action. If your opponent wins, he retains his weapon. Natural weapons (teeth, claws, etc.) cannot bedisarmed.", 'Core 97'],
  'Divine Lore': ["Your dedication to your deity is such that your prayers can produce magical effects. Divine Lore is unusual in that it is not one talent, but many different ones. Such is the devotion required that you can only ever know one Divine Lore. Each Divine Lore talent is	a	separate magical proficiency, with the specialty noted in parenthesis. For example, Divine Lore (Sigmar) is	a	different talent than Divine Lore (Ulric). The most common Divine Lores correspond to the major deities of the Old World: Manann, Morr, Myrmidia, Ranald, Sigmar, Shallya, Taal/Rhya, Ulric, Verena. If you know	a	Divine Lore, you can attempt to cast any spell from that lore. See Chapter 7: Magic for spell lists and further details.", 'Core 97-98'],
  'Dwarfcraft': ["Members	of	your	race	are	natural	craftsmen.	You	gain	a	+10%	bonus	on	tests	with	the	following	Trade	skills:	Armourer,	Brewer,	Gem	Cutter,	Gunsmith,	Miner,	Smith,	Stoneworker, and	Weaponsmith.", 'Core 98'],
  'Etiquette': ["You	are	well	versed	in	the	social	graces	of	the	upper	classes.	You	gain	a	+10%	bonus	on	Charm	and	Gossip	Skill	Tests	when	dealing	with	the	nobility.	The	bonus	also	applies	in	other	situations	in	which	knowing	the	proper	etiquette	is	important	(impersonating	a	noble	with	the	Disguise	skill,	for	instance).", 'Core 98'],
  'Excellent Vision': ["Your	eyes	are	keen.	You	gain	a	+10%	bonus	on	Perception	Skill	Tests	that	involve	sight,	and	on	Lip	Reading	Skill	Tests.", 'Core 98'],
  'Fast Hands': ["You	are	adept	at	touching	melee	opponents	during	spellcasting.	You	gain	a	+20%	Weapon	Skill	bonus	when	casting	touch	spells.", 'Core 98'],
  'Fearless': ["You are	either	brave	enough	or	crazy	enough	that	that	you	know	no	fear.	You are	immune	to	fear	and	treat	terror	as	fear.	You are	also	immune	to	the	effects	of	the	Intimidate	skill	and	the	Unsettling	talent.	See	Chapter 9: The Game Master for	more	information	on	fear	and	terror.", 'Core 98'],
  'Flee!': ["When	your	life	is	on	the	line,	you are	capable	of	impressive	bursts	of	speed.	When	running	away	from	combat	or	another	dire	threat,	you	gain	a	+1	bonus	to	your	Movement	Characteristic	for	1d10	rounds.", 'Core 98'],
  'Fleet Footed': ["You	gain	a	permanent	+1	bonus	to	your	Movement	Characteristic.	Modify	your	starting	profile	to	reflect	this	bonus."],
  'Flier': ["You	can	fly. For	more	information	on	flying,	see	Chapter 6: Combat, Damage, and Movement.", 'Core 98'],
  'Frenzy': ["You can incite yourself into	a	frothing rage. You must spend	1	round psyching yourself up (howling, biting your shield, etc.). The next round you lose control and go berserk, gaining	a	+10% bonus to Strength and Will Power but	a	–10% penalty to Weapon Skill and Intelligence. You must attack the nearest enemy in melee combat, all attacks must be all out attacks, charge attacks, or swift attacks, and you may not flee or retreat. You remain in this frenzied state until the combat is over.", 'Core 98'],
  'Frightening': ["You	have	a	frightening	appearance.	You	cause	Fear,	as	detailed	in	Chapter 9: The Game Master.", 'Core 98'],
  'Grudge-Born Fury': ["Your	people	have	a	long	list	of	grudges	against	the	various	Goblinoid	races.	Their	depredations	fill	you	with	such	fury	that	you	gain	a	+5%	bonus	to	WS	when	attacking	Orcs,	Goblins,	and	Hobgoblins.", 'Core 98'],
  'Hardy': ["You	gain	a	permanent	+1	bonus	to	your	Wounds	Characteristic.	Modify	your	starting	profile	to	reflect	this	bonus.", 'Core 98'],
  'Hedge Magic': ["You are	a	self-taught	spellcaster	who	has	figured	out	how	to	work	magic	by	trial	and	error.	You	can	cast	Petty	Magic	(Hedge)	spells	only	without	having	the	Speak	Arcane	Language	skill;	the	Petty	Magic	(Hedge)	talent	is	still	required.	You	must	roll	an	extra	d10	when	casting	a	spell.	This	does	not	add	into	your	Casting	Roll,	but	does	count	for	the	purposes	of	Tzeentch’s	Curse.	Once	you	learn	an	Arcane	Language,	you	no	longer	have	to	roll	the	extra	die.", 'Core 98'],
  'Hoverer': ["You	can	fly	low	to	the	ground.	For	more	information	on	flying,	see	Chapter 6: Combat, Damage, and Movement.", 'Core 98'],
  'Keen Senses': ["You	have	naturally	acute	senses.	You	gain	a	+20%	bonus	on	Perception	Tests.", 'Core 99'],
  'Lesser Magic': ["You know	a	spell common to all types of magic. Lesser Magic is unusual in that it is not one talent, but many, and each must be acquired individually. Each Lesser Magic talent is	a	separate spell, with the spell name noted in parenthesis. For example, Lesser Magic (Dispel) is	a	different talent than Lesser Magic (Skywalk). The most common Lesser Magic spells are Aethyric Armour, Blessed Weapon, Dispel, Magic Alarm, Magic Lock, Move, Silence, and Skywalk. See Chapter 7: Magic for more information on Lesser Magic and descriptions of the various spells. You must have	a	Petty Magic talent before you can learn	a	Lesser Magic talent.", 'Core 99'],
  'Lightning Parry': ["When you make	a	swift attack (see Chapter 6: Combat, Damage, and Movement), you can forego one of your attacks to gain	a	free parry. If you had Attacks 3, for example, you could make two attacks and gain one parry with your swift attack action. The limit of one parry per round remains in effect.", 'Core 99'],
  'Lightning Reflexes': ["You	gain	a	permanent	+5%	bonus	to	your	Agility	 Characteristic.	Modify	your	starting	profile	to	reflect	this bonus.", 'Core 99'],
  'Linguistics': ["You	have	a	natural	affinity	for	languages.	You	gain	a	+10%	bonus	on	all	Read/Write	and	Speak	Language	Skill	Tests.", 'Core 99'],
  'Luck': ["You	were	born	lucky.	At	the	most	improbable	times,	things	go	your	way.	You	gain	an	extra	Fortune	Point	each	day. See	Chapter 6: Combat, Damage, and Movement	for	more	information	about	Fortune	Points.", 'Core 99'],
  'Marksman': ["You	gain	a	permanent	+5%	bonus	to	your	Ballistic	Skill	Characteristic.	Modify	your	starting	profile	to	reflect	this	bonus.", 'Core 99'],
  'Master Gunner': ["You	reduce	the	reload	time	of	all	black	powder	weapons	by	a	half	action.	If	you	also	have	Rapid	Reload,	you	gain	the	benefits	of	both	talents	(thus	reducing	the	reload	time	of	black	powder	weapons	by	a	full	action).", 'Core 99'],
  'Master Orator': ["You	are	such	an	accomplished	orator	that	you	can	fire up	huge	crowds.	You	can	affect	100	times	the	normal	number of	people	when	using	the	Charm	skill.	You	must	have	Public	Speaking	before	you	can	gain	this	talent.", 'Core 99'],
  'Meditation': ["You	can	focus	your	mind	and	ignore	the	world	around	you.	When	performing	ritual	magic,	you	gain	a	bonus	to	your	Casting	Roll	equal	to	your	Magic	Characteristic.", 'Core 99'],
  'Menacing': ["You	have	an	imposing	presence,	due	to	size,	demeanour,	or	appearance.	You	gain	a	+10%	bonus	on	Intimidate	and	Torture	Skill	Tests.", 'Core 99'],
  'Mighty Missile': ["You	know	how	to	target	magic	missiles	to	inflict	maximum	damage.	You	gain	a	+1	bonus	on	damage	rolls	with	magic	missile	spells.", 'Core 99'],
  'Mighty Magic': ["You know how to target missile attacks so they do extra damage. You gain	a	+1 bonus on damagerolls with missile weapons.", 'Core 99'],
  'Mimic': ["You	have	an	ear	for	voices	and	accents	and	can	reproduce	them	accurately.	You	gain	a	+10%	bonus	on	Performer	(Actor,	Clown,	Comedian,	Jester	and	Storyteller)	Skill	Tests,	Disguise	Skill	Tests	if	the	disguise	has	a	verbal	component,	and	Speak	Language	Skill	Test	when	trying	to	pass	as	a	native.", 'Core 99'],
  'Natural Weapons': ["You have claws or vicious teeth that can rend apart your foes in combat. When attacking without	a	weapon, you count as being armed with	a	hand weapon. You cannot parry with your natural weapons. You cannot, for obvious reasons, be disarmed.", 'Core 100'],
  'Night Vision': ["You can see extremely well in natural darkness at distances up to 30 yards. This talent doesn’t work in total darkness, requiring illumination equivalent to starlight to function.", 'Core 100'],
  'Orientation': ["You have an instinctive feel for direction. You rarely get lost and always know the direction of north. You gain	a	+10% bonus on Navigation Skill Tests.", 'Core 100'],
  'Petty Magic': ["You know the most basic of magical techniques. Like Arcane Lore, it not one talent but many. Each Petty Magic talent is	a	separate magical proficiency, with the specialty noted in parenthesis. For example, Petty Magic (Arcane) is	a	different talent than Petty Magic (Divine). The most common Petty Magic talents	are	Arcane, Divine, and Hedge. If you know	a	Petty Magic talent and you have	a	Magic Characteristic of at least 1, you can attempt to cast any spell from that talent. See Chapter 7: Magic for spell lists and further details.", 'Core 100'],
  'Public Speaking': ["You know how to work	a	crowd. You can affect 10 times the normal number of people when using the Charm skill.", 'Core 100'],
  'Quick Draw': ["Your speedy reflexes allow you to quickly draw weapons and other items. Once per round, you can use the ready action as	a	free action.", 'Core 100'],
  'Rapid Reload': ["You can reload ranged weapons with practiced ease. You reduce the reload times of all missile weapons by	a	half action. You could reload	a	crossbow in	a	half action, for example, whereas it is normally	a	full action. If the weapon already had	a	reload time of	a	half action, it becomes	a	free action. It takes you virtually no time to reload such weapons, which allows you to make swift attacks with them. See Chapter 6: Combat, Movement, and Damage for more information on swift attacks.", 'Core 100'],
  'Resistance to Chaos': ["You	are	naturally resistant to the power of Chaos. You gain	a	+10% bonus on Will Power Tests to resist magic and other Chaos effects, and you	are	immune to Chaos mutation. However, you can never become	a	spellcaster of any type.", 'Core 100'],
  'Resistance to Disease': ["Your	constitution	allows	you	to	shrug	off	many	diseases.	You	gain	a	+10%	bonus	on	Toughness	Tests	to	resist	disease.", 'Core 100'],
  'Resistance to Magic': ["You are	naturally	resistant	to	the	effects	of	magic.	You gain	a	+10%	bonus	on	Will	Power	Tests	to	resist	magic.", 'Core 100'],
  'Resistance to Poison': ["Your	hardiness	allows	you	to	ignore	the	effects	of	many	poisons.	You	gain	a	+10%	bonus	on	Toughness	Tests	to	resist	poison.", 'Core 100'],
  'Rover': ["You are	at	home	in	the	wild.	You	gain	a	+10%	bonus	on	Concealment	and	Silent	Move	Skill	Tests	when	in	rural	locations.", 'Core 100'],
  'Savvy': ["You	gain	a	permanent	+5%	bonus	to	your	Intelligence	Characteristic.	Modify	your	starting	profile	to	reflect	this	bonus.", 'Core 100'],
  'Schemer': ["You are	a	master	of	personal	politics.	You	gain	a	+10%	bonus	on	intrigue-related	Charm	Tests	and	on	WP	Tests	to	resist	the	Charm	of	others.", 'Core 100'],
  'Seasoned Traveller': ["You have extensive travel experience. You gain	a	+10% bonus on Common Knowledge and Speak Language Skill Tests.", 'Core 100'],
  'Sharpshooter': ["You	can	make	aimed	shots	with	exceptional	accuracy.	When	you	use	the	aim	action,	your	next	ranged	attack	gains	a	+20%	Ballistic	Skill	bonus	instead	of	the	normal	+10%.", 'Core 100'],
  'Sixth Sense': ["You get	a	strange feeling when you are in grave danger, and this sometimes alerts you to trouble before it happens. When danger is afoot, the GM may secretly roll	a	test on your Will Power. If successful, the GM may tell you that you have	a	bad feeling about your situation or that you feel like you’re being watched. This talent may enable to you to avoid being surprised when the rest of your allies succumb.", 'Core 100'],
  'Specialist Weapon Group (Various)': ["You know how to use	a	group of weapons that require special training. Specialist Weapon Group is unusual in that it is not one talent, but many and each must be acquired individually. Each Specialist Weapon Group talent is	a	separate proficiency, with the specialty noted in parenthesis. For example, Specialist Weapon Group (Two-handed) is	a	different talent than Specialist Weapon Group (Throwing). The most common Specialist Weapon Group talents are: Cavalry, Crossbow, Engineer, Entangling, Fencing, Flail, Gunpowder, Longbow, Parrying, Sling, Throwing, and Two-handed. For details on the weapons included in each group, see Chapter 5: Equipment.", 'Core 100-101'],
  'Stout-Hearted': ["You	are	exceptionally	brave.	You	gain	a	+10%	bonus	on	Fear	and	Terror	Tests,	and	on	Will	Power	Tests	to	resist	Intimidate	attempts.", 'Core 101'],
  'Street Fighting': ["You	learned	how	to	brawl	in	the	gutters.	You	can	make	unarmed	attacks	with	a	+10%	bonus	to	Weapon	Skill.	Furthermore,	you	gain	a	+1	bonus	on	damage	rolls	with	unarmed	attacks.", 'Core 101'],
  'Streetwise': ["You	know	how	to	get	by	on	the	street.	You	gain	a	+10%	bonus	on	Charm	and	Gossip	Skill	Tests	when	dealing	with	the	criminal	underworld.", 'Core 101'],
  'Strike Mighty Blow': ["You	know	how	to	target	melee	attacks	so	they	do	extra	damage.	You	gain	a	+1	bonus	on	damage	rolls	with	melee	weapons.", 'Core 101'],
  'Strike to Injure': ["You’re	an	expert	at	targeting	your	enemies’	most	vulnerable	areas.	The	Critical	Value	of	any	Critical	Hits	you inflict	is	increased	by	1.", 'Core 101'],
  'Strike to Stun': ["If you	hit	with	a	melee	attack,	you	may	attempt	to	stun	your	opponent	instead	of	inflicting	damage.	First,	you	must	make	a	Strength	Test.	If	that	is	successful,	your	opponent	must	make	a	Toughness	Test,	with	a	+10%	bonus	for	each	AP	on	his	head.	If	he	fails,	your	opponent	is	stunned	for	1d10	rounds.	Stunned	characters	cannot	take	any	actions	and	cannot	dodge.", 'Core 101'],
  'Strong-Minded': ["Your	resilient	mind	is	less	susceptible	to	sanity-blasting	events.	You	don’t	have	to	check	for	insanity	until	you	have	8	Insanity	Points.", 'Core 101'],
  'Sturdy': ["You	have	a	brawny	physique.	You	do	not	suffer	any	Movement	penalties	while	wearing	heavy/plate	armour.	If you are	using	Encumbrance	values	with	a	character	who	has	the	sturdy	talent	ignore	the	Encumbrance	values	of	the	armour worn,	though	the	–10%	Agility	modifier	still	applies.	See	Chapter 5: Equipment	for	more	information	about	armour.", 'Core 101'],
  'Suave': ["You	gain	a	permanent	+5%	bonus	to	your	Fellowship	Characteristic.	Modify	your	starting	profile	to	reflect	this bonus.", 'Core 101'],
  'Sure Shot': ["You	know	how	to	find	the	weak	spots	in	your	enemies’	armour.	When	you	hit	with	a	ranged	attack,	you	can	ignore	1	Armour	Point.	If	your	target	has	no	armour,	this	talent	has	no effect.", 'Core 101-102'],
  'Surgery': ["You	know	the	most	advanced	scientific	healing	techniques.	You	gain	a	+10%	on	Heal	Skill	Tests.	If you are treating	a	heavily	wounded	patient,	a	successful	test	heals	2	Wounds	instead	of	the	normal	1.	If	this	character	is	in	danger	of	losing	a	limb	from	a	Critical	Hit	(see	Chapter 6: Combat, Damage, and Movement),	you	also	provide	the	patient	with	a	+20%	Toughness	bonus	on	the	test	to	resist	limb	loss.", 'Core 102'],
  'Super Numerate': ["You	have	a	gift	for	calculation	and	can	work	out	a	solution	for	nearly	any	mathematical	problem	given	time.	You gain	a	+10%	bonus	on	Gamble	and	Navigation	Skill	Tests,	and	a	+20%	bonus	on	Perception	Skill	Tests	that	involve	estimation.", 'Core 102'],
  'Swashbuckler': ["You	are	an	agile	combatant.	You	can	use	the	Jump/Leap	action	as	a	half	action	and	you	increase	the	distance	of	all	leaps	by	1	yard.", 'Core 102'],
  'Terrifying': ["One	look	at	your	monstrous	countenance	sends	enemies	running.	You	cause	terror,	as	detailed	in	Chapter 9: The Game Master.", 'Core 102'],
  'Trapfinder': ["You	are	an	expert	at	dealing	with	traps.	You	gain	a	+10%	bonus	to	Perception	and	Pick	Lock	Tests	that	deal	with	locating	and	disarming	traps.", 'Core 102'],
  'Trick Riding': ["You are capable of amazing feats on horseback. You can do handstands on	a	galloping mount, leap from horse to horse, and the like. You only need to take Ride Skill Tests under the mostextreme circumstances, and even then you gain	a	+10% bonus.", 'Core 102'],
  'Tunnel Rat': ["You are	at	home	beneath	the	earth.	You	gain	a	+10%	bonus	on	Concealment	and	Silent	Move	Skill	Tests	when	in	underground	locations.", 'Core 102'],
  'Undead': ["You are	a	creature of undeath, hideously reanimated by necromantic magic (see Chapter 7: Magic). You are immune to Fear, Terror, stunning, poison, disease, and all spells, skills, and effects that involve the manipulation of emotions and the mind.", 'Core 102'],
  'Unsettling': ["Your daunting presence disturbs your opponents. Enemies must make	a	successful Will Power Test on seeing you or suffer	a	–10% penalty to their Weapon Skill and Ballistic Skill. They may test to overcome the effects this talent each round until they either make it or are out of sight of you.", 'Core 102'],
  'Very Resilient': ["You gain	a	permanent +5% bonus to yourToughness Characteristic. Modify your starting profile to reflect this bonus.", 'Core 102'],
  'Very Strong': ["You gain	a	permanent +5% bonus to your	Strength Characteristic. Modify your starting profile to reflect this bonus.", 'Core 102'],
  'Warrior Born': ["You gain	a	permanent +5% bonus to your Weapon Skill Characteristic. Modify your starting profile to reflect this bonus.", 'Core 102'],
  'Wrestling': ["You are	an	expert	grappler.	You	can	make	unarmed	attacks	with	a	+10%	bonus	to	Weapon	Skill	when	attempting	to	grapple.	Furthermore,	you	gain	a	+10%	bonus	on		grappling	Strength	Tests.", 'Core 102']
}