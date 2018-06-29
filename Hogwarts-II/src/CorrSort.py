#!/usr/bin/python3
# -*- coding: utf-8 -*-

knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
             ['Ravenclaw', ['smart', 'wise', 'curious']],
             ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
             ['Slytherin', ['cunning', 'wily', 'malignant']]]

def house_designation(student_qualities):
    ranking = []
    for lst in knowledge:
        count = 0
        for q in student_qualities:
            if q in lst[1]:
                count += 1
        ranking.append(count)
    ans = []
    for _ in range(4):
        ans.append(knowledge[ranking.index(max(ranking))][0])
        ranking[ranking.index(max(ranking))] = -1
    return ans