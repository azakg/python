from TV import TV

def main():

    tv1 = TV()
    print(tv1.getOnStatus())
    tv1.turnOn()
    print(tv1.getOnStatus())
    print(tv1.getChannel())
    tv1.setChannel(115)
    print(tv1.channel)

main()
