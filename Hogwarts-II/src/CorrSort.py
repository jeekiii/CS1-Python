#!/usr/bin/python3
# -*- coding: utf-8 -*-

knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
             ['Ravenclaw', ['smart', 'wise', 'curious']],
             ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
             ['Slytherin', ['cunning', 'wily', 'malignant']]]

def house_designation(student_qualities):
    ranking = []
    for list in knowledge:
        count = 0
        for q in student_qualities:
            if q in list[1]:
                count += 1
        ranking.append(count)
    return knowledge[ranking.index(max(ranking))][0]