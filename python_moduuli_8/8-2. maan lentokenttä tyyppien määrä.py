import mysql.connector


def lentokenttahakija(yhteys, iso_country, type):
    sql = f"SELECT COUNT(type) FROM airport WHERE iso_country = '{iso_country}' AND type = '{type}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return kursori.fetchone()[0]


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='a1234xd',
         autocommit=True
         )

iso_country = input("Anna maa-koodi : ")
type_varasto = ('balloonport', 'seaplane_base', 'heliport', 'small_airport',
                'medium_airport', 'large_airport', 'closed')
type_varasto_s = ('kuumailmapallokenttiä', 'lentosatamia', 'helikopterikenttiä', 'pieniä lentokenttiä',
                  'keskikokoisia lentokenttiä', 'suuria lentokenttiä', 'suljettuja lentokenttiä')


for tyyppi in range(len(type_varasto)):
    tulos = lentokenttahakija(yhteys, iso_country, type_varasto[tyyppi])
    if tulos > 0:
        print(f'{type_varasto_s[tyyppi]} on: {tulos}')
