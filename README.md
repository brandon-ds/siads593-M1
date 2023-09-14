# SIADS 593: Milestone I - The Value of Skill: FIFA Ratings vs Real-World Transfer Fees

![Contributors](https://img.shields.io/badge/Contributors-3-brightgreen)
<!--![Forks](https://img.shields.io/badge/Forks-2-blue)
![Stargazers](https://img.shields.io/badge/Stars-5-orange)
![Issues](https://img.shields.io/badge/Issues-4-red)
![MIT License](https://img.shields.io/badge/License-MIT-yellow)
--!>

<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://github.com/your_username_/Project-Name">
    <img src="https://c8.alamy.com/comp/2CBM9RJ/fifa-2CBM9RJ.jpg" alt="FIFA Logo" width="80" height="80">
  </a>
</p>


  <h3 align="center">The Value of Skill: FIFA Ratings vs Real-World Transfer Fees</h3>

  <p align="center">
    Analyzing the correlation between FIFA Ratings and Real-World Football Transfer Fees.
    <br />
<!--     <a href="https://github.com/your_username_/Project-Name"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/your_username_/Project-Name">View Demo</a>
    ·
    <a href="https://github.com/your_username_/Project-Name/issues">Report Bug</a>
    ·
    <a href="https://github.com/your_username_/Project-Name/issues">Request Feature</a> -->
  </p>
</p>

## Table of Contents

1. [About The Project](#about-the-project)
2. [Datasets](#datasets)
3. [Cleaning and Manipulation](#cleaning-and-manipulation)
4. [Analysis](#analysis)
5. [Visualizations](#visualizations)
6. [Ethical Considerations](#ethical-considerations)
7. [Contributions](#contributions)
9. [Advisor](#advisor)

## About The Project

This project aims to explore the relationships between the athletic prowess of association football players and the transfer fees clubs pay to obtain players from other organizations. We will be leveraging player ratings from EA Sports FIFA video games and real-world transfer fees to assess which elements of a player's abilities (e.g., pace, control, defense, and position) significantly impact their market value.

**Programming Language**: Python

## Datasets

### Primary Dataset

- **Description**: FUTbin.com has compiled FIFA player ratings, each having about 70 attributes. The dataset contains players rated on a 1-100 scale on various skills like speed, body type, shot accuracy, and physical data.
- **Estimated Size**: Approximately 90,000 records each with 70 attributes.
- **Location**: [FUTbin](https://www.futbin.com/players

- - **Format**: HTML / Google Sheet
- **Access Method**: Web scraping

### Secondary Datasets

#### Transfer Fees

- **Description**: A dataset on GitHub records the transfer fees for the most popular European leagues. This will be cross-referenced with the FIFA ratings.
- **Estimated Size**: 18MB
- **Location**: [GitHub](https://github.com/ewenme/transfers/tree/master/data)
- **Format**: CSV
- **Access Method**: Download or web scrape

#### Inflation Rates (Euros)

- **Description**: Dataset from Oregon State to adjust for inflation in the transfer fees, specific to the Euro currency.
- **Estimated Size**: 64KB
- **Location**: URL for Euro inflation dataset
- **Format**: Excel Spreadsheet (.xlsx)
- **Access Method**: Download

## Cleaning and Manipulation

- Join datasets based on player names.
- Handle missing or anomalous data.
- Standardize player ratings.
- Normalize transfer fees for inflation (Euros).

## Analysis

- Distribution analysis of transfer fees.
- Clustering based on player ratings and transfer fees.
- Investigate outliers and possible lurking variables.

## Visualizations

- Pairplot segmented by player's position showing relationships between different skill metrics and transfer value.
- Scatter plot with standard deviation bands for FIFA player ratings against corresponding transfer fees.

## Ethical Considerations

- Subjectivity in FIFA ratings.
- Risk of stereotyping players through clustering.
- Inflation rates specific to the Euro currency.

## Contributions

- Austin Eck: Data gathering and cleaning, first drafts of written components.
- Brandon Loewit: Visualizations, bias mitigation.
- David Rezkalla: Data merging, analysis.


## Advisor

Anthony Whyte 
email: arwhyte@umich.edu


