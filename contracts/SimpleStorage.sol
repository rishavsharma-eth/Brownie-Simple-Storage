// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage{
   
   uint256 public favoriteNumber;

   function store(uint256 _favoriteNumber) public returns(uint256) {
       favoriteNumber = _favoriteNumber;
       return _favoriteNumber;
   }

   function retrieve() public view returns(uint256){
           return favoriteNumber;
   }
    
    // struct helloWorld{
    //     uint256 thisInteger;
    //     string thisBool;
    // }

    struct shawty{
        uint256 thisInteger1;
        string thisBool1;
    }

    // helloWorld public hi = helloWorld({thisInteger:343, thisBool:true});
    shawty[] public widow; 
    mapping(string => uint256) public firstMappingFunction;

    function thisFunction (string memory _name, uint256 thisInteger) public{
        // widow.push(shawty({thisInteger1: thisInteger, thisBool1: _name}));
        // We can also write the above line as
        widow.push(shawty(thisInteger, _name));
        firstMappingFunction[_name] = thisInteger;
    }
}
