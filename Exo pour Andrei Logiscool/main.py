from chararcter_class import thing

# Create a thing
mon_ID = 1
mon_nom = "thing1"
mes_voisins = [1,2,3,4,5,6,7]
ma_couleur = "red"

my_thing1 = thing(mon_ID,mon_nom,mes_voisins,ma_couleur); #Create a thing
my_thing1.presented_itself();

my_thing1.write_to_file("test.txt","w")
my_thing1.write_to_file("test.txt","a")
