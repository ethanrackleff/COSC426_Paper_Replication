import csv
import pandas as pd



def generate_sentences_PP(pluralNouns_all, pluralNouns_anim, singNouns_anim, singNouns_all, smallVerbSet_sing, smallVerbSet_plur, largeVerbSetPlural, largeVerbSetSing, adjectives, is_are):
    # making array 
    sentidArr = []
    comparisonArr=[]
    pairidArr = []
    contextidArr =[]
    lemmaArr = []
    conditionArr = []
    pronounArr = []
    sentenceArr = []
    roiArr = []
    
    contextId = 1
    sentId = 1
    pairId = 1
    lemma = ''
    condition = True
    roi = 5
    flag = False  # if taxi driver in noun 2?
    for noun1 in pluralNouns_all:
        if noun1[0]  == 't': 
            roi+=1
        for noun2 in pluralNouns_anim:
            if noun2[0]  == 't': 
                roi+=1
                flag = True
            for verb1 in smallVerbSet_sing:
                i = 0
                for i in range(len(largeVerbSetPlural)):
                    verb2 = largeVerbSetPlural[i]
                    # Write “the noun the noun2 verb verb2”
                    sentenceArr.append("The "+ noun1+ " the "+noun2+" "+verb1+" "+verb2+".")
                    # write unexpected
                    comparisonArr.append("unexpected")
                    pairidArr.append(pairId)
                    contextidArr.append(contextId)
                    lemmaArr.append(verb2)
                    sentidArr.append(sentId)
                    conditionArr.append(1)
                    pronounArr.append('na')
                    roiArr.append(roi)
                    sentId+=1
                    
                    # Write “the noun the noun2 verb listofbigverbs_sing[i]”
                    sentenceArr.append("The "+ noun1+" the "+noun2+" "+verb1+" "+largeVerbSetSing[i]+".")
                    # Write “expected”
                    i+=1
                    comparisonArr.append("expected")
                    sentidArr.append(sentId)
                    sentId+=1
                    pairidArr.append(pairId)
                    pairId+=1
                    contextidArr.append(contextId)
                    # Write lemma “verb2” 
                    lemmaArr.append(verb2)
                    conditionArr.append(1)
                    pronounArr.append('na')
                    roiArr.append(roi)
                contextId+=1
                # roi += 1 
                for adj in adjectives:
                    for be in is_are:
                        # Write “the noun the noun2 verb be adj”
                        if be == 'is':
                            comparisonArr.append("unexpected")
                        else: #are
                            comparisonArr.append("expected")
                        sentenceArr.append("The "+ noun1+" the "+noun2+" "+verb1+" "+ be +" "+adj+".")
                        sentidArr.append(sentId)
                        sentId+=1
                        lemmaArr.append('be')
                        pairidArr.append(pairId)
                        contextidArr.append(contextId)
                        conditionArr.append(1)
                        pronounArr.append('na')
                        roiArr.append(roi)
                    pairId+=1
                    contextId+=1
                if flag == True:
                    roi-=1
                    flag = False
            roi = 5

    for noun1 in pluralNouns_all:
        if noun1[0]  == 't': 
            roi+=1
        for noun2 in singNouns_anim:
            if noun2[0]  == 't': 
                roi+=1
                flag = True
            for verb1 in smallVerbSet_plur:
                i = 0
                for i in range(len(largeVerbSetPlural)):
                    verb2 = largeVerbSetPlural[i]
                    # Write “the noun the noun2 verb verb2”
                    sentenceArr.append("The "+ noun1+ " the "+noun2+" "+verb1+" "+verb2+".")
                    # write unexpected
                    comparisonArr.append("unexpected")
                    pairidArr.append(pairId)
                    contextidArr.append(contextId)
                    lemmaArr.append(verb2)
                    sentidArr.append(sentId)
                    conditionArr.append(1)
                    pronounArr.append('na')
                    roiArr.append(roi)
                    sentId+=1
                    
                    # Write “the noun the noun2 verb listofbigverbs_sing[i]”
                    sentenceArr.append("The "+ noun1+" the "+noun2+" "+verb1+" "+largeVerbSetSing[i]+".")
                    # Write “expected”
                    i+=1
                    comparisonArr.append("expected")
                    sentidArr.append(sentId)
                    sentId+=1
                    pairidArr.append(pairId)
                    pairId+=1
                    contextidArr.append(contextId)
                    # Write lemma “verb2” 
                    lemmaArr.append(verb2)
                    conditionArr.append(1)
                    pronounArr.append('na')
                    roiArr.append(roi)
                contextId+=1
                # roi += 1 
                for adj in adjectives:
                    for be in is_are:
                        # Write “the noun the noun2 verb be adj”
                        if be == 'is':
                            comparisonArr.append("unexpected")
                        else: #are
                            comparisonArr.append("expected")
                        sentenceArr.append("The "+ noun1+" the "+noun2+" "+verb1+" "+ be +" "+adj+".")
                        sentidArr.append(sentId)
                        sentId+=1
                        lemmaArr.append('be')
                        pairidArr.append(pairId)
                        contextidArr.append(contextId)
                        conditionArr.append(1)
                        pronounArr.append('na')
                        roiArr.append(roi)
                    pairId+=1
                    contextId+=1
                if flag == True:
                    roi-=1
                    flag = False
            roi = 5

    for noun1 in singNouns_all:
        if noun1[0]  == 't': 
            roi+=1
        for noun2 in pluralNouns_anim:
            if noun2[0]  == 't': 
                roi+=1
                flag = True
            for verb1 in smallVerbSet_sing:
                i = 0
                for i in range(len(largeVerbSetPlural)):
                    verb2 = largeVerbSetPlural[i]
                    # Write “the noun the noun2 verb verb2”
                    sentenceArr.append("The "+ noun1+ " the "+noun2+" "+verb1+" "+verb2+".")
                    # write unexpected
                    comparisonArr.append("expected")
                    pairidArr.append(pairId)
                    contextidArr.append(contextId)
                    lemmaArr.append(verb2)
                    sentidArr.append(sentId)
                    conditionArr.append(1)
                    pronounArr.append('na')
                    roiArr.append(roi)
                    sentId+=1
                    
                    # Write “the noun the noun2 verb listofbigverbs_sing[i]”
                    sentenceArr.append("The "+ noun1+" the "+noun2+" "+verb1+" "+largeVerbSetSing[i]+".")
                    # Write “expected”
                    i+=1
                    comparisonArr.append("unexpected")
                    sentidArr.append(sentId)
                    sentId+=1
                    pairidArr.append(pairId)
                    pairId+=1
                    contextidArr.append(contextId)
                    # Write lemma “verb2” 
                    lemmaArr.append(verb2)
                    conditionArr.append(1)
                    pronounArr.append('na')
                    roiArr.append(roi)
                contextId+=1
                # roi += 1 
                for adj in adjectives:
                    for be in is_are:
                        # Write “the noun the noun2 verb be adj”
                        if be == 'is':
                            comparisonArr.append("expected")
                        else: #are
                            comparisonArr.append("unexpected")
                        sentenceArr.append("The "+ noun1+" the "+noun2+" "+verb1+" "+ be +" "+adj+".")
                        sentidArr.append(sentId)
                        sentId+=1
                        lemmaArr.append('be')
                        pairidArr.append(pairId)
                        contextidArr.append(contextId)
                        conditionArr.append(1)
                        pronounArr.append('na')
                        roiArr.append(roi)
                    pairId+=1
                    contextId+=1
                if flag == True:
                    roi-=1
                    flag = False
            roi = 5


    for noun1 in singNouns_all:
        if noun1[0]  == 't': 
            roi+=1
        for noun2 in singNouns_anim:
            if noun2[0]  == 't': 
                roi+=1
                flag = True
            for verb1 in smallVerbSet_plur:
                i = 0
                for i in range(len(largeVerbSetPlural)):
                    verb2 = largeVerbSetPlural[i]
                    # Write “the noun the noun2 verb verb2”
                    sentenceArr.append("The "+ noun1+ " the "+noun2+" "+verb1+" "+verb2+".")
                    # write unexpected
                    comparisonArr.append("expected")
                    pairidArr.append(pairId)
                    contextidArr.append(contextId)
                    lemmaArr.append(verb2)
                    sentidArr.append(sentId)
                    conditionArr.append(1)
                    pronounArr.append('na')
                    roiArr.append(roi)
                    sentId+=1
                    
                    # Write “the noun the noun2 verb listofbigverbs_sing[i]”
                    sentenceArr.append("The "+ noun1+" the "+noun2+" "+verb1+" "+largeVerbSetSing[i]+".")
                    # Write “expected”
                    i+=1
                    comparisonArr.append("unexpected")
                    sentidArr.append(sentId)
                    sentId+=1
                    pairidArr.append(pairId)
                    pairId+=1
                    contextidArr.append(contextId)
                    # Write lemma “verb2” 
                    lemmaArr.append(verb2)
                    conditionArr.append(1)
                    pronounArr.append('na')
                    roiArr.append(roi)
                contextId+=1
                # roi += 1 
                for adj in adjectives:
                    for be in is_are:
                        # Write “the noun the noun2 verb be adj”
                        if be == 'is':
                            comparisonArr.append("expected")
                        else: #are
                            comparisonArr.append("unexpected")
                        sentenceArr.append("The "+ noun1+" the "+noun2+" "+verb1+" "+ be +" "+adj+".")
                        sentidArr.append(sentId)
                        sentId+=1
                        lemmaArr.append('be')
                        pairidArr.append(pairId)
                        contextidArr.append(contextId)
                        conditionArr.append(1)
                        pronounArr.append('na')
                        roiArr.append(roi)
                    pairId+=1
                    contextId+=1
                if flag == True:
                    roi-=1
                    flag = False
            roi = 5

    
    df = pd.DataFrame()
    df['sentid'] = sentidArr
    df['comparison'] = comparisonArr
    df['pairid'] = pairidArr
    df['contextid'] = contextidArr
    df['lemma'] = lemmaArr
    df['condition'] = conditionArr
    df['pronoun'] = pronounArr
    df['sentence'] = sentenceArr
    df['ROI'] = roiArr 
    df.to_csv('TSE_bert_data.tsv', sep="\t")
    return df

    # def generate_sentences_PS():
        
    # def generate_sentences_SP():

    # def generate_sentences_PP():

def main():
        Nouns_plur_all_less = ['ministers', 'pilots', 'architects', 'managers', 'dancers', 'books',  'movies', 'games']
        Nouns_plur_anim_less = ['chefs', 'senators', 'skaters', 'teachers', 'farmers', 'customers']
        Nouns_sing_all_less = ['minister', 'pilot', 'architect', 'manager', 'dancer', 'book',  'movie', 'game']
        Nouns_sing_anim_less = ['chef', 'senator', 'skater', 'teacher', 'farmer', 'customer']
        Nouns_plur_all= ['surgeons', 'officers', 'authors', 'ministers', 'pilots', 'architects', 'managers', 'dancers', 'executives', 'consultants', 'taxi drivers', 'guards', 'assistants', 'parents', 'chefs', 'senators', 'skaters', 'teachers', 'farmers', 'customers', 'books',  'movies', 'games']
        Nouns_plur_anim = ['surgeons', 'officers', 'authors', 'ministers', 'pilots', 'architects', 'managers', 'dancers', 'executives', 'consultants', 'taxi drivers', 'guards', 'assistants', 'parents', 'chefs', 'senators', 'skaters', 'teachers', 'farmers', 'customers']
        Nouns_sing_anim_all = ['teacher', 'manager', 'executive', 'customer', 'minister', 'author', 'consultant', 'parent', 'officer', 'surgeon', 'assistant', 'taxi driver', 'guard', 'chef', 'skater', 'pilot', 'farmer', 'dancer', 'senator', 'architect', 'book',  'movie', 'game']
        Nouns_sing_anim = ['teacher', 'manager', 'executive', 'customer', 'minister', 'author', 'consultant', 'parent', 'officer', 'surgeon', 'assistant', 'taxi driver', 'guard', 'chef', 'skater', 'pilot', 'farmer', 'dancer', 'senator', 'architect']
        Tse_verb_sing= ['laugh', 'swim', 'smile']
        Tse_verb_plur= ['laughs', 'swims', 'smiles']
        Listofsmallverbs_sing= ['like', 'admire', 'hate', 'love' ]
        Listofsmallverbs_plur= ['likes', 'admires', 'hates', 'loves' ]
        is_are= ['are', 'is']
        adjs= ['tall', 'old', 'young', 'short']
        Listof_bigverbs_sing= ['abandon', 'absorb', 'accept', 'accompany', 'accrue', 'acquire', 'add', 'administer', 'advance', 'afford', 'aid', 'alienate', 'allocate', 'amalgamate', 'amend', 'analyze', 'antagonize', 'appear', 'apply', 'approach', 'arm', 'arrive', 'assemble', 'assimilate', 'assume', 'attack', 'attest', 'audit', 'autograph', 'await', 'balance', 'band', 'bankrupt', 'bash', 'beat', 'begin', 'bellow', 'bet', 'blackmail', 'blend', 'blow', 'board', 'bolster', 'born', 'bounce', 'branch', 'break', 'bribe', 'broadcast', 'buck', 'buffet', 'buoy', 'buttress', 'calculate', 'cap', 'careen', 'cast', 'cause', 'celebrate', 'challenge', 'charge', 'chauffeur', 'chew', 'choose', 'circulate', 'clamp', 'clean', 'climb', 'close', 'coax', 'cohost', 'collect', 'command', 'commercialize', 'compel', 'complain', 'comply', 'compute', 'conceive', 'condemn', 'confirm', 'confuse', 'conquer', 'consist', 'constrain', 'consume', 'contemporize', 'contract', 'convene', 'convince', 'coordinate', 'corner', 'cosponsor', 'countenance', 'court', 'crank', 'create', 'crimp', 'crumble', 'cuff', 'curry', 'dabble', 'dance', 'deal', 'deceive', 'decrease', 'defect', 'deflect', 'delay', 'deliver', 'democratize', 'deny', 'deposit', 'deregulate', 'design', 'destroy', 'determine', 'devote', 'differ', 'dignify', 'direct', 'disarm', 'discard', 'disconnect', 'discover', 'disengage', 'dismantle', 'disparage', 'displace', 'dispute', 'dissipate', 'distance', 'distribute', 'divert', 'doctor', 'don', 'downsize', 'drape', 'drift', 'drop', 'dump', 'ease', 'echo', 'edit', 'elect', 'embark', 'emerge', 'employ', 'enact', 'encourage', 'endorse', 'engineer', 'enlarge', 'ensure', 'entitle', 'equal', 'erase', 'escalate', 'evade', 'exacerbate', 'except', 'excuse', 'exhaust', 'exorcize', 'expel', 'explode', 'expose', 'extinguish', 'fabricate', 'fade', 'familiarize', 'fashion', 'feed', 'ferry', 'fight', 'finance', 'finger', 'fit', 'flaunt', 'flip', 'flourish', 'fly', 'fold', 'force', 'forge', 'form', 'franchise', 'fret', 'fuel', 'funnel', 'galvanize', 'gasp', 'generalize', 'glamorize', 'gloat', 'gore', 'grant', 'ground', 'guard', 'guzzle', 'hammer', 'handle', 'harm', 'haunt', 'hear', 'heighten', 'hide', 'hint', 'hold', 'hope', 'hurry', 'ignite', 'imagine', 'implement', 'impose', 'improve', 'incorporate', 'indicate', 'industrialize', 'inflict', 'infuriate', 'initiate', 'insist', 'instill', 'integrate', 'interest', 'interview', 'invest', 'involve', 'issue', 'join', 'juggle', 'keep', 'kill', 'kowtow', 'land', 'laugh', 'lead', 'lease', 'legitimize', 'let', 'license', 'lighten', 'linger', 'list', 'loan', 'lodge', 'loosen', 'lower', 'make', 'manipulate', 'market', 'match', 'maul', 'mediate', 'mention', 'migrate', 'mince', 'misinterpret', 'mitigate', 'model', 'mollify', 'motivate', 'mull', 'mute', 'navigate', 'network', 'notch', 'nudge', 'object', 'occupy', 'offset', 'operate', 'organize', 'outlast', 'outsell', 'overcome', 'override', 'overthrow', 'own', 'paint', 'panic', 'parry', 'pave', 'peddle', 'perform', 'persuade', 'pile', 'pit', 'plague', 'plead', 'pluck', 'point', 'pollinate', 'popularize', 'pose', 'postpone', 'pour', 'preclude', 'prepare', 'present', 'prevail', 'probe', 'prod', 'program', 'prolong', 'prop', 'protect', 'provoke', 'pull', 'punish', 'put', 'quarrel', 'quit', 'raid', 'ramp', 'ratify', 'react', 'reap', 'reassert', 'rebuild', 'receive', 'recommend', 'record', 'redeem', 'redo', 'refinance', 'refrain', 'regain', 'regroup', 'reimpose', 'reinvest', 'rejuvenate', 'relax', 'relish', 'remake', 'remind', 'renew', 'reopen', 'repay', 'replace', 'report', 'reproduce', 'reschedule', 'resemble', 'reshape', 'resolve', 'rest', 'restrict', 'resurrect', 'retrieve', 'revamp', 'revise', 'revolutionize', 'ride', 'rival', 'root', 'ruin', 'sacrifice', 'save', 'scan', 'scrap', 'scuttle', 'see', 'select', 'separate', 'settle', 'shape', 'shell', 'ship', 'shore', 'show', 'side', 'simplify', 'ski', 'slash', 'slog', 'smile', 'sneak', 'socialize', 'sound', 'spawn', 'speed', 'spin', 'spread', 'squeeze', 'stage', 'stand', 'start', 'stay', 'step', 'stipulate', 'stop', 'stress', 'strip', 'study', 'subordinate', 'substantiate', 'suffer', 'supersede', 'suppose', 'surpass', 'survey', 'sustain', 'sweat', 'switch', 'take', 'target', 'team', 'test', 'thrash', 'tick', 'time', 'torment', 'track', 'transform', 'treat', 'trust', 'uncover', 'underscore', 'unite', 'unravel', 'upset', 'vacillate', 'vault', 'visit', 'vote', 'wake', 'warn', 'weaken', 'welcome', 'win', 'withdraw', 'work', 'wreak']
        Listofbigverbs_plur= ['abandons', 'absorbs', 'accepts', 'accompanies', 'accrues', 'acquires', 'adds', 'administers', 'advances', 'affords', 'aids', 'alienates', 'allocates', 'amalgamates', 'amends', 'analyzes', 'antagonizes', 'appears', 'applies', 'approaches', 'arms', 'arrives', 'assembles', 'assimilates', 'assumes', 'attacks', 'attests', 'audits', 'autographs', 'awaits', 'balances', 'bands', 'bankrupts', 'bashes', 'beats', 'begins', 'bellows', 'bets', 'blackmails', 'blends', 'blows', 'boards', 'bolsters', 'is born', 'bounces', 'branches', 'breaks', 'bribes', 'broadcasts', 'bucks', 'buffets', 'buoys', 'buttresses', 'calculates', 'caps', 'careens', 'casts', 'causes', 'celebrates', 'challenges', 'charges', 'chauffeurs', 'chews', 'chooses', 'circulates', 'clamps', 'cleans', 'climbs', 'closes', 'coaxes', 'cohosts', 'collects', 'commands', 'commercializes', 'compels', 'complains', 'complies', 'computes', 'conceives', 'condemns', 'confirms', 'confuses', 'conquers', 'consists', 'constrains', 'consumes', 'contemporizes', 'contracts', 'convenes', 'convinces', 'coordinates', 'corners', 'cosponsors', 'countenances', 'courts', 'cranks', 'creates', 'crimps', 'crumbles', 'cuffs', 'curries', 'dabbles', 'dances', 'deals', 'deceives', 'decreases', 'defects', 'deflects', 'delays', 'delivers', 'democratizes', 'denies', 'deposits', 'deregulates', 'designs', 'destroys', 'determines', 'devotes', 'differs', 'dignifies', 'directs', 'disarms', 'discards', 'disconnects', 'discovers', 'disengages', 'dismantles', 'disparages', 'displaces', 'disputes', 'dissipates', 'distances', 'distributes', 'diverts', 'doctors', 'dons', 'downsizes', 'drapes', 'drifts', 'drops', 'dumps', 'eases', 'echoes', 'edits', 'elects', 'embarks', 'emerges', 'employs', 'enacts', 'encourages', 'endorses', 'engineers', 'enlarges', 'ensures', 'entitles', 'equals', 'erases', 'escalates', 'evades', 'exacerbates', 'excepts', 'excuses', 'exhausts', 'exorcizes', 'expels', 'explodes', 'exposes', 'extinguishes', 'fabricates', 'fades', 'familiarizes', 'fashions', 'feeds', 'ferries', 'fights', 'finances', 'fingers', 'fits', 'flaunts', 'flips', 'flourishes', 'flies', 'folds', 'forces', 'forges', 'forms', 'franchises', 'frets', 'fuels', 'funnels', 'galvanizes', 'gasps', 'generalizes', 'glamorizes', 'gloats', 'gores', 'grants', 'grounds', 'guards', 'guzzles', 'hammers', 'handles', 'harms', 'haunts', 'hears', 'heightens', 'hides', 'hints', 'holds', 'hopes', 'hurries', 'ignites', 'imagines', 'implements', 'imposes', 'improves', 'incorporates', 'indicates', 'industrializes', 'inflicts', 'infuriates', 'initiates', 'insists', 'instills', 'integrates', 'interests', 'interviews', 'invests', 'involves', 'issues', 'joins', 'juggles', 'keeps', 'kills', 'kowtows', 'lands', 'laughs', 'leads', 'leases', 'legitimizes', 'lets', 'licenses', 'lightens', 'lingers', 'lists', 'loans', 'lodges', 'loosens', 'lowers', 'makes', 'manipulates', 'markets', 'matches', 'mauls', 'mediates', 'mentions', 'migrates', 'minces', 'misinterprets', 'mitigates', 'models', 'mollifies', 'motivates', 'mulls', 'mutes', 'navigates', 'networks', 'notches', 'nudges', 'objects', 'occupies', 'offsets', 'operates', 'organizes', 'outlasts', 'outsells', 'overcomes', 'overrides', 'overthrows', 'owns', 'paints', 'panics', 'parries', 'paves', 'peddles', 'performs', 'persuades', 'piles', 'pits', 'plagues', 'pleads', 'plucks', 'points', 'pollinates', 'popularizes', 'poses', 'postpones', 'pours', 'precludes', 'prepares', 'presents', 'prevails', 'probes', 'prods', 'programs', 'prolongs', 'props', 'protects', 'provokes', 'pulls', 'punishes', 'puts', 'quarrels', 'quits', 'raids', 'ramps', 'ratifies', 'reacts', 'reaps', 'reasserts', 'rebuilds', 'receives', 'recommends', 'records', 'redeems', 'redoes', 'refinances', 'refrains', 'regains', 'regroups', 'reimposes', 'reinvests', 'rejuvenates', 'relaxes', 'relishes', 'remakes', 'reminds', 'renews', 'reopens', 'repays', 'replaces', 'reports', 'reproduces', 'reschedules', 'resembles', 'reshapes', 'resolves', 'rests', 'restricts', 'resurrects', 'retrieves', 'revamps', 'revises', 'revolutionizes', 'rides', 'rivals', 'roots', 'ruins', 'sacrifices', 'saves', 'scans', 'scraps', 'scuttles', 'sees', 'selects', 'separates', 'settles', 'shapes', 'shells', 'ships', 'shores', 'shows', 'sides', 'simplifies', 'skis', 'slashes', 'slogs', 'smiles', 'sneaks', 'socializes', 'sounds', 'spawns', 'speeds', 'spins', 'spreads', 'squeezes', 'stages', 'stands', 'starts', 'stays', 'steps', 'stipulates', 'stops', 'stresses', 'strips', 'studies', 'subordinates', 'substantiates', 'suffers', 'supersedes', 'supposes', 'surpasses', 'surveys', 'sustains', 'sweats', 'switches', 'takes', 'targets', 'teams', 'tests', 'thrashes', 'ticks', 'times', 'torments', 'tracks', 'transforms', 'treats', 'trusts', 'uncovers', 'underscores', 'unites', 'unravels', 'upsets', 'vacillates', 'vaults', 'visits', 'votes', 'wakes', 'warns', 'weakens', 'welcomes', 'wins', 'withdraws', 'works', 'wreaks']
        print(generate_sentences_PP(Nouns_plur_all_less, Nouns_plur_anim_less, Nouns_sing_anim_less, Nouns_sing_all_less, Listofsmallverbs_sing, Listofsmallverbs_plur, Tse_verb_sing, Tse_verb_plur, adjs, is_are))
main()

