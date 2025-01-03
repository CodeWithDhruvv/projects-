
print("MSSSSSSSMSSSSMMMSSMMMPTMM;-/MMM^     MMMSSMMMSSMM")
print("SSSSSSSMMSSMMMMMMMMMP-.MMM :  ;.;P       dMMMMMMMMMP")
print("SSMSSSMMMSMMMMMMMMMP   :M;`:  ;.+t+dMMMMMMMMMMP")   
print("MMMSSMMMMMMMMPTMMMM:P ./       ^^MMMMMMMP")    
print("MMMMMMPTMMMMP=TMMMsg,         db`c  dMMMMMP")      
print("MMMMMM  TMMM   d$$$b ^          /T$; ;-/TMMMP  ")       
print("MMMMM; .^`M; d$P^T$$b          :  $$ ::  T       ")   
print("MMMMMM   .-+d$$   $$$;         ; d$$ ;;  __        ")   
print("MMMMMMb   _d$$$   $$$$         :$$$; :MmMMMMp.       ") 
print("MMMMMM"  " T$$$._.$$$;          T$P. MMMSSSSSSb.      ")
print("MMM`TMb   -T$$$$$$P       `._   :MMSSSMMP       ")
print("MMM /       T$$P           /     :MMMMMMM     ")    
print("MMSb. ;                            :MMMMMMM       ")  
print("MMSSb_lSSSb.       `.   .___.       MMMMMMMM         ")
print("MMMMSSSSSSSSb.                     .MMMMMMMMM         ")
print("MMMMMMMMMMMSSSb                  .dMMMMMMMMM'         ")
print("MMMMMMMMMMMMMSS;               .dMMMMMMMMMMP          ")
print("MMMMMMMMMMMMMb`;-.          .dMMMMMMMMMMP'           ")
print("MMMMMMMMMMMMMMb    --.___.dMMMMMMMMMP^      ")

print ("Welcome to Treasure Island")
print ("your mission is to find the treasure")
input1 = input("you are on a cross road, where do you want to go?, type right or left\t")
input1.lower()

if input1 == "right":
    print ("dead end!, Game Over")

else:
    input_2 = input("do yo want to swim or wait for a boat\t")
    input_2.lower()
    if input_2 == "swim":
        print("Shark ate you, Game Over")

    else:
        print ("youve reached the island using a boat")

        input_3 = input ("what door you want to go in Red, Blue or Yellow\t")
        input_3.lower()
        if input_3 == "red":
            print("you were killed by spikes")
        elif input_3 == "blue":
            print (" not this door either, life is unfair")
        elif input_3 == "yellow":
            print ("YOU WIN")