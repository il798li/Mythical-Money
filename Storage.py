import random, json, discord, math,	time, threading, typing
shop = {
	'gold': {
		'buy': 1000,
		'single': 'Gold',
		'plural': 'Gold'
	},
	'sapphire': {
		'buy': 5000,
		'single': 'Sapphire',
		'plural': 'Sapphires'
	},
	'emerald': {
		'buy': 10000,
		'single': 'Emerald',
		'plural': 'Emeralds'
	},
	'ruby' : {
		'buy': 25000,
		'single' : 'Ruby',
		'plural' : 'Rubies'
	},
	'bone': {
		'buy': 1000,
		'single': 'Bone',
		'plural': 'Bones'
	},
	'mist': {
		'buy': 5000,
		'single': 'Mist',
		'plural': 'Mist'
	},
	'fang': {
		'buy': 10000,
		'single': 'Fang',
		'plural': 'Fangs'
	},
	'flamer': {
		'buy': 25000,
		'single': 'Flamer',
		'plural': 'Flamers'
	},
	'acacia': {
		'buy': 1000,
		'single': 'Acacia Wood',
		'plural': 'Acacia Wood'
	},
	'birch': {
		'buy': 5000,
		'single': 'Birch Wood',
		'plural': 'Birch Wood'
	},
	'oak': {
		'buy': 10000,
		'single': 'Oak Wood',
		'plural': 'Oak Wood'
	},
	'spruce': {
		'buy': 25000,
		'single': 'Spruce Wood',
		'plural': 'Spruce Wood'
	},
	'wheat': {
		'buy': 1000,
		'single': 'Wheat',
		'plural': 'Wheat'
	},
	'corn': {
		'buy': 5000,
		'single': 'Corn',
		'plural': 'Corn'
	},
	'watermelon': {
		'buy': 10000,
		'single': 'Watermelon',
		'plural': 'Watermelons'
	},
	'pumpkin': {
		'buy': 25000,
		'single': 'Pumpkin',
		'plural': 'Pumpkins'
	}
}
def load (
	file: str = 'JSON/Profiles.json'
):
	return json . load(
		open (
			file
		)
	)
def dump(
	dictionary: dict,
	file: str = 'JSON/Profiles.json',
	indent: int = 4,
	sort_keys: bool = False
):
	json.dump(
		dictionary,
		open(
			file,
			'w'
		),
		indent = indent,
		sort_keys = sort_keys,
	)
def register(
	user: discord.User
):
	profiles = load(
		'JSON/Profiles.json'
	)
	if str(
		user.id
	) in profiles.keys() or user.bot:
		return 'Invalid user!'
	profiles[
		str(
			user.id
		)
	] = {
		'coins': 0,
		'armor': {
			'helmet': {
				'name': 'Starter Helmet',
				'health': 5,
				'defense': 0.99749056993368110473970777745431,
			},
			'chestplate': {
				'name': 'Starter Chestplate',
				'health': 8,
				'defense': 0.99749056993368110473970777745431
			}, 
			'leggings': {
				'name': 'Starter Leggings', 
				'health': 8, 
				'defense': 0.99749056993368110473970777745431
			}, 
			'boots': {
				'name': 'Starter Boots', 
				'health': 8, 
				'defense': 0.99749056993368110473970777745431
			}
		},
		'tools': {
			'weapon': {
				'name': 'Starter Sword',
				'entities': 1, 
				'chances': {
					'zombie': 100, 
					'ghost': 0, 
					'vampire': 0,
					'blazer': 0
				},
				'damage': 1
			}, 
			'hoe': {
				'name': 'Starter Hoe',
				'entities': 1,
				'chances': {
					'wheat': 100, 
					'corn': 0, 
					'watermelon': 0, 
					'pumpkin': 0
				}
			}, 
			'pickaxe': {
				'name': 'Starter Pickaxe', 
				'entities': 1, 
				'chances': {
					'copper': 100, 
					'gold': 0, 
					'diamond': 0, 
					'titanium': 0
				}
			}, 
			'axe': {
				'name': 'Starter Axe', 
				'entities': 1, 
				'chances': {
					'acacia': 100, 
					'birch': 0,
					'oak': 0, 
					'spruce': 0
				}
			}
		},
		'inventory': {
			'bone': 0,
			'mist': 0,
			'fang': 0,
			'flamer': 0,
			'copper': 0,
			'gold': 0,
			'diamond': 0,
			'titanium': 0,
			'acacia': 0,
			'birch': 0,
			'oak': 0,
			'spruce': 0,
			'wheat': 0,
			'corn': 0,
			'watermelon': 0,
			'pumpkin': 0
		}
	}
	dump(
		profiles,
		'json/profiles.json'
	)
	return 'Registered user!'
craftables = {
	'bone dagger': {
		'name': 'Bone Dagger',
		'damage': 2.5,
		'recipe': {
			'bone': 10
		},
		'chances': {
			'zombie': 997,
			'ghost': 1,
			'vampire': 1,
			'blazer': 1
		},
		'entities': 5,
		'destination': [
			'tools',
			'weapon'
		]
	},
	'misty dagger': {
		'name': 'Misty Dagger',
		'damage': 5,
		'recipe': {
			'mist': 100
		},
		'chances': {
			'zombie': 1,
			'ghost': 997,
			'vampire': 1,
			'blazer': 1
		},
		'entities': 10,
		'destination': [
			'tools',
			'weapon'
		]
	},
	'bloody dagger': {
		'name': 'Bloody Dagger',
		'damage': 7.5,
		'recipe': {
			'fang': 1000
		},
		'chances': {
			'zombie': 1,
			'ghost': 1,
			'vampire': 997,
			'blazer': 1
		},
		'entities': 15,
		'destination': [
			'tools',
			'weapon'
		]
	},
	'flaming dagger': {
		'name': 'Flaming Dagger',
		'damage': 10,
		'recipe': {
			'flamer': 10000
		},
		'chances': {
			'zombie': 1,
			'ghost': 1,
			'vampire': 1,
			'blazer': 997
		},
		'entities': 20,
		'destination': [
			'tools',
			'weapon'
		]
	},
	'bone sword': {
		'name': 'Bone Sword',
		'damage': 5,
		'recipe': {
			'bone': 100
		},
		'chances': {
			'zombie': 497,
			'ghost': 1,
			'vampire': 1,
			'blazer': 1
		},
		'entities': 10,
		'destination': [
			'tools',
			'weapon'
		]
	},
	'misty sword': {
		'name': 'Misty Sword',
		'damage': 10,
		'recipe': {
			'mist': 1000
		},
		'chances': {
			'zombie': 1,
			'ghost': 497,
			'vampire': 1,
			'blazer': 1
		},
		'entities': 10,
		'destination': [
			'tools',
			'weapon'
		]
	},	
	'wheat hoe': {
		'name': 'Wheat Hoe',	
		'recipe' : {
			'wheat': 10
		},
		'chances': {
			'wheat': 997,

		}
	}
}
mobs = {
	'zombie': {
		'coins': 250,
		'drops': 'bone'
	},
	'ghost': {
		'coins': 500,
		'drops': 'mist'
	},
	'vampire': {
		'coins': 750,
		'drops': 'fang'
	},
	'blazer': {
		'coins': 1000,
		'drops': 'flamer'
	}
}
crops = {
	'wheat': {
		'coins': 250,
		'drops': 'wheat',
	},
	'corn': {
		'coins': 500,
		'drops': 'corn'
	},
	'watermelon': {
		'coins': 750,
		'drops': 'corn'
	},
	'pumpkin': {
		'coins': 1000,
		'drops': 'pumpkin'
	}
}
woods = {
	'acacia': {
		'coins': 250,
		'drops': 'acacia'
	},
	'birch': {
		'coins': 500,
		'drops': 'birch'
	},
	'oak': {
		'coins': 750,
		'drops': 'oak'
	},
	'spruce': {
		'coins': 1000,
		'drops': 'spruce'
	}
}
bosses = {
	'Mythical Money': {
		'health': 1000000000000000000000000000000,
		'damage': 1000,
		'coins': 50000
	}
}