import os
import discord
import functions
import config


###Frontend Bot

bob = False
verified = False
verified2 = False
tables = []
columns = []
user = ""
ip = ""
password = ""
database = ""

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        # La siguiente sentencia es para definir presencia del bot
        await client.change_presence(activity=discord.Game(name=" Creating a bot.. "))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_message(self, message):
        global bob, r, ii, verified, verified2, ip, user, password, database
        if message.author == self.user:
            return

        if message.content.startswith('!help'):
            ##Desarollar/configurar un embed
            embed = discord.Embed(title="Configuración bot CK's ", description="CK system config", colour=0x6A008C)
            embed.set_author(name="Big_Lolo#8178", url="https://github.com/Big-Lolo",
                             icon_url="https://avatars.githubusercontent.com/u/95545807?v=4")
            ##embed.set_footer(text="Call me back please")
            embed.set_image(
                url="https://ze-robot.com/images/source/839.jpg")
            ##texts / fields
            embed.add_field(name="!start ➔ Conección Base de Datos SQL",
                            value="Para conectar la base de datos debes usar el comando "
                                  "!start [ip] [user] [contraseña] [database]", inline=False)

            embed.add_field(name="!add ➔ Asignación tablas | columnas", value="Para añadir las tablas y columnas donde se "
                        "encontrará el identificador usa el comando: !add [nombre_tabla] [nombre_columna]",inline=False)

            embed.add_field(name="!del ➔ Borrar tablas | columnas", value="Para borrar las tablas y columnas añadidas "
                            "con el comando ! add, usa el comando: !del", inline=False)

            embed.add_field(name="!save ➔ Guardado de Datos", value="Guarda los datos introducidos con los comandos "
                            "!start y !add para no tener que volver a escribirlos. Usa el comando !save", inline=False)

            embed.add_field(name="!unsave ➔ Borrado de datos ", value="Para borrar todos los datos guardados sobre la "
                            "base de datos, usa el comando !unsave ", inline=False)

            embed.add_field(name=" !CK ➔ Character Kill", value="Para borrar el personaje de un usuario, usa el "
                            "comando !CK [identificador(steam o rockstar)]", inline=False)

            embed.set_footer(
                text="Nota!: Cualquier error que pueda ocurrir, puede notificarlo al desarollador clicando sobre el "
                     "nombre que aparece al principio de este embed.", icon_url="")

            await message.channel.send(embed=embed)

        if message.content.startswith("!start"):
            await message.channel.send("Conectando...")
            x = message.content.split(" ", 4)[1:]
            if x[2] == "-":
                x[2] = None
            functions.connect(x[0], x[1], x[2], x[3])
            if not functions.connect(x[0], x[1], x[2], x[3]):
                embed2 = discord.Embed(title="Connection", description="CONEXIÓN FALLIDA", colour=0xFF0000)
                await message.channel.send(embed=embed2)
            else:
                embed3 = discord.Embed(title="Connection", description="Conexión realizada con éxito", colour=0x00B236)
                await message.channel.send(embed=embed3)
                verified = True
                ip = x[0]
                user = x[1]
                password = x[2]
                database = x[3]

        if message.content.startswith("!add"):
            y = message.content.split(" ", 2)[1:]
            tables.append(y[0])
            columns.append(y[1])
            print(tables)
            print(columns)
            embed01 = discord.Embed(title="Realizado!", description="Se han agregado correctamente las tablas| columnas"
            , colour=0x00B236)
            await message.channel.send(embed=embed01)
            verified2 = True

        if message.content.startswith("!del"):
            tables.clear()
            columns.clear()
            embed02 = discord.Embed(title="Realizado!", description="Se han borrado correctamente las tablas| columnas"
            , colour=0x00B236)
            await message.channel.send(embed=embed02)

        if message.content.startswith("!show"):
            if columns == []:
                embed03 = discord.Embed(title="Mostrando...",description="Las tablas y columnas estan vacias"
                , colour=0x00B236)
                await message.channel.send(embed=embed03)
            else:
                for ii in range(len(columns)):
                    await message.channel.send(f"Tabla: {tables[ii]}, Columna: {columns[ii]}")

        ##Eliminar usuario
        if message.content.startswith("!CK"):
            if functions.savedatas() != False:
                dats = functions.savedatas()
                tabs = dats[0]
                cols = dats[1]
                ipp = dats[2]
                userr = dats[3]
                passwordd = dats[4]
                databasee = dats[5]
                card = message.content.split(" ", 1)[1:]
                steam = card[0]
                print(steam)
                functions.deluser(tabs, cols, steam, ipp, userr, passwordd, databasee)
                embed12 = discord.Embed(title="!CK REALIZADO!", description="Se ha realizado correctamente el CK.",
                                        colour=0x00B236)
                embed12.set_footer(text="Credenciales obtenidas de datos guardados anteriormente.")
                await message.channel.send(embed=embed12)
            else:
                if verified:
                    if verified2:
                        card = message.content.split(" ", 1)[1:]
                        steam = card[0]
                        print(steam)
                        functions.deluser(tables, columns, steam, ip, user, password, database)
                        embed11 = discord.Embed(title="!CK REALIZADO!", description="Se ha realizado correctamente el CK"
                                                ,colour=0x00B236)
                        embed11.set_footer(text="Credenciales aun no guardadas. Usa !save para guardar las credenciales")
                        await message.channel.send(embed=embed11)
                    else:
                        embed9 = discord.Embed(title="NO TABS/COLS",description="No has definido las tablas / columnas. "
                        "Usa !help para obtener más info", colour=0xFF0000)
                        await message.channel.send(embed=embed9)
                else:
                    embed10 = discord.Embed(title="No Conection", description="No has configurado la conección. Usa !help "
                    "para obtener más info", colour=0xFF0000)
                    await message.channel.send(embed=embed10)


        if message.content.startswith("!save"):
            if verified and verified2:
                f = open("config_database.py", "w")
                credenciales = [tables, columns, ip, user, password, database]
                f.write(f"dats = {credenciales}")
                f.close()
                embed13 = discord.Embed(title="Guardado", description="Las credenciales, tablas y columnas han sido "
                "guardadas correctamente", colour=0x00B236)
                await message.channel.send(embed=embed13)

        if message.content.startswith("!unsave"):
            if functions.savedatas() == False:
                embed13 = discord.Embed(title="Ups!!", description="No hay nada guardado aún")
                await message.channel.send(embed=embed13)
            else:
                f = open("config_database.py", "w")
                f.write(f"dats = [] ")
                embed14 = discord.Embed(title="Borrando..", description="Se han borrado todos los datos guardados",
                                        colour=0x00B236)
                await message.channel.send(embed=embed14)






client = MyClient()
client.run(config.token)
