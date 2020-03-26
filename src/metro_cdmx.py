# Metro CDMX                                                 :noexport:


# Lista de adyacencia
metro_cdmx = {}

# Línea 1 Observatorio - Pantitlán 
metro_cdmx["Observatorio"] = {"Tacubaya"}
metro_cdmx["Tacubaya"] = {"Observatorio", "Juanacatlán", "Patriotismo", "Constituyentes", "Sn. Pedro de los Pinos"}
metro_cdmx["Juanacatlán"] = {"Tacubaya", "Chapultepec"}
metro_cdmx["Chapultepec"] = {"Juanacatlán", "Sevilla"}
metro_cdmx["Sevilla"] = {"Chapultepec", "Insurgentes"}
metro_cdmx["Insurgentes"] = {"Sevilla", "Cuauhtémoc"}
metro_cdmx["Cuauhtémoc"] = {"Insurgentes", "Balderas"}
metro_cdmx["Balderas"] = {"Cuauhtémoc", "Salto del Agua", "Niños Héroes", "Juárez"}
metro_cdmx["Salto del Agua"] = {"Balderas", "Isabel la Católica", "Doctores", "San Juan de Letrán"}
metro_cdmx["Isabel la Católica"] = {"Salto del Agua", "Pino Suárez"}
metro_cdmx["Pino Suárez"] = {"Isabel la Católica", "Merced", "Zócalo", "Chabacano"}
metro_cdmx["Merced"] = {"Pino Suárez", "Candelaria"}
metro_cdmx["Candelaria"] = {"Merced", "San Lázaro", "Fray Servando", "Morelos"}
metro_cdmx["San Lázaro"] = {"Candelaria", "Moctezuma", "Morelos", "Flores Magón"}
metro_cdmx["Moctezuma"] = {"San Lázaro", "Balbuena"}
metro_cdmx["Balbuena"] = {"Moctezuma", "Boulevard Pto. Aéreo"}
metro_cdmx["Boulevard Pto. Aéreo"] = {"Balbuena", "Gómez Farías"}
metro_cdmx["Gómez Farías"] = {"Boulevard Pto. Aéreo", "Zaragoza"}
metro_cdmx["Zaragoza"] = {"Gómez Farías", "Pantitlán"}
metro_cdmx["Pantitlán"] = {"Zaragoza", "Hangares", "Puebla", "Agrícola Oriental"}

# Línea 2 Taxqueña - Cuatro Caminos 
metro_cdmx["Tasqueña"]={"General Anaya"}
metro_cdmx["General Anaya"]={"Ermita","Tasqueña"}
metro_cdmx["Ermita"]={"Portales","General Anaya","Mexicaltzingo","Eje Central"}
metro_cdmx["Portales"]={"Ermita","Nativitas"}
metro_cdmx["Nativitas"]={"Portales","Villa de Cortés"}
metro_cdmx["Villa de Cortés"]={"Nativitas","Xola"}
metro_cdmx["Xola"]={"Villa de Cortés","Viaducto"}
metro_cdmx["Viaducto"]={"Xola","Chabacano"}
metro_cdmx["Chabacano"]={"Viaducto","San Antonio Abad","Jamaica","Lázaro Cárdenas","La Viga","Obrera"} 
metro_cdmx["San Antonio Abad"]={"Chabacano","Pino Suárez"}
metro_cdmx["Pino Suárez"]={"San Antonio Abad","Zócalo","Isabel la Católica","Merced"} 
metro_cdmx["Zócalo"]={"Pino Suárez","Allende"}
metro_cdmx["Allende"]={"Zócalo","Bellas Artes"}
metro_cdmx["Bellas Artes"]={"Allende","Hidalgo","Garibaldi / Lagunilla","San Juan de Letrán"} 
metro_cdmx["Hidalgo"]={"Bellas Artes","Revolución", "Guerrero","Juárez"} 
metro_cdmx["Revolución"]={"Hidalgo","San Cosme"}
metro_cdmx["San Cosme"]={"Revolución","Normal"}
metro_cdmx["Normal"]={"San Cosme","Colegio Militar"}
metro_cdmx["Colegio Militar"]={"Normal","Popotla"}
metro_cdmx["Popotla"]={"Colegio Militar","Cuitláhuac"}
metro_cdmx["Cuitláhuac"]={"Popotla","Tacuba"}
metro_cdmx["Tacuba"]={"Cuitláhuac","Panteones","Refinería","San Joaquín"} 
metro_cdmx["Panteones"]={"Tacuba","Cuatro Caminos"}
metro_cdmx["Cuatro Caminos"]={"Panteones"}

# Línea 3 Universidad - Indios Verdes 
metro_cdmx["Universidad"] = {"Copilco"}
metro_cdmx["Copilco"] = {"Universidad", "Miguel Angel de Quevedo"}
metro_cdmx["Miguel Angel de Quevedo"] = {"Copilco", "Viveros / Derechos Humanos"}
metro_cdmx["Viveros / Derechos Humanos"] = {"Miguel Angel de Quevedo", "Coyoacán"}
metro_cdmx["Coyoacán"] = {"Viveros / Derechos Humanos", "Zapata"}
metro_cdmx["Zapata"] = {"Coyoacán", "División del Norte", "20 de Noviembre", "Parque de los Venados"}
metro_cdmx["División del Norte"] = {"Zapata", "Eugenia"}
metro_cdmx["Eugenia"] = {"División del Norte", "Etiopía / Plaza de la Transparencia"}
metro_cdmx["Etiopía / Plaza de la Transparencia"] = {"Eugenia", "Centro Médico"}
metro_cdmx["Centro Médico"] = {"Etiopía / Plaza de la Transparencia", "Hospital General", "Chilpancingo", "Lázaro Cárdenas"}
metro_cdmx["Hospital General"] = {"Centro Médico", "Niños Héroes"}
metro_cdmx["Niños Héroes"] = {"Hospital General", "Balderas"}
metro_cdmx["Balderas"] = {"Niños Héroes", "Juárez", "Cuauhtémoc", "Salto del Agua"}
metro_cdmx["Juárez"] = {"Balderas", "Hidalgo"}
metro_cdmx["Hidalgo"] = {"Juárez", "Guerrero", "Revolución", "Bellas Artes"}
metro_cdmx["Guerrero"] = {"Hidalgo", "Tlatelolco", "Buenavista", "Garibaldi / Lagunilla"}
metro_cdmx["Tlatelolco"] = {"Guerrero", "La Raza"}
metro_cdmx["La Raza"] = {"Tlatelolco", "Potrero", "Autobuses del Norte", "Misterios"}
metro_cdmx["Potrero"] = {"La Raza", "Deportivo 18 de Marzo"}
metro_cdmx["Deportivo 18 de Marzo"] = {"Potrero", "Indios Verdes", "Lindavista", "La Villa-Basílica"}
metro_cdmx["Indios Verdes"] = {"Deportivo 18 de Marzo"}

#Línea 4 Santa Anita - Martín Carrera
metro_cdmx["Santa Anita"] = {"Jamaica", "Coyuya", "La Viga"}
metro_cdmx["Jamaica"] = {"Santa Anita", "Fray Servando", "Mixiuhca", "Chabacano"}
metro_cdmx["Fray Servando"] = {"Jamaica", "Candelaria"}
metro_cdmx["Candelaria"] = {"Fray Servando", "Morelos", "Merced", "San Lázaro"}
metro_cdmx["Morelos"] = {"Candelaria", "Canal del Norte", "Tepito", "San Lázaro"}
metro_cdmx["Canal del Norte"] = {"Morelos", "Consulado"}
metro_cdmx["Consulado"] = {"Canal del Norte", "Bondojito", "Valle Gómez", "Eduardo Molina"}
metro_cdmx["Bondojito"] = {"Consulado", "Talismán"}
metro_cdmx["Talismán"] = {"Bondojito", "Martín Carrera"}
metro_cdmx["Martín Carrera"] = {"Talismán", "La Villa-Basílica"}

#Línea 5 Politécnico-Pantitlán 
metro_cdmx["Politécnico"]={"Instituto del Petróleo"}
metro_cdmx["Instituto del Petróleo"]={"Politécnico","Autobuses del Norte", "Vallejo", "Lindavista"}
metro_cdmx["Autobuses del Norte"]={"Instituto del Petróleo","La Raza"}
metro_cdmx["La Raza"]={"Autobuses del Norte","Misterios", "Potrero", "Tlatelolco"}
metro_cdmx["Misterios"]={"La Raza","Valle Gómez"}
metro_cdmx["Valle Gómez"]={"Misterios","Consulado"}
metro_cdmx["Consulado"]={"Valle Gómez","Eduardo Molina", "Bondojito", "Canal del Norte"}
metro_cdmx["Eduardo Molina"]={"Consulado","Aragón"}
metro_cdmx["Aragón"]={"Eduardo Molina","Oceanía"}
metro_cdmx["Oceanía"]={"Aragón","Terminal Aérea", "Deportivo Oceanía", "Romero Rubio"}
metro_cdmx["Terminal Aérea"]={"Oceanía","Hangares"}
metro_cdmx["Hangares"]={"Terminal Aérea", "Pantitlán"}
metro_cdmx["Pantitlán"] = {"Zaragoza", "Hangares", "Puebla", "Agrícola Oriental"}

#Linea 6 El Rosario - Martín Carrera
metro_cdmx["El Rosario"] = {"Tezozómoc", "Aquiles Serdán"}
metro_cdmx["Tezozómoc"] = {"El Rosario", "Azcapotzalco"}
metro_cdmx["Azcapotzalco"] = {"Tezozómoc", "Ferrería"}
metro_cdmx["Ferrería"] = {"Azcapotzalco", "Norte 45"}
metro_cdmx["Norte 45"] = {"Ferrería", "Vallejo"}
metro_cdmx["Vallejo"] = {"Norte 45", "Instituto del Petróleo"}
metro_cdmx["Instituto del Petróleo"] = {"Vallejo","Lindavista","Politécnico", "Autobuses del Norte"}
metro_cdmx["Lindavista"] = {"Instituto del Petróleo", "Deportivo 18 de Marzo"}
metro_cdmx["Deportivo 18 de Marzo"] = {"Lindavista", "La Villa-Basílica", "Indios Verdes", "Potrero"}
metro_cdmx["La Villa-Basílica"] = {"Deportivo 18 de Marzo", "Martín Carrera"}
metro_cdmx["Martín Carrera"] = {"La Villa-Basílica", "Talismán"}

# Linea 7 El Rosario - Barranca del muerto
metro_cdmx["El Rosario"] = {"Aquiles Serdán", "Tezozómoc"}
metro_cdmx["Aquiles Serdán"] = {"El Rosario", "Camarones"}
metro_cdmx["Camarones"] = {"Aquiles Serdán", "Refinería"}
metro_cdmx["Refinería"] = {"Camarones", "Tacuba"}
metro_cdmx["Tacuba"] = {"Refinería","San Joaquín","Panteones", "Cuitláhuac"}
metro_cdmx["San Joaquín"] ={"Tacuba","Polanco"}
metro_cdmx["Polanco"] ={"San Joaquín","Auditorio"}
metro_cdmx["Auditorio"] ={"Polanco","Constituyentes"}
metro_cdmx["Constituyentes"] ={"Auditorio","Tacubaya"}
metro_cdmx["Tacubaya"] ={"Constituyentes","Sn. Pedro de los Pinos", "Observatorio", "Patriotismo", "Juanacatlán"}
metro_cdmx["Sn. Pedro de los Pinos"] ={"Tacubaya","Sn. Antonio"}
metro_cdmx["Sn. Antonio"] ={"Sn. Pedro de los Pinos","Mixcoac"}
metro_cdmx["Mixcoac"] ={"Sn. Antonio","Barranca del Muerto","Insurgentes Sur"}
metro_cdmx["Barranca del Muerto"] ={"Mixcoac"}

# Linea 8 Garibaldi-Constitución de 1917
metro_cdmx["Garibaldi / Lagunilla"] = {"Lagunilla", "Guerrero", "Bellas Artes"}
metro_cdmx["Bellas Artes"]={"Allende","Hidalgo","Garibaldi / Lagunilla","San Juan de Letrán"} 
metro_cdmx["San Juan de Letrán"] = {"Bellas Artes", "Salto del Agua"}
metro_cdmx["Salto del Agua"] = {"Balderas", "San Juan de Letrán", "Isabel la Católica", "Doctores"}
metro_cdmx["Doctores"] = {"Salto del Agua", "Obrera"}
metro_cdmx["Obrera"] = {"Doctores", "Chabacano"}
metro_cdmx["Chabacano"] = {"Obrera", "´Lázaro Cárdenas", "Viaducto", "La Viga", "Jamaica", "San Antonio de Abad"}
metro_cdmx["La Viga"] = {"Chabacano", "Santa Anita"}
metro_cdmx["Santa Anita"] = {"La Viga", "Jamaica", "Coyuya"}
metro_cdmx["Coyuya"] = {"Santa Anita", "Iztacalco"}
metro_cdmx["Iztacalco"] = {"Coyuya", "Apatlaco"}
metro_cdmx["Apatlaco"] = {"Iztacalco", "Aculco"}
metro_cdmx["Aculco"] = {"Apatlaco", "Escuadrón 201"}
metro_cdmx["Escuadrón 201"] = {"Aculco", "Atlalilco"}
metro_cdmx["Atlalilco"] = {"Iztapalapa", "Escuadrón 201", "Mexicaltzingo", "Pueblo Culhuacán"}
metro_cdmx["Iztapalapa"] = {"Atlalilco", "C. de la Estrella"}
metro_cdmx["C. de la Estrella"] = {"Iztapalapa", "U.A.M. I"}
metro_cdmx["U.A.M. I"] = {"C. de la Estrella", "Const. de 1917"}
metro_cdmx["Const. de 1917"] = {"U.A.M. I"}

# Línea 9 Pantitlán - Tacubaya
metro_cdmx["Tacubaya"] ={"Constituyentes","Sn. Pedro de los Pinos", "Observatorio", "Patriotismo", "Juanacatlán"}
metro_cdmx["Patriotismo"] = {"Tacubaya","Chilpancingo"}
metro_cdmx["Chilpancingo"] = {"Patriotismo", "Centro Médico"}
metro_cdmx["Centro Médico"] = {"Etiopía / Plaza de la Transparencia", "Hospital General", "Chilpancingo", "Lázaro Cárdenas"}
metro_cdmx["Lázaro Cárdenas"] = {"Centro Médico", "Chabacano"}
metro_cdmx["Chabacano"]={"Viaducto","San Antonio Abad","Jamaica","Lázaro Cárdenas","La Viga","Obrera"} 
metro_cdmx["Jamaica"] = {"Santa Anita", "Fray Servando", "Mixiuhca", "Chabacano"}
metro_cdmx["Mixiuhca"] = {"Jamaica", "Velódromo"}
metro_cdmx["Velódromo"] = {"Mixiuhca", "Ciudad Deportiva"}
metro_cdmx["Ciudad Deportiva"] = {"Velódromo", "Puebla"} 
metro_cdmx["Puebla"] = {"Pantitlán", "Ciudad Deportiva"}
metro_cdmx["Pantitlán"] = {"Zaragoza", "Hangares", "Puebla", "Agrícola Oriental"}

# Linea A Pantitlán-Los Reyes
metro_cdmx["Pantitlán"] = {"Hangares", "Zaragoza", "Puebla", "Agrícola Oriental"}
metro_cdmx["Agrícola Oriental"] = {"Pantitlán", "Canal de San Juan"}
metro_cdmx["Canal de San Juan"] = {"Agrícola Oriental", "Tepalcates"}
metro_cdmx["Tepalcates"] = {"Canal de San Juan", "Guelatao"}
metro_cdmx["Guelatao"] = {"Tepalcates", "Peñón Viejo"}
metro_cdmx["Peñón Viejo"] = {"Guelatao", "Acatitla"}
metro_cdmx["Acatitla"] = {"Peñón Viejo", "Santa Marta"}
metro_cdmx["Santa Marta"] = {"Acatitla", "Los Reyes"}
metro_cdmx["Los Reyes"] = {"Santa Marta", "La Paz"}
metro_cdmx["La Paz"] = {"Los Reyes"}


# Línea B Ciudad Azteca - Buenavista
metro_cdmx["Ciudad Azteca"] = {"Plaza Aragón"}
metro_cdmx["Plaza Aragón"] = {"Ciudad Azteca", "Olímpica"}
metro_cdmx["Olímpica"] = {"Plaza Aragón", "Ecatepec"}
metro_cdmx["Ecatepec"] = {"Olímpica", "Múzquiz"}
metro_cdmx["Múzquiz"] = {"Ecatepec", "Río de los Remedios"}
metro_cdmx["Río de los Remedios"] = {"Múzquiz", "Impulsora"}
metro_cdmx["Impulsora"] = {"Río de los Remedios", "Nezahualcóyotl"}
metro_cdmx["Nezahualcóyotl"] = {"Impulsora", "Villa de Aragón"}
metro_cdmx["Villa de Aragón"] = {"Nezahualcóyotl", "Bosque de Aragón"}
metro_cdmx["Bosque de Aragón"] = {"Villa de Aragón", "Deportivo Oceanía"}
metro_cdmx["Deportivo Oceanía"] = {"Bosque de Aragón", "Oceanía"}
metro_cdmx["Oceanía"] = {"Deportivo Oceanía", "Romero Rubio", "Aragón", "Terminal Aérea"}
metro_cdmx["Romero Rubio"] = {"Oceanía", "Flores Magón"}
metro_cdmx["Flores Magón"] = {"Romero Rubio", "San Lázaro"}
metro_cdmx["San Lázaro"] = {"Flores Magón", "Morelos", "Candelaria", "Moctezuma"} 
metro_cdmx["Morelos"] = {"San Lázaro", "Tepito", "Canal del Norte", "Candelaria"} 
metro_cdmx["Tepito"] = {"Morelos", "Lagunilla"}
metro_cdmx["Lagunilla"] = {"Tepito", "Garibaldi / Lagunilla"} 
metro_cdmx["Garibaldi / Lagunilla"] = {"Lagunilla", "Guerrero", "Bellas Artes"} 
metro_cdmx["Guerrero"] = {"Garibaldi / Lagunilla", "Buenavista", "Tlatelolco", "Hidalgo"}
metro_cdmx["Buenavista"] = {"Guerrero"}

# Línea 12 Mixcoac - Tláhuac
metro_cdmx["Mixcoac"] = {"Insurgentes Sur", "Barranca del Muerto", "Sn. Antonio"} 
metro_cdmx["Insurgentes Sur"] = {"Mixcoac","20 de Noviembre"}
metro_cdmx["20 de Noviembre"] = {"Insurgentes Sur", "Zapata"}
metro_cdmx["Zapata"] = {"20 de Noviembre", "Parque de los Venados", "División del Norte", "Coyoacán"}
metro_cdmx["Parque de los Venados"] = {"Zapata", "Eje Central"}
metro_cdmx["Eje Central"] = {"Parque de los Venados", "Ermita"}
metro_cdmx["Ermita"] = {"Eje Central", "Mexicaltzingo", "Portales", "General Anaya"} 
metro_cdmx["Mexicaltzingo"] = {"Ermita", "Atlalilco"}
metro_cdmx["Atlalilco"] = {"Mexicaltzingo", "Pueblo Culhuacán", "Escuadrón 201", "Iztapalapa"} 
metro_cdmx["Pueblo Culhuacán"] = {"Atlalilco", "ESIME Culhuacán"}
metro_cdmx["ESIME Culhuacán"] = {"Pueblo Culhuacán", "Tomatlán"}
metro_cdmx["Tomatlán"] = {"ESIME Culhuacán", "Calle 11"}
metro_cdmx["Calle 11"] = {"Tomatlán", "Periférico Ote."}
metro_cdmx["Periférico Ote."] = {"Calle 11", "Tezonco"}
metro_cdmx["Tezonco"] = {"Periférico Ote.", "Olivos"}
metro_cdmx["Olivos"] = {"Tezonco", "Nopalera"}
metro_cdmx["Nopalera"] = {"Olivos", "Zapotitlán"}
metro_cdmx["Zapotitlán"] = {"Nopalera", "Tlaltenco"}
metro_cdmx["Tlaltenco"] = {"Zapotitlán", "Tláhuac"}
metro_cdmx["Tláhuac"] = {"Tlaltenco"}
