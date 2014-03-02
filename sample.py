from minecraft import minecraft, block

mc = minecraft.Minecraft.create("service1.kingfisher.co")

mc.setBlocks(0,0,0,9,9,9,1)

blocks = mc.getBlocks(0,0,0,9,9,9)

# Prints the array of blocks. There should be 1000 blocks all set to block type 1
print(blocks)
print("Number of blocks: " + str(len(blocks)))
