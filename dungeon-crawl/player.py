class player:

	def __init__(self, name, max_health):

		# General
		self.name = name


		# Health Bar Related
		health_bar = health_bar(max_health, max_health)


		# inventory (Gold included in inventory)
		# level (Should EXP be seperate)

		# Equiped (Weapons, armor, or anything else specifically equiped and not inside your inventory)... This could be a seperate model
		# ATK level
		# Armor level


	# This will keep track off the current items that the player has equiped.
	equipped = {
		"main_hand": None,
		"off_hand": None,
		"helment": None,
		"chest": None,
		"hands": None,
		"pants": None,
		"shoes": None
	}


class health_bar:

	def __init__(self, max_health, current_health):
		self.current_health = current_health
		self.max_health = max_health


	def removeHealth(damage):
		self.current_health = damage
		exhaustPlayer()

	def exhaustPlayer():
		if current_health <= 0:
			return True
		else:
			return False