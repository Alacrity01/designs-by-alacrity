def get_colors_dict():
	colors={
		'black':(0, 0, 0),
		'white':(255, 255, 255),
		'light_gray':(200, 200, 200),
		'medium_gray':(150, 150, 150),
		'dark_gray':(75, 75, 75),
		'micron':(50, 145, 221),
		'lockheed':(0, 62, 105),
		'nasa_jpl':(218, 22, 53),
		'spr':(0, 153, 255),
		'majorkey_green':(32, 245, 147),
		'majorkey_purple':(108, 0, 209),
		'majorkey_deep':(29, 6, 59),
		'night':(10, 3, 40),
		'foam':(235, 235, 235),
		'retina_burn':(40, 30, 30),
		'graylord':(100, 100, 100),
		'royal_blue':(0, 196, 255),
		'deep_space':(25, 0, 48),
		'aqua':(0, 150, 255),
		'brightlight':(240, 240, 255),
		'off_black':(10, 10, 10),
		'shale_gray':(138, 151, 158),
		'scratched_shale':(151, 151, 151),
		'natural_rust':(161, 113, 63),
		'slate':(38, 38, 38),
		'scratched_slate':(64, 64, 64),
		'cyberyellow':(216, 252, 63),
	}
	return colors

def get_themes():
	colors = get_colors_dict()
	themes = {
		'stone_age':[
			colors['slate'],
			colors['scratched_slate'],
			colors['natural_rust']
		],
		'cyberslate':[
			colors['slate'],
			colors['scratched_slate'],
			colors['cyberyellow']
		],
	}
	return themes

