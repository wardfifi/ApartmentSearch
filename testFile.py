#testFile

from lab06 import *
from Apartment import * 

def test_ensureSortedAscending():

    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    a0 = Apartment(1115, 215, "average")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 225, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(800, 190, "excellent")
    a5 = Apartment(500, 250, "average")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_mergesort():
    numList1 = [9,8,7,6,5,4,3,2,1]
    numList2 = [1,2,3,4,5,6,7,8,9]
    numList3 = []
    numList4 = [1,9,2,8,3,7,4,6,5]
    numList5 = [5,4,6,3,7,2,8,1,9]
    mergesort(numList1)
    mergesort(numList2)
    mergesort(numList3)
    mergesort(numList4)
    mergesort(numList5)
    assert numList1 == [1,2,3,4,5,6,7,8,9]
    assert numList2 == [1,2,3,4,5,6,7,8,9]
    assert numList3 == []
    assert numList4 == [1,2,3,4,5,6,7,8,9]
    assert numList5 == [1,2,3,4,5,6,7,8,9]

def test_getBestApartment():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    mergesort(apartmentList)
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad"
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(900, 210, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    mergesort(apartmentList)
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent"

def test_getWorstApartment():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    mergesort(apartmentList)
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad"
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(900, 210, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    mergesort(apartmentList)
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad"
    a0 = Apartment(800, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 205, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(900, 210, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    mergesort(apartmentList)
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average"

def test_getAffordableApartments():
    a0 = Apartment(800, 215, "bad")
    a1 = Apartment(920, 215, "average")
    a2 = Apartment(865, 205, "excellent")
    a3 = Apartment(959, 190, "excellent")
    a4 = Apartment(799, 190, "excellent")
    a5 = Apartment(900, 210, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    mergesort(apartmentList)
    assert getAffordableApartments(apartmentList, 799) == "(Apartment) Rent: $799, Distance From UCSB: 190m, Condition: excellent"
    a0 = Apartment(800, 215, "bad")
    a1 = Apartment(920, 215, "average")
    a2 = Apartment(865, 205, "excellent")
    a3 = Apartment(959, 190, "excellent")
    a4 = Apartment(799, 190, "excellent")
    a5 = Apartment(900, 210, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    mergesort(apartmentList)
    assert getAffordableApartments(apartmentList, 900) == "(Apartment) Rent: $799, Distance From UCSB: 190m, Condition: excellent\n\
(Apartment) Rent: $800, Distance From UCSB: 215m, Condition: bad\n\
(Apartment) Rent: $865, Distance From UCSB: 205m, Condition: excellent\n\
(Apartment) Rent: $900, Distance From UCSB: 210m, Condition: bad"

def test_getApartmentDetails():

    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    mergesort(apartmentList)
    assert a0.getApartmentDetails() == "(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad"
    assert a1.getApartmentDetails() == "(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average"
    assert a2.getApartmentDetails() == "(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: excellent"
    assert a3.getApartmentDetails() == "(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent"
    assert a4.getApartmentDetails() == "(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent"
    assert a5.getApartmentDetails() == "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad"

def test__lt__():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    assert (a0 < a4) == False
    assert (a1 < a2) == False
    assert (a3 < a2) == True

def test__eq__():
    a0 = Apartment(950, 215, "excellent")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(950, 190, "excellent")
    a5 = Apartment(500, 215, "average")
    assert (a3 == a4) == True
    assert (a1 == a2) == False
    assert (a0 == a2) == True
    assert (a2 == a3) == True
    assert (a2 == a5) == False

def test__gt__():

    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    assert (a0 > a4) == True
    assert (a1 > a2) == True
    assert (a0 > a1) == True
    assert (a4 > a0) == False

