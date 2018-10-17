type_dictionary = {
#nounphrases
    "np": [
        "address",
        "area",
        "areas",
        "barbecue",
        "breath",
        "center",
        "city",
        "food",
        "foods",
        "class",
        "canapes",
        "centre",
        "crossover",
        "downtown",
        "gastro",
        "gastropub",
        "east",
        "chiquito",
        "change",
        "damn",
        "care",
        "harbor",
        "house",
        "list",
        "music",
        "moron",
        "part",
        "parts",
        "park",
        "place",
        "prices",
        "range",
        "restaurant",
        "restaurants",
        "rice",
        "side",
        "system",
        "thing",
        "time",
        "town",
        "type",
        "venue",
        "venues",
        "world",
        "south",
        "west",
        "sock"
    ],
#nouns
    "n": [
        "address",
        "area",
        "areas",
        "barbecue",
        "breath",
        "center",
        "city",
        "food",
        "foods",
        "class",
        "canapes",
        "centre",
        "crossover",
        "downtown",
        "gastro",
        "gastropub",
        "east",
        "chiquito",
        "change",
        "damn",
        "care",
        "harbor",
        "house",
        "list",
        "music",
        "moron",
        "part",
        "parts",
        "park",
        "place",
        "prices",
        "range",
        "restaurant",
        "restaurants",
        "rice",
        "side",
        "system",
        "thing",
        "time",
        "town",
        "type",
        "venue",
        "venues",
        "world",
        "south",
        "west",
        "sock"
    ],
    "(np\\np)/(np\s)": [
        "that"
    ],

    "(n\\n)/(np\s)": [
        "that"
    ],

#adjectives
    "n/n": [
        "priced",
        "pan",
        "house",
        "harbor",
        "christmas",
        "barbecue",
        "sea",
        "gastro",
        "gastropub",
        "seafood",
        "gastro",
        "prezzo",
        "gastro",
        "canapes",
        "cambridge",
        "fusion",
        "christmas",
        "barbecue",
        "fish",
        "bistro",
        "belgium",
        "tuscan",
        "afghan",
        "african",
        "american",
        "asian",
        "australasian",
        "australian",
        "austrian",
        "basque",
        "belgian",
        "brazilian",
        "british",
        "caribbean",
        "cantonese",
        "chinese",
        "catalan",
        "cheap",
        "cuban",
        "danish",
        "english"
        "eritrean",
        "european",
        "expensive",
        "fancy",
        "fast",
        "fine",
        "french",
        "german",
        "creative",
        "corsica",
        "fusion",
        "available",
        "different",
        "central",
        "dear",
        "every",
        "else",
        "greek",
        "hindi",
        "hungarian",
        "indian",
        "indonesian",
        "irish",
        "italian",
        "jamaican",
        "japanese",
        "korean",
        "lebanese",
        "mediterranean",
        "mexican",
        "modern",
        "medium",
        "moroccan",
        "malaysian",
        "polish",
        "portuguese",
        "persian",
        "polynesian",
        "oriental",
        "good",
        "halal",
        "high",
        "international",
        "korea",
        "kosher",
        "north",
        "inner",
        "kind",
        "polynesia",
        "moderate",
        "long"
        "really",
        "romania",
        "romanian",
        "russian",
        "scandinavia",
        "scandinavian",
        "scottish",
        "singapore",
        "singaporean",
        "spanish",
        "swedish",
        "swiss",
        "thai",
        "thailand",
        "traditional",
        "turkey",
        "turkish",
        "unusual",
        "vegetarian",
        "venetian",
        "vietnam",
        "vietnamese",
        "welsh",
        "south",
        "tuscan",
        "west",
        "surprise",
        "steak",
        "steakhouse",
        "world",
    ],

    "np/n": [
        #Determiners
        "a",
        "an",
        "any",
        "anyone",
        "anything",
        "anywhere",
        "my",
        "such",
        "that",
        "the",
        "their",
        "there",
        "this",
        "some",
        #Non Determiners?
        "priced",
        "pan",
        "house",
        "harbor",
        "christmas",
        "barbecue",
        "sea",
        "gastro",
        "gastropub",
        "seafood",
        "gastro",
        "prezzo",
        "gastro",
        "canapes",
        "cambridge",
        "fusion",
        "christmas",
        "barbecue",
        "fish",
        "bistro",
        "belgium",
        "tuscan",
        "afghan",
        "african",
        "american",
        "asian",
        "australasian",
        "australian",
        "austrian",
        "basque",
        "belgian",
        "brazilian",
        "british",
        "caribbean",
        "cantonese",
        "chinese",
        "catalan",
        "cheap",
        "cuban",
        "danish",
        "english"
        "eritrean",
        "european",
        "expensive",
        "fancy",
        "fast",
        "fine",
        "french",
        "german",
        "creative",
        "corsica",
        "fusion",
        "available",
        "different",
        "central",
        "dear",
        "every",
        "else",
        "greek",
        "hindi",
        "hungarian",
        "indian",
        "indonesian",
        "irish",
        "italian",
        "jamaican",
        "japanese",
        "korean",
        "lebanese",
        "mediterranean",
        "mexican",
        "modern",
        "medium",
        "moroccan",
        "malaysian",
        "polish",
        "portuguese",
        "persian",
        "polynesian",
        "oriental",
        "good",
        "halal",
        "high",
        "international",
        "korea",
        "kosher",
        "north",
        "inner",
        "kind",
        "polynesia",
        "moderate",
        "long"
        "really",
        "romania",
        "romanian",
        "russian",
        "scandinavia",
        "scandinavian",
        "scottish",
        "singapore",
        "singaporean",
        "spanish",
        "swedish",
        "swiss",
        "thai",
        "thailand",
        "traditional",
        "turkey",
        "turkish",
        "unusual",
        "vegetarian",
        "venetian",
        "vietnam",
        "vietnamese",
        "welsh",
        "south",
        "tuscan",
        "west",
        "surprise",
        "steak",
        "steakhouse",
        "world",
    ],

#connectives
    "(s\s)/s": [
        "and",
        "but",
        "so",
        "if"
    ],

#intransitive verb
    "np\s": [
        "are",
        "am",
        "be",
        "care",
        "do",
        "did",
        "decide",
        "could",
        "eat",
        "does",
        "doesnt",
        "dont",
        "get",
        "let",
        "looking",
        "look",
        "matter",
        "meant",
        "mind"
        "should",
        "was",
        "would"
    ],

    "(np\\np)/np": [
        "serving",
        "in",
        "of"
    ],

#transitive verbs
    "(np\s)/np": [
        "find",
        "care",
        "change",
        "damn",
        "do",
        "did",
        "decide",
        "eat",
        "does"
        "doesnt",
        "dont",
        "give",
        "got",
        "help",
        "includes",
        "know",
        "like",
        "missing",
        "need",
        "needs"
        "said",
        "says",
        "searching",
        "see",
        "sells",
        "serve",
        "served",
        "serves",
        "serving",
        "try",
        "trying",
        "want",
        "about",
        "is",
        "was"
    ],
#auxiliary verbs
    "(np\s)/(np\s)": [
        "can",
        "do",
        "did",
        "could",
        "does",
        "doesnt",
        "dont",
        "have",
        "has",
        "may"
        "should",
        "wanna",
        "would"
    ],
    "(s\s)/pp":[
        "looking"
    ],
    "s/s": [
        "bye",
        "please"
    ],

#prepostions
    "pp/np": [
        "about",
        "at",
        "beside",
        "for",
        "from",
        "in",
        "of",
        "on"
        "then",
        "to",
        "with" 
    ],
#adverbs
    "s\s": [
        
        "alright",
        "fine",
        "again",
        "just",
        "not",
        "well",
        "so",
#fill
        "ah",
        "no",
        "oh",
        "ok",
        "okay"
        "uh",
        "um",
        "umh",
        "yes",
        "sorry",
        "please"
    ],

    "(n/n)/(n/n)": [
        "reasonably",
        "moderately",
    ],
#pronoun
    "s/(np\s)": [
        "what",
        "i",
        "it",
        "its",
        "me",
        "one",
        "other",
        "something",
        "they",
        "you",
        "yourself"
    ],

#sentence
    "s": [
        "how",
        "theres",
        "thats",
        "whats",
        "its",
        "iam",
        "im",
        "wanna",
        "lets",
        "id"
    ]
}
