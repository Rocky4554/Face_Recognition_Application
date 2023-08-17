-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2022 at 06:21 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `regteach`
--

CREATE TABLE `regteach` (
  `fname` varchar(50) NOT NULL,
  `lname` varchar(45) NOT NULL,
  `cnum` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `ssq` varchar(45) NOT NULL,
  `sa` varchar(45) NOT NULL,
  `pwd` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `regteach`
--

INSERT INTO `regteach` (`fname`, `lname`, `cnum`, `email`, `ssq`, `sa`, `pwd`) VALUES
('muskan', 'gupta', '6206722170', 'guptamuskan0607@gmail.com', 'Your Nick Name', 'rinki', 'Muskan@12345');

-- --------------------------------------------------------

--
-- Table structure for table `stdattendance`
--

CREATE TABLE `stdattendance` (
  `std_id` varchar(45) NOT NULL,
  `std_roll_no` varchar(45) NOT NULL,
  `std_name` varchar(45) NOT NULL,
  `std_time` varchar(45) NOT NULL DEFAULT current_timestamp(),
  `std_date` varchar(45) NOT NULL,
  `std_attendance` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stdattendance`
--

INSERT INTO `stdattendance` (`std_id`, `std_roll_no`, `std_name`, `std_time`, `std_date`, `std_attendance`) VALUES
('1', '4', ' muskan', '11:46:36', '01/12/2022', 'Present'),
('2', '5', 'raunak', '11:47:49', ' 01/12/2022', 'Absent'),
('3', '8', ' binod', '12:11:14', ' 01/12/2022', 'Present');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Student_ID` int(11) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Department` varchar(45) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `Division` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `Mobile_No` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Roll_No` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Teacher_Name` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Student_ID`, `Name`, `Department`, `Course`, `Year`, `Semester`, `Division`, `Gender`, `DOB`, `Mobile_No`, `Address`, `Roll_No`, `Email`, `Teacher_Name`, `PhotoSample`) VALUES
(1, 'muskan', 'BTECH', 'CSE', '2019-23', 'Semester-7', 'Morning', 'Female', '06/07/1999', '88888888', 'abcdefgh', '4', 'muskan@gmail.com', 'abcd', 'No'),
(2, 'raunak', 'BTECH', 'EE', '2020-24', 'Semester-8', 'Morning', 'Male', '1/5/1999', '1234567', 'abgchjm', '5', 'raunak@gmail.com', 'adcnj', 'No'),
(3, 'binod', 'BSC', 'IT', '2017-21', 'Semester-4', 'Morning', 'Male', '4/7/89', '1234567', 'dto', '8', 'binod@gmail.com', 'hgfhkk', 'No');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `regteach`
--
ALTER TABLE `regteach`
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `pwd` (`pwd`);

--
-- Indexes for table `stdattendance`
--
ALTER TABLE `stdattendance`
  ADD PRIMARY KEY (`std_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Student_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `Student_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
