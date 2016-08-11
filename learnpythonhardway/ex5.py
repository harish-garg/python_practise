name  = "John Hancock"
age = 33 # years
height = 72 # inches
weight = 130 # pounds
eyes = 'Orange'
teeth = 'Green'
hair = 'Blue'


print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

height_cm = height * 2.54
weight_kg = weight * 0.45
print "Height in cms is %d." % height_cm
print "Weight in kgs is %d." % weight_kg
