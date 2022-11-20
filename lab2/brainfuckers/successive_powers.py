powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
primes = [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]

# Opiszę to zadanie, ponieważ wydaje mi się, iż rozwiązanie jest nietypowe.
# Cryptohack hintował, aby użyć kartki i długopisu, więc pewnie istnieje jakieś szybkie i proste rozwiązanie wynikające z łatwo zauważalnej zależności
# Ja za to zdecydowałem się na brute force, który wiem, że jestem zrobić w czasie skończonym

# Zadanie byłoby zbyt proste gdyby wiadomo było że te 12 potęg to pierwsze 12 potęg, a nie losowo wybrane 12

# Szukamy liczby pierwszej i liczby x
def foo():
    # iteracja po liczbach pierwszych https://gist.github.com/cblanc/46ebbba6f42f61e60666
    for prime in primes:
        print(f"Prime: {prime}")
        # Teraz próbuje zgadnąć liczbę x (zakładam, ze jest ona większa niż 100 i najpierw sprawdzałem tylko do 1000 (akurat się udało :D))
        for x in range(100,1000):
            k = 0 # licznik ile juz bylo poteg w ciagu (max.12)
            for i in range(1,100):
                power = pow(x,i,prime) # obliczenie potęg: x^i % prime
                if (power == powers[k]): k+=1   # naliczam ile już potęg z rzędu zgadza się z potęgami w liście `powers`
                else: k=0                       # jak ciąg się przerwie (lub wgl nawet nie rozpocznie) no to licznik k=0
                if k == 12:             # Jak 12 wyliczonych przeze mnie potęg zgodzi się z listą `powers` no to "mamy to"
                    print("Mamy to")
                    odp = (prime, x)
                    return odp
print(foo())
