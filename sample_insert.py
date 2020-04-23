import psycopg2

postgres_insert_query = """ INSERT INTO public.people_record (amount, datetime) VALUES (%s,%s)"""
record_to_insert = (2, "21/04/2020 22:55")

try:
    connection = psycopg2.connect(user = "",
                                  password = "",
                                  host = "",
                                  port = "",
                                  database = "")

    cursor = connection.cursor()
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    print("Data sent successfully")

except (Exception, psycopg2.Error) as error :
    print ("Connection fails", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Connection closed")