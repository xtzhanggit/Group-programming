import pydb
import time

sql_popu = "select population_density from attributes where group_name = '"  + "G_001" + "'"
sql_birth = "select online_number from attributes where group_name = '" + "G_001" + "'"
sql_death = "select offline_number from attributes where group_name = '" + "G_001" + "'"

if __name__ == "__main__":
    while True:
        popu1 = pydb.db_get(sql_popu, "Group_data")[0][0]
        bir1 = pydb.db_get(sql_birth, "Group_data")[0][0]
        dea1 = pydb.db_get(sql_death, "Group_data")[0][0]
        
        time.sleep(600) 
        popu2 = pydb.db_get(sql_popu, "Group_data")[0][0]
        
        time.sleep(600) 
        popu3 = pydb.db_get(sql_popu, "Group_data")[0][0]

        time.sleep(600) 
        popu4 = pydb.db_get(sql_popu, "Group_data")[0][0]

        time.sleep(600) 
        popu5 = pydb.db_get(sql_popu, "Group_data")[0][0]

        time.sleep(600)
        popu6 = pydb.db_get(sql_popu, "Group_data")[0][0]
        bir2 = pydb.db_get(sql_birth, "Group_data")[0][0]
        dea2 = pydb.db_get(sql_death, "Group_data")[0][0]
        
        average_popu = (popu1 + popu2 + popu3 + popu4 + popu5 + popu6)/6
        birthrate = (bir2 - bir1) / average_popu
        deathrate = (dea2 - dea1) / average_popu

        sql_update = "update attributes set birth_rate = " + str(birthrate) + ", death_rate = " + str(deathrate) + " where group_name = '" + "G_001" + "'"
        pydb.db_exe(sql_update, "Group_data")
