# tv-tropes-pantheon-search-database

Providing an easy way of sorting through the Trope Pantheons' inhabitants since 2024!

![Image](https://static.tvtropes.org/pmwiki/pub/images/tv_tropes_search_v1_0.png)

Coded in Python by [Lapsem](https://tvtropes.org/pmwiki/pmwiki.php/Tropers/Lapsem)

**Program began:** January 7th, 2024

**Uploaded to GitHub:** February 7th, 2024

## Overview
The purpose of this program is to provide a quick and easy way to sort through the inhabitants of the [Trope Pantheons](https://tvtropes.org/pmwiki/pmwiki.php/Pantheon/TropePantheons) of [TV Tropes](https://tvtropes.org/) -- cleaner than [the sprawling Google Docs spreadsheet](https://docs.google.com/spreadsheets/d/1syLqv_NT0ZQADdTmIfnCe12qHEyMBrW0SrgpSXufYE4/edit?usp=sharing) that was previously in use, and _far_ easier than sifting through the Related pages for a trope to check if the trope is or is not already represented in the Pantheons.

I originally coded and tested this program in [PyCharm](https://www.jetbrains.com/pycharm/), but I was advised to share it via GitHub so other people could more easily view it. However, this is not meant to stay on GitHub forevermore without moving anywhere else and is more meant as a proof-of-concept -- I created this program with the expectation that it would _eventually_ be implemented within TV Tropes. If that happens, then this page will remain as a place where people can check out how the TV Tropes Pantheon Search works.

## Usage
The `main.py` file brings up a menu that lets the user search by trope name, deity name, namespace, work title, rank, Hall, or House. These criteria are searched for via searchboxes that let the viewer use more than one keyword, except for Rank, which features a collection of check-boxes.

These criteria can all then be sorted in alphabetical order backwards and forwards -- except for Rank which is sorted in its own order -- and articles at the beginning of trope/work names are omitted in alphabetization (i.e., [The Berserker](https://tvtropes.org/pmwiki/pmwiki.php/Main/TheBerserker) is filed under B and not T, and _[A Christmas Carol](https://tvtropes.org/pmwiki/pmwiki.php/Literature/AChristmasCarol)_ is filed under C instead of A). Additionally, the program returns a count of how many results are returned per search.

## How it stores data
Instead of having a database that tropers manually add entries to and manually remove entries from, one file (`pantheon_data_recorder.py`) iterates over each line of every Pantheon page and checks for a certain commented-out phrase that holds deity data, to be written into a spreadsheet (`pantheon_data.csv`). For example, the profile for Street Fighter's M. Bison would look like this:

`%% PANTHEON SEARCH DATABASE DATA: [=ButForMeItWasTuesday,M. Bison,Franchise,StreetFighter,Intermediate God,VillainousPersonalitiesAndQuirks,Villainy=]`

Since this is a [.csv](https://en.wikipedia.org/wiki/Comma-separated_values) file, any entry therein that uses commas (such as for multiple characters in one profile) must be bookended by double-quotes (") or else it won't show up in the main program. For example:

`%% PANTHEON SEARCH DATABASE DATA: [=StarterMon,"Venusaur, Charizard and Blastoise",Franchise,Pokemon,Intermediate God,GameCharacters,Gaming=]`

The benefit of this system is that search-database entries can be added right alongside the profiles that they correspond to. As for removal, this system has automatic "garbage cleanup" by completely overwriting the spreadsheet's data whenever it's updated: when a profile is moved or deleted, the now-outdated corresponding data is automatically winked away into nothingness the next time the spreadsheet updates -- which I imagine would be once per day. That also means that there's no use in directly editing the spreadsheet, since any changes to it will be overwritten unless they come from a profile on a Pantheon page.

Additionally, the folders in this program store the test data that the program pulls from, and a text file (`list_of_pantheon_pages.txt`) stores the addresses of those text files -- both to be replaced with the internal addresses of the Pantheon page text data, should this be fully implemented.

Furthermore, the two .py files each have plenty of comments saying which code-block does what, and if you want to gain an even deeper understanding of this code, then feel free to read through them.

---

If you've got anything to say to me about this program, then please [message me on TV Tropes](https://tvtropes.org/pmwiki/wiki_pm.php?to_troper=Lapsem).

Happy searching!

-- Lapsem

---

**P.S.:** This program wasn't made for the [Dominions Expansion](https://tvtropes.org/pmwiki/pmwiki.php/Pantheon/DominionsExpansion) or the [Great Treasury](https://tvtropes.org/pmwiki/pmwiki.php/Pantheon/GreatTreasury).
