# -*- coding: utf-8 -*-s
from dictionary import *
import string
import re

def Assignment_hashtag():
    "" "main function that returns the appropiate hashtag of the post, receives the post as parameter." ""
    post_clean = standardization(post)
    hastag_assigned =  verification_hastag(post_clean)
    #learn(evaluation(post_clean), verification_hastag(post_clean),ideas_hashtea)
    return hastag_assigned
def standardization(post):
 "" " function that receives the post, deletes unnecesary data and returns a word list (nouns, adjectives, etc)."""
    post = post.lower()
    post = string.replace(post,"."," ")
    post = string.replace(post,","," ")
    post = string.replace(post,"(","")
    post = string.replace(post,")","")
    post = string.replace(post,"]","")
    post = string.replace(post,"[","")
    post = string.replace(post,":","")
    post = string.replace(post,";","")
    post = string.replace(post,"0","")
    post = string.replace(post,"1","")
    post = string.replace(post,"2","")
    post = string.replace(post,"3","")
    post = string.replace(post,"4","")
    post = string.replace(post,"5","")
    post = string.replace(post,"6","")
    post = string.replace(post,"7","")
    post = string.replace(post,"8","")
    post = string.replace(post,"9","")
    post = string.replace(post,"@","")
    post = string.replace(post,"!","")
    post = string.replace(post,"¡","")
    post = string.replace(post,"¿","")
    post = string.replace(post,"?","")
    post = string.replace(post,"á","a")
    post = string.replace(post,"é","e")
    post = string.replace(post,"í","i")
    post = string.replace(post,"ó","o")
    post = string.replace(post,"ú","u")
    post = string.replace(post,"Ñ","N")
    post = string.replace(post,"ñ","n")
    post = string.replace(post,"alla ","")
    post = string.replace(post,"ante","")
    post = string.replace(post,"bajo","")
    post = string.replace(post,"cabe","")
    post = string.replace(post,"con nosotros","")
    post = string.replace(post,"contra","")
    post = string.replace(post,"de acuerdo","")
    post = string.replace(post,"desde","")
    post = string.replace(post,"en cuestion","")
    post = string.replace(post,"entre","")
    post = string.replace(post,"hacia","")
    post = string.replace(post,"hasta","")
    post = string.replace(post,"para","")
    post = string.replace(post,"por","")
    post = string.replace(post,"segun","")
    post = string.replace(post,"sea","")
    post = string.replace(post,"sin ","")
    post = string.replace(post,"son","")
    post = string.replace(post,"sobre","")
    post = string.replace(post,"tras","")
    post = string.replace(post,"durante","")
    post = string.replace(post,"mediante","")
    post = string.replace(post,"excepto","")
    post = string.replace(post,"salvo","")
    post = string.replace(post,"incluso","")
    post = string.replace(post,"mas o menos","")
    post = string.replace(post,"acerca de","")
    post = string.replace(post,"arreglo","")
    post = string.replace(post,"al rededor","")
    post = string.replace(post,"lado","")
    post = string.replace(post,"de lado","")
    post = string.replace(post,"alrededor","")
    post = string.replace(post,"antes","")
    post = string.replace(post,"pesar","")
    post = string.replace(post,"cerca","")
    post = string.replace(post,"objeto","")
    post = string.replace(post,"debajo","")
    post = string.replace(post,"delante","")
    post = string.replace(post,"cuanto","")
    post = string.replace(post,"enfrente","")
    post = string.replace(post,"virtud","")
    post = string.replace(post,"frente","")
    post = string.replace(post,"fuera","")
    post = string.replace(post,"junto","")
    post = string.replace(post,"lejos","")
    post = string.replace(post,"culpa","")
    post = string.replace(post,"encima","")
    post = string.replace(post,"gracias","")
    post = string.replace(post,"nosotros","")
    post = string.replace(post,"ellos","")
    post_clear = []
    post_clear.append(post.split(" "))

    return post_clear
def learn(words, hashting, idea_hasteada):
	""" 
    function that receives repeated words from the post, the assigned hashtag, 
    and the posts saved into the database with the same hashtag. Modifies the dictionary module.
    """
    counter = 0
    if hashting == "#gestion":
        for x in words:
            for q in xrange(0,len(idea_hasteada)):
                if (x in idea_hasteada[q]):
                        counter +=1
            if counter > 1:
                gestion.append(x)

    if hashting == "#movilidad":
        for x in words:
            for q in xrange(0,len(idea_hasteada)):
                if (x in idea_hasteada[q]):
                        counter +=1
            if counter > 1:
                movilidad.append(x)

    if hashting == "#basurero":
        for x in words:
            for q in xrange(0,len(idea_hasteada)):
                if (x in idea_hasteada[q]):
                        counter +=1
            if counter > 1:
                basurero.append(x)

    if hashting == "#mercado":
        for x in words:
            for q in xrange(0,len(idea_hasteada)):
                if (x in idea_hasteada[q]):
                        counter +=1
            if counter > 1:
                print counter

    if hashting == "#resilencia":
        for x in words:
            for q in xrange(0,len(idea_hasteada)):
                if (x in idea_hasteada[q]):
                        counter +=1
            if counter > 1:
                resilencia.append(x)

    if hashting == "#infraestructura":
        for x in words:
            for q in xrange(0,len(idea_hasteada)):
                if (x in idea_hasteada[q]):
                        counter +=1
            if counter > 1:
                infraestructura.append(x)

def evaluation(post):
    "" "Function that receives the normalized post and searches for repeated words, returns a list of said things." ""
    repeated = []
    only = []
    for x in post[0]:
        if x not in only:
            only.append(x)
        else:
            """palabras repetidas, no necesariamente relacion al hashtag"""
            """repeated words, not necessarily related to the hashtag."""
            if x not in repeated:
                repeated.append(x)

    return repeated
def verification_hastag(post):
    "" "function that receives the normalized post and returns the appropiate hashtag." ""
    list_counter = []
    counter_gestion = 0
    counter_movilidad= 0
    counter_basurero = 0
    counter_resilencia = 0
    counter_infraestructura= 0
    counter_mercado= 0
    lon = len(post[0])
    for i in xrange(0,lon):
        index = 0
        for x in gestion:
            if(gestion[index] in post[0][i] ):
                counter_gestion = counter_gestion + 1
            if  re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 1
            index += 1
        index = 0
        for x in gestion_clave:
            if(gestion_clave[index] in post[0][i] ):
                counter_gestion = counter_gestion + 5
            if re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 5
            index += 1
    list_counter.append(counter_gestion)
    i=0
    for i in xrange(0,lon):
        index = 0
        for x in movilidad:
            if(movilidad[index] in post[0][i]):
                counter_movilidad += 1
            if  re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 1

            index += 1
        index = 0
        for x in movilidad_clave:
            if(movilidad_clave[index] in post[0][i]):
                counter_movilidad += 5
            if re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 5
            index += 1
    list_counter.append(counter_movilidad)
    i=0
    for i in xrange(0,lon):
        index = 0
        for x in basurero:
            if(basurero[index] in post[0][i]):
                counter_basurero += 1
            if  re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 1
            index += 1
        index = 0
        for x in basurero_clave:
            if(basurero_clave[index] in post[0][i]):
                counter_basurero += 5
            if re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 5
            index += 1
    list_counter.append(counter_basurero)
    i=0
    for i in xrange(0,lon):
        index = 0
        for x in mercados:
            if(mercados[index] in post[0][i]):
                counter_mercado += 1
            if  re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 1
            index += 1
        index = 0
        for x in mercados_clave:
            if(mercados_clave[index] in post[0][i]):
                counter_mercado += 5
            if re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 5
            index += 1
    list_counter.append(counter_mercado)
    i=0
    for i in xrange(0,lon):
        index = 0
        for x in resilencia:
            if(resilencia[index] in post[0][i]):
                counter_resilencia += 1
            if  re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 1
            index += 1
        index = 0
        for x in resilencia_clave:
            if(resilencia_clave[index] in post[0][i]):
                counter_resilencia += 5
            if re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 5
            index += 1
    list_counter.append(counter_resilencia)
    i=0
    for i in xrange(0,lon):
        index = 0
        for x in infraestructura:
            if(infraestructura[index] in post[0][i]):
                counter_infraestructura += 1
            if  re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 1
            index += 1
        index = 0
        for x in infraestructura_clave:
            if(infraestructura_clave[index] in post[0][i]):
                counter_infraestructura += 5
            if re.search(x+'*', post[0][i]):
                counter_gestion = counter_gestion + 5
            index += 1
    list_counter.append(counter_infraestructura)
    index = 0
    bandera = 0
    for l in xrange(0, len(list_counter)):
        for j in xrange(0, len(list_counter)):
            if((list_counter[l] > list_counter[j]) and (l <> j)):
                bandera =l+1
    if((list_counter[0] == list_counter[1]) and (list_counter[1] == list_counter[2]) and (list_counter[2] == list_counter[3]) and (list_counter[3] == list_counter[4])):
        bandera = 7

    if bandera == 1:
        return "#gestion"
    if bandera == 2:
        return"#movilidad"
    if bandera == 3:
        return "#basurero"
    if bandera == 4:
        return "#mercados"
    if bandera == 5:
        return "#resilencia"
    if bandera == 6:
        return "#infraestructura"
    if bandera == 7:
        return "#gestion #movilidad #basura ..."
    if bandera == 0:
        return "ninguno"

Assignment_hashtag()
