print("""
            ___
           /]_/
          |\/|.--/'-.
          \|/:o /  /\    ._,
             \_/_.'0/    _|_
              \____]] (>[___]=]]]===
              /    \___/P{]
           __//    /----\/
          (_[-'\__/_
              / | | \
             '=='='=='
            ____||||___
           (_""_/ \_""_)
""")

print("Bienvenido a la aventura galactica!")

start = input("¿Quieres jugar? (S/N)\n===> ")
if start == 's' or start == 'S':
    print("\nEmpecemos!")
    print("\nTe encuentras en una nave espacial, a punto de despegar y tu objetivo es investigar un nuevo planeta.")
    print("\nSe ha realizado con exito el despege y estas cerca de llegar al planeta pero de pronto la nave se destabiliza, y no hay manera de poder estacionar la nave. Intentas estabilizarlo y en ese mismo momento impactas sobre el planeta.\nTe despiertas y te das cuenta que has sobrevivido al impacto.")
    print("\nTienes la posibilidad de salir de la nave (escribe 'salir' si deseas hacerlo), también puedes quedarte dentro de ella, intentar arreglar el comando y contactar con la central (escribe 'quedarme' si deseas hacerlo.)")
    action = input("\n¿Que deseas hacer?\n===> ")
    if action == "salir":
        print("\nHas decidido salir de la nave, entonces a lo lejos visualizas unas siluetas que estan moviendose hacía donde te encuentras. Puedes acercarte a ellos ('acercarte'), o también puedes esconderte detras de unas rocas y observarlos ('observar').")
        action = input("\n¿Que deseas hacer?\n===> ")
        if action == "observar":
            print("\nDecides esconderte detras de unas rocas y observarlos, entonces te das cuenta que son criaturas enormes, derriban la puerta de tu nave y empiezan a robarse cosas, parecen criaturas violentas. Puedes ir a explorar el planeta ('explorar'), también puedes acercarte a dialogar con ellos ('dialogar'), sino también puedes atacarlos ('atacar').")
            action = input("\n¿Que deseas hacer?\n===> ")
            if action == 'explorar':
                print("\nDecides ir a explorar, entonces a lo lejos visualizas una civilización, sin darte cuenta te encuentras con criaturas desconocidas, pero te das cuenta que son diferentes a las que viste anteriormente. Estas intentan comunicarse contigo pero no logran hacerlo, luego te toman y te llevan a su hogar. Aquí te das cuenta que son criaturas con un gran avance tecnologico, ellos podrían ser capaces de arreglar tu nave y parecen amistosos. Puedes guiarlos a tu nave para que lo arreglen ('guiar'), también puedes robar sus cosas y tratar de arreglarlo solo ('robar'), o no hacer nada y quedarte con ellos para siempre ('quedarte').")
                action = input("\n¿Que deseas hacer?\n===> ")
                if action == 'guiar':
                    print("\nHas decidido guiarlos hacía tu nave, ellos te siguen y por suerte llegan al lugar, cuando ven tu nave lo entienden inmediatamente entonces se ponen mano a la obra. A las pocas horas pudieron lograr arreglarlo, te puedes comunicar con la central y decides volver, aunque antes de eso le das las gracias y le otorgas una bolsa de papas fritas de ofrenda. Todo ha salido genial y pudiste volver sano y salvo, ahora esta sera una anecdota que podras contar a tus amigos e hijos.")
                    print("\nHAS GANADO!")
                    exit()
                elif action == 'robar':
                    print("\nHas decidido robar sus cosas para poder ir arreglar solo la nave, pero cuando estas haciendolo uno de ellos se percata de lo que estas haciendo, ahora le desagradas, entonces te atacan y te llevan prisionero. Creo que has tomado una mala decisión.")
                    print("\nHAS PERDIDO")
                    exit()
                else: 
                    print("\nHas decidido quedarte, pues aunque no entiendas su idioma ellos te tratan bien, aunque la comida no es tan buena y parece todo perfecto dentro de un tiempo se origina una guerra con la otra especie que viste al principio. Ellos son una especie muy violenta y en todo eso se destruye todo.")
                    print("\nHAS PERDIDO")
                    exit()
            elif action == 'dialogar':
                print("\nTe acercas a dialogar con esas criaturas pero ellos no te entienden, por lo cuál te atacan y te llevan prisionero.")
                print("\nHAS PERDIDO!")
                exit()
            else:
                print("\nHas decidido atacar pero esas criaturas te doblan el tamaño y estan armados, creo que fue una mala decision, te terminan atacando y te llevan prisionero.")
                print("\nHAS PERDIDO!")
                exit()
        else:
            print("\nDecides acercarte a ellos, pero cuando te ven te atacan y te llevan prisionero.")
            print("\nHAS PERDIDO!")
            exit()
    else:
        print("\nDecides quedarte en la nave, intentar arreglar las cosas pero mientras estas tranquilo entonces escuchas unos ruidos afuera, al instante rompen la puerta y te encuentras con especies desconocidas y estas te llevan prisionero.")
        print("\nHAS PERDIDO!")
        exit()
else:
    print("\nHA FINALIZADO EL JUEGO!")
    exit()