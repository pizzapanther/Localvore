# Localvore.Guide

[Team Hairball's](https://github.com/koding/global.hackathon/blob/master/Teams/TeamHairball/ABOUT.md) Koding Global Virtual Hackathon's Submission

Koding.com Hosted Site URL: http://dev.localvore.guide/

## Description

[![Koding Hackathon](https://raw.githubusercontent.com/pizzapanther/Localvore/master/about/badge.png "Koding Hackathon")](https://koding.com/Hackathon)

Localvore.Guide was conceived when my wife was trying to find more information about local farmers markets which usually do not have a good presence on the web. The concept was then expanded to include other local businesses so we can help support the local economy and jobs. The term _Localvore_ is often used to represent consumers that eat food that is grown within 150 miles, but we wanted to expand it to mean a consumer that consumes goods that originate locally.

To help local businesses grow, we see two areas of improvement. First, local businesses need help to market themselves better to sell more. And secondly, local businesses need tools and services to help them function as efficiently as a bigger businesses. Localvore.Guide starts tackling the first problem by showcasing local businesses. We've started by curating a list of businesses in Houston, TX, our home town.

The hackathon theme Localvore.Guide applies to is "Problems facing our planet" because we feel keeping a thriving local economy is key to sustaining people as software eats the world and businesses become more efficient. We need to help local businesses and entrepreneurs thrive. Localvore.Guide does this by presenting local businesses in a manner that makes them easy to find and engage with by using maps and geographically sorted data.

## The Tech

Localvore.Guide uses a Django backend powered with PostGIS so we can do fast geospatial queries to find the best places near you. On the frontend we've implemented Material Design with AngularJS. While right now the app is
hosted on the web, this combination allows us to package the app for Android and iOS by just expanding our build process.

## Screenshots

Here provide couple screenshots of your project. You can use a tool like https://monosnap.com/welcome or https://droplr.com to take a screenshot. Animated gifs are also welcome.

Homepage - Featured Listings
![Homepage - Featured Listings](https://raw.githubusercontent.com/pizzapanther/Localvore/master/about/ss1.png "Homepage - Featured Listings")

Restuarant Listings
![Restuarant Listings](https://raw.githubusercontent.com/pizzapanther/Localvore/master/about/ss2.png "Restuarant Listings")

Listing Detail Page
![Listing Detail Page](https://raw.githubusercontent.com/pizzapanther/Localvore/master/about/ss3.png "Listing Detail Page")

## APIs used

- **Yelp API**: used to look up business ratings
- **Google Maps**: used to produce maps and look up addresses and geospatial coordinates
- **Google Places API**: used to look up business ratings
