StudentRank.java
public class StudentRank {
    private String[] students;
    private int[] ranks;

    // Constructor
    public StudentRank(String[] students, int[] ranks) {
        this.students = students;
        this.ranks = ranks;
    }

    // Method to get the highest-ranked student
    public String highestRank() {
        int maxRankIndex = 0;
        for (int i = 1; i < ranks.length; i++) {
            if (ranks[i] > ranks[maxRankIndex]) {
                maxRankIndex = i;
            }
        }
        return students[maxRankIndex];
    }

    // Method to get the lowest-ranked student
    public String lowestRank() {
        int minRankIndex = 0;
        for (int i = 1; i < ranks.length; i++) {
            if (ranks[i] < ranks[minRankIndex]) {
                minRankIndex = i;
            }
        }
        return students[minRankIndex];
    }

    public static void main(String[] args) {
        String[] students = {"Taylor", "Wesley", "Jordan"};
        int[] ranks = {1, 5, 3};
        StudentRank sr = new StudentRank(students, ranks);

        System.out.println(sr.highestRank()); // Output: Wesley
        System.out.println(sr.lowestRank());  // Output: Taylor
    }
}
------------------------------------------------------------------------------------------
CustomerList.js
----------------

import React from 'react'

function CustomerList({customers}) {
  return (
    <div className='layout-column align-items-center justify-content-start'>
        {customers.length == 0 && (
            <div data-testid='no-results'>No Results Found!</div>
        )}
        
        {customers.length > 0 && (
          <div className='card w-40 pt-30 pb-8 mt-20'>
                <table>
                    <thead>
                    <tr>
                        <th>Name</th>
                        <th>Age</th>
                        <th>Location</th>
                        <th>Gender</th>
                        <th>Income</th>
                    </tr>
                    </thead>
                    <tbody data-testid='searched-customers'>
                        {customers && customers.map((customer, i) => (
                          <tr key={`row-${i}`}> 
                              <td> {customer.name} </td> 
                              <td> {customer.age} </td> 
                              <td> {customer.location} </td>
                              <td> {customer.gender} </td> 
                              <td> {customer.income} </td>  
                          </tr>
                        )
                        )}
                    </tbody>
                </table>
          </div>
        )}
    </div>
  )
}

export default CustomerList;

------------------------------------------------------------------------------------------
SearchCustomer.js
-----------------

import React, { useState, useEffect } from "react"
import CustomerList from './CustomerList'
import List from '../List';

function SearchCustomer() {
  const [dataSearch, setDataSearch] = useState('')
  const [listFiltered, setListFiltered] = useState(List)

  useEffect(() => {
    filterRowsBySearch()
	}, [dataSearch])

  const filterRowsBySearch = () => {
    if (dataSearch === '') {
      setListFiltered(List)
      return
    }

    const rowsFiltered = listFiltered.filter((row, i) => {
      const name = row.name,
            age = row.age.toString(),
            location = row.location,
            gender = row.gender,
            income = row.income;

      return name.startsWith(dataSearch) || age.startsWith(dataSearch) || location.startsWith(dataSearch) 
        || gender.startsWith(dataSearch) || income.startsWith(dataSearch)
    })

    setListFiltered(rowsFiltered)
  }

  const handleInputSearch = (e) => {
    setDataSearch(e.target.value)
	}

  return (
    <>
    <div className='layout-row align-items-center justify-content-center mt-30'>
        <input type="text" className='large mx-20 w-20' data-testid='search-input' value={dataSearch} placeholder='Enter search term (Eg: Phil)' onChange={handleInputSearch} />
    </div>
    <CustomerList customers={listFiltered} />
    </>
  )
}

export default SearchCustomer
