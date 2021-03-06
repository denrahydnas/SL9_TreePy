# Step 1:
# Make two strings, each should be 8 characters long, made up of Xs and Os.
# First string should start with X, second string should start with O.
# Both strings should alternate between the two characters.
# You can use multiplication for this.

string1 = "xo"*4
string2 = "ox"*4


# Step 2:
# Make a list
# Add 1 of the X-started strings.
# Add 1 of the O-started strings.
# Repeat until you have 8 items total in the list.
# You can use multiplication for this, too.

xoxo = [string1, string2] *4

# Step 3:
# Print out the list of strings, joined with newlines \n.

print('\n'.join(xoxo))