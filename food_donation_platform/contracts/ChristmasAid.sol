pragma solidity ^0.8.0;

contract ChristmasAid {
    address public owner;
    mapping(address => uint256) public donations;
    address[] public recipients;

    constructor() {
        owner = msg.sender;
    }

    function donate() public payable {
        require(msg.value > 0, "Donation must be greater than 0");
        donations[msg.sender] += msg.value;
    }

    function addRecipient(address recipient) public {
        require(msg.sender == owner, "Only the owner can add recipients");
        recipients.push(recipient);
    }

    function distributeFunds() public {
        require(msg.sender == owner, "Only the owner can distribute funds");
        uint256 share = address(this).balance / recipients.length;
        for (uint256 i = 0; i < recipients.length; i++) {
            payable(recipients[i]).transfer(share);
        }
    }
}
