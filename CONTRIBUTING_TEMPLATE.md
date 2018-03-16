[comment]: <> (This file is intended to be a template for a contributions statement for repositories within the OpenGeoMetadata organization. Feel free to edit and revise as needed.)

# [name_of_institution] GeoBlacklight Metadata Repository

This repository is the most current source for geospatial metadata housed within the **[insert instituion name here](https://www.linktolivegeoblacklightgoeshere.org)** collection. We encourage any institution to index our metadadata into their own discovery environment(s).

[comment]: <> (If your organization uses Travis-CI for metadata validation checks, you can follow this convention to put a link to the build-failing shield. Otherwise, just delete this section.)

#### Metadata validation checks

Our metadata is validated to be in compliance with the current [GeoBlacklight 1.0 schema](https://github.com/geoblacklight/geoblacklight/blob/master/schema/geoblacklight-schema.md) through Travis-CI. Click the "build-failing" button below to see which of our records (if any) have validation errors.

[![Build Status](https://api.travis-ci.org/OpenGeoMetadata/edu.nyu.svg?branch=master)](https://travis-ci.org/OpenGeoMetadata/edu.nyu)

#### Contribution and enhancement status

[comment]: <> (We suggest that you indicate the status of whether or not you are open to others contributing to your repository in this section by using a green, yellow, or red dot. Green means that suggestions are welcome, yellow means that suggestions may be welcome, but people should communicate with the repository owner(s) first before suggesting any remediations, and red means that there are procedural or other obstacles that preclude anyone in the community from posing metadata enhancements.)

![Open for metadata contributions](https://upload.wikimedia.org/wikipedia/commons/archive/0/0e/20170421060213%21Location_dot_green.svg) *Open for metadata contributions and enhancements*

[comment]: <> (You may want to provide a list of things that you're interested in others doing to your metadata. This is optional)

#### Suggested enhancements our existing metadata

There are manny potential ways members of the GeoBlacklight community can enhance our metadata. Some examples include (but are not limited to):
* Fixing typos
* Normalizing string values for subjects and placenames
* Adding placename strings to records
* Enhancing descriptions
* Correcting errors on bounding box values
* Suggesting references for contextual information
* Submitting fixes for invalid records

[comment]: <> (We highly recommend that you describe your process for how you prefer metadata fixes to be made. Feel free to link to instructions, external forms, scripts, or other interfaces that may improve your own local workflow.)

#### Preferred process for submitting enhancements

We prefer that enhancements be consolidated into as few branches as possible. Here is a suggested workflow:
* Clone our entire repository to your desktop
* Save all new or updated files according to our naming convention
* Create a branch and name it in such a way that names and describes the nature of your fixes. If the scope of the changes is large, you may want to create an issue to describe your intended work
* Submit a pull request to the master branch

#### Contact Information

If you have any questions about remediating this metadata or would like to discuss larger-scale remediation projects, please reach out to **[insert names and contact information]** or create an issue within this repository.
