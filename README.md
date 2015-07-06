A repository for shared geospatial metadata collaboration.



### Organizational Structure

** Based off of comments and feedback on [#3](https://github.com/OpenGeoMetadata/metadatarepository/issues/3) and [#4](https://github.com/OpenGeoMetadata/metadatarepository/issues/4) *

An indvidual institution shall create and maintain geospatial metadata within its own individual repository hosted under the collaborative [OpenGeoMetadata](https://github.com/opengeometadata) organization. This structure will allow the benefit of appropriately namespaced identifiers and the ability for teams from individual institutions to collaborate on their metadata while still enabling machine harvestable metadata under a common organization.

#### Organization Owners

1 member from each participating institution will be added to the OpenGeoMetadata organization owner team. From there, they will have the rights to create, enable, and manage rights for their own institution's team. To be added for your institution please comment on [#8](https://github.com/OpenGeoMetadata/metadatarepository/issues/8).

#### Unique Namespace

Participating institutions will be able to create their own unique namespace as the name repository for their institution. This ensures that each institution maintains and is responsible for unique identifiers under their For example, an institution who uses an [ARK](link to ark) as a unique identifier with a linked persistant url may want to name their repository

```
edu.institution.arks
```

Institutions who do not have persistant urls for their resources may just with to use their institution as the namespace

```
edu.institution
```

Some examples already established include Princeton [edu.princeton.arks](https://github.com/OpenGeoMetadata/edu.princeton.arks) and Stanford [edu.stanford.purl](https://github.com/OpenGeoMetadata/edu.stanford.purl)


### Structure within an organizations repository

** Summarized from https://github.com/OpenGeoMetadata/metadatarepository/issues/3 **

Within its repository an organization has tremendous flexibility on how it organizes its metadata records. An optional file, `layers.json` is requested for easy mapping of layers to their location within an organization's repository (e.g., `Layer-Id : Folder`).

#### Basic directory structure

For an organization with a small number of records (e.g., 250 records), a basic structure within your repository is achievable. A directory should be created for *each* layer (or item described). That directory shall be named based off of the unique identifier generated or given. Each directory shall contain the metadata for that layer, in whichever standardized format an institution deems appropriate.

**Directory structure**
```
/layer123/fgdc.xml
/layer124/fgdc.xml
/layer125/fgdc.xml
```

#### Advanced directory structure

For an organization with a large amount of described layers, a flat directory structure may be inappropriate due to performance issues. A more advanced directory structure may be needed. Examples of this could include:

**Directory structure** ([View on Github](https://github.com/OpenGeoMetadata/edu.stanford.purl))
```
/bb/338/jh/0716/iso19110.xml
               /iso19139.xml
               /preview.jpg
/bb/509/gh/7292/iso19110.xml
               /iso19139.xml
               /preview.jpg
/bc/899/yk/4538/iso19110.xml
               /iso19139.xml
               /preview.jpg
layers.json
```

**layers.json** ([View on Github](https://github.com/OpenGeoMetadata/edu.stanford.purl/blob/master/layers.json))
```
{
  "druid:bb338jh0716": "bb/338/jh/0716",
  "druid:bb509gh7292": "bb/509/gh/7292",
  "druid:bc899yk4538": "bc/899/yk/4538",
  ...
}
```

#### Metadata within a directory

Institutions can include as much or as little metadata within a layers individual directory. A common practice is naming the file based off of the schema it is created with.

**Example directory within /bc/899/yk/4538/** ([View on Github](https://github.com/OpenGeoMetadata/edu.stanford.purl/tree/master/bc/899/yk/4538))
```
geoblacklight.xml
iso19110.xml
iso19139.xml
mods.xml
preview.jpg
```


### Benefits of Github platform

While adopting and using a platform for a collaborative effor is no trivial task, we see many benefits of starting with and using Github as way forward.

#### Github has a lot of functionality already baked in

Features and functionality that may be needed now or in the future including:

 - User authentication and groups
 - Commenting
 - Multi organizational structure
 - Open platform by default
 - Robost API
 - High availability
 - Free for public data/code
 
These features offer a tremendous advantage for  new project such as this. We don't have to go and rebuild this functionality somewhere else, instead we can focus on the metadata sharing. Github also offers web and desktop based graphical user interfaces so non technical users can also easily contribute.

Github also allows us to access the raw metadata from each repository in a machine readable format. Git enables us to quickly determine whether metadata has been updated (SHA comparison)
