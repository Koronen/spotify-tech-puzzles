# Bilateral Projects
## Problem ID: bilateral

A friend of yours works at an undisclosed company in the music streaming
industry, and needs your help. The company has offices in Stockholm and London,
and collaboration between the two offices is extensive. The situation is that
each of the many but small projects is handled by a two-person team with a
member in each city. While emails, faxes, and phones are wonderful, and work
well within each team, the CEO wants a briefing every year on the projects. For
this purpose the CEO invites representatives from the projects to Barbados for
a week of beach fun presentations of all the projects. However, money is tight
and a new policy has been created: the CEO wants at least one person from each
project, and additionally, she wants to invite as few people as possible. This
is where you come in. In order to help your friend get a ticket to Barbados,
you are to write a program that, given all the two-person teams, computes the
smallest number of people that must be invited in order to get at least one
person from each project, as well as a list of people to invite. If possible
(subject to the set of people being smallest possible), the list of invitees
should include your friend.

### Input
The first line of input contains an integer 1 ≤ m ≤ 10 000, the number of
teams. The following m lines each contain two integers, i, j separated by a
space, being the employee IDs of the two employees in that team (the first one
is from Stockholm and the second one is from London). Stockholm employees have
IDs in the range 1000 to 1999 and London employees have IDs in the range 2000
to 2999. An employee can be a member of several teams, but there cannot be
several teams consisting of the same pair of employees. Your friend has ID
1009.

### Output
Output first a single line with an integer k indicating the smallest number of
employees that must be invited to meet the requirements above. Then output k
lines giving the IDs of employees to invite. If possible (subject to k being
smallest possible), the list should contain your friend.

If there are several solutions subject to these constraints, anyone is
acceptable.
