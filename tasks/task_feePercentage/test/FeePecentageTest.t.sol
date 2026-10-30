// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

import {Test} from "../lib/forge-std/src/Test.sol";
import {FeePercentage} from "../src/FeePercentage.sol";

contract FeePercentageTest is Test{
    FeePercentage public feeCalc;

    function setUp() external{
        feeCalc = new FeePercentage();
    }

    function testFeeCalculator600() public{
        assertEq(feeCalc.feeCalculator(600),120);
    }
}

