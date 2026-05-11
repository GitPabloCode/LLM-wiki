
---
<!-- pagina 1 -->

[¶0]
| ERTMS/ETCS                                               | ERTMS/ETCS                                               |
|----------------------------------------------------------|----------------------------------------------------------|
| System Requirements Specification Chapter 1 Introduction | System Requirements Specification Chapter 1 Introduction |
| REF :                                                    | SUBSET-026-1                                             |
| ISSUE :                                                  | 3.6.0                                                    |
| DATE :                                                   | 13/05/2016                                               |


---
<!-- pagina 2 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1]

# 1.1 Modification History [¶2]

[¶3]
| Issue Number Date     | Section Number                        | Modification / Description                                                                | Author / Editor    |
|-----------------------|---------------------------------------|-------------------------------------------------------------------------------------------|--------------------|
| 0.0.1                 | All                                   | first issue                                                                               | SAB                |
| 0.1.0                 | All                                   | Review comments from Adtranz                                                              | SAB                |
| 1.0.0                 | All                                   | Final review                                                                              | SAB                |
| 1.0.2 / 15. Apr. 1999 | All                                   | Reworked edition                                                                          | SAB                |
| 1.0.3 / 22. Apr. 1999 | 1.8.9                                 | Comment of Alstom                                                                         | SAB                |
| 1.1.0 / 23. Apr. 1999 |                                       | Final issue of class P SRS                                                                | Ch. Frerichs (ed.) |
| 1.1.1 / 27. Mai 1999  | 1.3.1.1/1.7.1.2                       | Review comments added                                                                     | SAB                |
| 1.1.2                 |                                       | Draft for class 1                                                                         | SAB                |
| 1.1.3 990729          | Document reference number.            | Revision during finalisation meeting, Stuttgart 990729                                    | HE                 |
| 1.2.0 990730          | Version number                        | Release version                                                                           | HE                 |
| 1.2.1 991209          | All                                   | First draft for 2 nd release                                                              | SAB                |
| 1.3.0 991216          | All                                   | Review comments added                                                                     | SAB                |
| 2.0.0 991222          | Minor editing                         | Finalisation                                                                              | SAB                |
| 2.0.1                 | All                                   | Corrections after review                                                                  | SAB                |
| 2.1.0                 | Version number                        | UNISIG release                                                                            | SAB                |
| 2.2.0                 | Version number                        | UNISIG release                                                                            | SAB                |
| 2.2.2 1.2.2002        | Version number                        | Final edition                                                                             | Ch. Frerichs       |
| 2.3.0 24/02/06        | Version number, no change since 2.2.2 | Release version                                                                           | HK                 |
| 3.0.0 23/12/08        | 1.8.7                                 | Release version Re-use of chapter 6, now dedicated to management of older system versions | AH                 |


---
<!-- pagina 3 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶4]

[¶5]
| 3.0.1 22/12/09   |                                                                  | Including the results of the editorial review of the SRS 3.0.0                  | AH   |
|------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------|------|
| 3.1.0 22/02/10   | No change                                                        | Release version                                                                 | AH   |
| 3.2.0 22/12/10   | No change                                                        | Release version                                                                 | AH   |
| 3.2.1 13/12/11   |                                                                  | Including all CR's that are in state 'Analysis completed' according to ERA CCM. | AH   |
| 3.3.0 07/03/12   |                                                                  | Baseline 3 release version                                                      | AH   |
| 3.3.1 04/04/14   | No change                                                        |                                                                                 | OG   |
| 3.3.2 23/04/14   | No change                                                        | Baseline 3 1 st maintenance pre-release version                                 | OG   |
| 3.3.3 06/05/14   | No change                                                        | Baseline 3 1 st maintenance 2 nd pre-release version                            | OG   |
| 3.4.0 12/05/14   | No change                                                        | Baseline 3 1 st maintenance release version                                     | OG   |
| 3.4.1 23/06/15   | No change                                                        |                                                                                 | OG   |
| 3.4.2 17/11/15   | CR1266                                                           |                                                                                 | OG   |
| 3.4.3 16/12/15   | Update due to overall CR consolation                             | phase                                                                           | OG   |
| 3.5.0 18/12/15   | Baseline 3 2 nd release version as EC (see ERA-REC-123-2015/REC) | recommended to                                                                  | OG   |
| 3.5.1 28/04/16   | No change                                                        |                                                                                 | OG   |
| 3.6.0 13/05/16   | Baseline 3 2 nd release                                          | version                                                                         | AH   |


---
<!-- pagina 4 -->

# 1.2 Table of Contents [¶6]

| 1.1                                                                                                                            | Modification History...........................................................................................................2     |
|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| 1.2                                                                                                                            | Table of Contents..............................................................................................................4     |
| 1.3                                                                                                                            | Introduction.......................................................................................................................5 |
| 1.4                                                                                                                            | Advantages of an International Interoperable System.......................................................5                          |
| 1.5                                                                                                                            | About this Document.........................................................................................................5        |
| 1.6                                                                                                                            | How to Read and Use the SRS.........................................................................................6                |
| 1.7                                                                                                                            | Requirements ...................................................................................................................6    |
| 1.8                                                                                                                            | Contents of the SRS.........................................................................................................6        |
| 1.8.2 Chapter 1: Introduction ..............................................................................................7  | 1.8.2 Chapter 1: Introduction ..............................................................................................7        |
| 1.8.3 Chapter 2: Basic System Description.........................................................................7            | 1.8.3 Chapter 2: Basic System Description.........................................................................7                  |
| 1.8.4 Chapter 3: Principles..................................................................................................7 | 1.8.4 Chapter 3: Principles..................................................................................................7       |
| 1.8.5                                                                                                                          | Chapter 4: Modes and Transitions .............................................................................7                      |
| 1.8.6                                                                                                                          | Chapter 5: Procedures...............................................................................................7                |
| 1.8.7                                                                                                                          | Chapter 6: Management of older System Versions....................................................7                                  |
| 1.8.8                                                                                                                          | Chapter 7: ERTMS/ETCS Language .........................................................................7                            |
| 1.8.9                                                                                                                          | Chapter 8: Messages.................................................................................................8                |
| 1.8.10                                                                                                                         | Chapter 9: Classification of the SRS clauses.............................................................8                           | [¶7]


---
<!-- pagina 5 -->

# 1.3 Introduction [¶8]

- 1.3.1.1 Train control is an important part of any railway operations management system. In the past  a  number  of  different  Automatic  Train  Control  (ATC)  systems  have  evolved  in different  countries  at  different  times.  These  systems  are  incompatible  and  not interoperable with each other. Only a few of these systems are used in more than one country, and even in those cases there have been differences in detailed development which have resulted in incompatible and not interoperable versions. [¶9]

- 1.3.1.2 Many  railways  anticipate  a  significant  increase  in  density  of  train  traffic  and  are rethinking their infrastructure strategy, to accommodate high levels of traffic, in which ATC  systems  play  an  important  part.  Also  many  railways  would  like  to  introduce standardised  systems  to  reduce  system  costs.  In  order  to  establish  international standardisation of ATC systems, the following document specifies the European Rail Traffic Management System/European Train Control System (ERTMS/ETCS). [¶10]

# 1.4 Advantages of an International Interoperable System [¶11]

- 1.4.1.1 The advantages expected by the railways can be summarised as: [¶12]

-  Cross border interoperability. [¶13]

-  Improvement of the safety of national and international train traffic. [¶14]

-  Improvement of international passengers and freight train traffic management. [¶15]

-  Shorter  headway  on heavily trafficked  lines,  by  driving  on  moving  block,  enabling exploitation of maximum track capacity. [¶16]

-  The possibility of step-by-step introduction of the new technology. [¶17]

-  Enabling  Pan-European competition between the manufacturers of ERTMS/ETCS components.  Strengthening  the  position  of  the  European  railway  industry  on  the world market. [¶18]

-  Enabling  preconditions  for future harmonisation  in  other  areas  of  rail traffic management. [¶19]

# 1.5 About this Document [¶20]

- 1.5.1.1 The purpose of this document is to specify the unified European Train Control System (ETCS) from a technical point of view. [¶21]

- 1.5.1.2 Some parts of the system are only specified to allow a migration from existing train control systems to ETCS (e.g. STM's) over a transition period. They might be removed in a future edition of the standard. [¶22]

- 1.5.1.3 To reach technical interoperability it is necessary not only that telegrams are generated and  understood  according  to  well  specified  rules  but  also  that  a  train  respectively [¶23]


---
<!-- pagina 6 -->

trackside  equipment  reacts  in  a  uniform  way  to  information  received.  Technical interoperability requires specifications of a detailed level. [¶24]

- 1.5.1.4 For  operational  interoperability  it  is  necessary  to  add  operating  rules,  engineering standards etc.  to  the  system  design.  Reaching  operational  interoperability  is  outside the scope of the SRS. [¶25]

# 1.6 How to Read and Use the SRS [¶26]

- 1.6.1.1 The SRS covers 9 chapters, which are briefly described in the section following this introduction. [¶27]

- 1.6.1.2 All  readers may need to refer to the Glossary of terms and abbreviations (SUBSET023). [¶28]

# 1.7 Requirements [¶29]

- 1.7.1.1 This specification defines the functions that allow reaching the technical interoperability.  This  is  materialised  through  numbered  clauses  which  are  formally identified  as  containing  ERTMS/ETCS  on-board  and/or  ERTMS/ETCS  trackside requirements (see details in chapter 9). [¶30]

- 1.7.1.2 The ERTMS/ETCS on-board equipment shall implement all its allocated requirements, with the only exceptions and conditions explicitly stated in the Control-Command and Signalling TSI and in this SRS. [¶31]

- 1.7.1.3 For  ERTMS/ETCS  trackside  the  implementation  of  functions  has  to  be  defined according to the characteristics of the specific lines and the related operational needs. In  any  case,  the  requirements  of  this  SRS,  which are  allocated  to the  trackside  and related to the implemented functions, shall be respected. [¶32]

- 1.7.1.4 Intentionally deleted. [¶33]

- 1.7.1.5 Not specified requirements and solutions shall only be permitted as long as they do not generate any interoperability problems. [¶34]

# 1.8 Contents of the SRS [¶35]

- 1.8.1.1 The  SRS  defines  the  system  requirements  for  the  European  Train  Control  System (ETCS) of ERTMS. [¶36]

- 1.8.1.2 This sub-section is intended to give a rough overview of the contents of each chapter within the SRS so that readers interested only in specialised subjects can easily find the relevant chapters. [¶37]


---
<!-- pagina 7 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶38]

# 1.8.2 Chapter 1: Introduction [¶39]

- 1.8.2.1 Chapter 1 (this chapter) gives a general introduction to the intention and structure of the SRS, including a brief overview of the contents of each chapter. [¶40]

# 1.8.3 Chapter 2: Basic System Description [¶41]

- 1.8.3.1 Chapter 2 gives an overview of the ERTMS/ETCS system structure. [¶42]

- 1.8.3.2 Chapter 2 also contains a description of the basic application levels. [¶43]

- 1.8.3.3 Chapter 2 does not contain technical requirements. [¶44]

# 1.8.4 Chapter 3: Principles [¶45]

- 1.8.4.1 Chapter 3 specifies the system principles of ETCS/ERTMS. These principles apply to onboard and trackside subsystems. [¶46]

- 1.8.4.2 The principles define the behaviour of the system in general and functional terms. [¶47]

# 1.8.5 Chapter 4: Modes and Transitions [¶48]

- 1.8.5.1.1 Chapter  4  defines  the  modes  of  the  ERTMS/ETCS  onboard  equipment  and  all transitions between modes. [¶49]

# 1.8.6 Chapter 5: Procedures [¶50]

- 1.8.6.1 Chapter  5  defines  the  dynamic  behaviour  of  procedures  that  are  necessary  for interoperability. Procedures are presented by a state transition chart and a corresponding table, where all elements (States, events, transitions) of the chart are defined.  The  description  of  the  procedures  shows  all  states  of  the  ERTMS/ETCS onboard  unit  and  the  conditions  that  must  be  fulfilled  to  switch  from  one  state  to another. [¶51]

# 1.8.7 Chapter 6: Management of older System Versions [¶52]

- 1.8.7.1.1 Chapter  6  defines  the  envelope  of  legally  operated  system  versions  and  lists  the exceptions  that  shall  apply  by  derogation  to  the  requirements  listed  in  the  other chapters  of  the  SRS,  when  an  older  ERTMS/ETCS  system  version  is  used  by  the trackside subsystem. [¶53]

# 1.8.8 Chapter 7: ERTMS/ETCS Language [¶54]

- 1.8.8.1 Chapter 7 defines and describes the necessary variables to be used for the data flow over  the  air  gap  between  track  and  train.  The  grouping  of  these  into  packets  is described. The format of messages is given in Chapter 8. [¶55]


---
<!-- pagina 8 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶56]

# 1.8.9 Chapter 8: Messages [¶57]

- 1.8.9.1 Chapter  8  defines  the  application  protocol  (format  and  content  of  messages,  logical sequence for radio) necessary to achieve technical interoperability. [¶58]

- 1.8.9.2 The  scope  of  this  chapter  is  limited  to  the  application  protocol  and  the  content  of messages. [¶59]

# 1.8.10 Chapter 9: Classification of the SRS clauses [¶60]

- 1.8.10.1 Chapter 9 encloses a classification into categories of all the clauses in the chapters 1 to 8 of the SRS. [¶61]

- 1.8.10.2 In  particular  to  assess  properly  the  compliance  of  an  ERTMS/ETCS  on-board equipment with the SRS, it identifies which clauses contain requirements allocated to the  ERTMS/ETCS  on-board  equipment  and  conversely  which  ones  do  not,  either because they  contain  requirements  allocated  to  the  ERTMS/ETCS  trackside  only  or because they are of another type. [¶62]


---
<!-- pagina 9 -->

# ERTMS/ETCS [¶63]

System Requirements Specification Chapter 2 Basic System Description [¶64]

REF : [¶65]

SUBSET-026-2 [¶66]

ISSUE : [¶67]

3.6.0 [¶68]

DATE  : [¶69]

13/05/2016 [¶70]


---
<!-- pagina 10 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶71]

# 2.1 Modification History [¶72]

[¶73]
| Issue Number Date   | Section Number                                                            | Modification / Description                                                    | Author       |
|---------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------|--------------|
| 0.0.1 19 july 1999  | All                                                                       | First class 1 draft using new templates and including contributions from WPs  | PZ           |
| 0.1.0 26 july 1999  | System architecture figure § 2.3.1.2                                      | Updating and introduction of Radio infill Reference to future class 1 deleted | PZ           |
| 1.0.0 29 July 1999  | Document version, editorial changes, updating the architecture figure.    | Finalisation in Stuttgart 990729                                              | HE           |
| 1.2.0 990730        | Version number                                                            | Release version                                                               | HE           |
| 1.2.1 991209        | All                                                                       | Draft for 2 nd release                                                        | SAB          |
| 1.3.0 9912016       | All                                                                       | Review comments added                                                         | SAB          |
| 2.0.0 991222        | Minor editing                                                             | Finalisation                                                                  | SAB          |
| 2.0.1               | All                                                                       | Corrections after review                                                      | SAB          |
| 2.1.0               | Minor editing                                                             | UNISIG release                                                                | SAB          |
| 2.2.0               | Version number                                                            | UNISIG release                                                                | SAB          |
| 2.2.2 1.2.2002      | Version number                                                            | Final edition                                                                 | Ch. Frerichs |
| 2.3.0 24/02/06      | Version number No change since 2.2.2                                      | Release version                                                               | HK           |
| 2.3.2 17/03/08      | Including CRs that are in state 'Analysis completed' according to ERA CCM | Working version                                                               | AH           |
| 3.0.0 23/12/08      | Version number No change since 2.3.2                                      | Release version                                                               | AH           |


---
<!-- pagina 11 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶74]

[¶75]
| 3.0.1 22/12/09   |                                                                                 | Including the results of the editorial review of the SRS 3.0.0 and the other error CR's that are in state 'Analysis completed' according to ERA CCM   | AH   |
|------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| 3.1.0 22/02/10   |                                                                                 | Release version                                                                                                                                       | AH   |
| 3.1.1 08/11/10   |                                                                                 | Including all CR's that are in state 'Analysis completed' according to ERA CCM                                                                        | AH   |
| 3.2.0 22/12/10   | No change                                                                       | Release version                                                                                                                                       | AH   |
| 3.2.1 13/12/11   |                                                                                 | Including all CR's that are in state 'Analysis completed' according to ERA CCM                                                                        | AH   |
| 3.3.0 07/03/12   |                                                                                 | Baseline 3 release version                                                                                                                            | AH   |
| 3.3.1 04/04/14   | No change                                                                       |                                                                                                                                                       | OG   |
| 3.3.2 23/04/14   | No change                                                                       | Baseline 3 1 st maintenance pre-release version                                                                                                       | OG   |
| 3.3.3 06/05/14   | No change                                                                       | Baseline 3 1 st maintenance 2 nd pre-release version                                                                                                  | OG   |
| 3.4.0 12/05/14   | No change                                                                       | Baseline 3 1 st maintenance release version                                                                                                           | OG   |
| 3.4.1 23/06/15   | CR1236                                                                          |                                                                                                                                                       | OG   |
| 3.4.2 17/11/15   | CR's 1237, 1265                                                                 |                                                                                                                                                       | OG   |
| 3.4.3 16/12/15   | No change                                                                       |                                                                                                                                                       | OG   |
| 3.5.0 18/12/15   | Baseline 3 2 nd release version as recommended to EC (see ERA-REC-123-2015/REC) | Baseline 3 2 nd release version as recommended to EC (see ERA-REC-123-2015/REC)                                                                       | AH   |
| 3.5.1 28/04/16   | No change                                                                       |                                                                                                                                                       | OG   |


---
<!-- pagina 12 -->

[¶76]
| 3.6.0    | Baseline 3 2 nd release version   | AH   |
|----------|-----------------------------------|------|
| 13/05/16 |                                   |      |


---
<!-- pagina 13 -->

# 2.2 Table of Contents [¶77]

| 2.1                                                                                                                          | Modification History...........................................................................................................2     | Modification History...........................................................................................................2     |
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| 2.2                                                                                                                          | Table of Contents..............................................................................................................5     | Table of Contents..............................................................................................................5     |
| 2.3                                                                                                                          | Introduction.......................................................................................................................6 | Introduction.......................................................................................................................6 |
| 2.3.1 Scope and purpose....................................................................................................6 | 2.3.1 Scope and purpose....................................................................................................6         |                                                                                                                                      |
| 2.4                                                                                                                          | System structure...............................................................................................................7     | System structure...............................................................................................................7     |
| 2.5                                                                                                                          | Subsystems ......................................................................................................................8   | Subsystems ......................................................................................................................8   |
| 2.5.1                                                                                                                        | 2.5.1                                                                                                                                | Trackside subsystem .................................................................................................8               |
| 2.5.2                                                                                                                        | 2.5.2                                                                                                                                | On-board subsystem..................................................................................................9                |
| 2.5.3                                                                                                                        | 2.5.3                                                                                                                                | ERTMS/ETCS reference architecture ......................................................................11                           |
| 2.6                                                                                                                          | Levels and transitions .....................................................................................................12       | Levels and transitions .....................................................................................................12       |
| 2.6.1                                                                                                                        | 2.6.1                                                                                                                                | Introduction..............................................................................................................12         |
| 2.6.2                                                                                                                        | 2.6.2                                                                                                                                | Definitions................................................................................................................12        |
| 2.6.3                                                                                                                        | 2.6.3                                                                                                                                | ERTMS/ETCS Application Level 0 ...........................................................................14                         |
| 2.6.4                                                                                                                        | 2.6.4                                                                                                                                | ERTMS/ETCS Application Level NTC......................................................................16                             |
| 2.6.5                                                                                                                        | 2.6.5                                                                                                                                | ERTMS/ETCS Application Level 1 ...........................................................................18                         |
| 2.6.6                                                                                                                        | 2.6.6                                                                                                                                | ERTMS/ETCS Application Level 2 ...........................................................................21                         |
| 2.6.7                                                                                                                        | 2.6.7                                                                                                                                | ERTMS/ETCS Application Level 3 ...........................................................................23                         |
| 2.6.8                                                                                                                        | 2.6.8                                                                                                                                | Level transitions.......................................................................................................25           | [¶78]


---
<!-- pagina 14 -->

# 2.3 Introduction [¶79]

# 2.3.1 Scope and purpose [¶80]

- 2.3.1.1 The  present  chapter  gives  the  basic  description  of  the ERTMS/ETCS  system proposed to achieve technical interoperability. [¶81]


---
<!-- pagina 15 -->

# 2.4 System structure [¶82]

- 2.4.1.1 Due to the nature of the required functions, the ERTMS/ETCS system will have to be partly on the trackside and partly on board the trains. [¶83]

- 2.4.1.2 This defines two subsystems, the on-board subsystem and the trackside subsystem. [¶84]

- 2.4.1.3 The environment of ERTMS/ETCS system is composed of: [¶85]

- the train, which will then be considered in the train interface specification; [¶86]

- the driver, which will then be considered via the driver interface specification; [¶87]

-  other onboard interfaces (see architecture drawing in 2.5.3), [¶88]

- external  trackside  systems  (interlockings,  control  centres,  etc.),  for  which  no interoperability requirement will be established. [¶89]


---
<!-- pagina 16 -->

# 2.5 Subsystems [¶90]

# 2.5.1 Trackside subsystem [¶91]

- 2.5.1.1 Depending of the application level (see further sections), the trackside subsystem can be composed of: [¶92]

- balise [¶93]

- lineside electronic unit [¶94]

-  the radio communication network (GSM-R) [¶95]

- the Radio Block Centre (RBC) [¶96]

- Euroloop [¶97]

-  Radio infill unit [¶98]

- Key Management Centre (KMC) [¶99]

- Public Key Infrastructure (PKI) [¶100]

# 2.5.1.2 Balise [¶101]

- 2.5.1.2.1 The  balise  is  a  transmission  device  that  can  send  telegrams  to  the  on-board subsystem. [¶102]

- 2.5.1.2.2 The balise  is  based  on  the  existing  Eurobalise  specifications.  These  documents  are included in the frame of the ERTMS/ETCS specifications. [¶103]

- 2.5.1.2.3 The balises provides the up-link, i. e. the possibility to send messages from trackside to the on-board subsystem. [¶104]

- 2.5.1.2.4 The balises can provide fixed messages or, when connected to a lineside electronic unit, messages that can be changed. [¶105]

- 2.5.1.2.5 The balises will be organised in groups, each balise transmitting a telegram and the combination of all telegrams defining the message sent by the balise group. [¶106]

# 2.5.1.3 Lineside electronic unit [¶107]

- 2.5.1.3.1 The lineside electronic units are electronic devices, that generate telegrams to be sent by balises, on basis of information received from external trackside systems. [¶108]

# 2.5.1.4 Trackside radio communication network (GSM-R) [¶109]

- 2.5.1.4.1 The GSM-R radio communication network is used for the bi-directional exchange of messages between on-board subsystems and RBC or radio infill units. [¶110]

# 2.5.1.4.2 Intentionally deleted

# 2.5.1.5 RBC [¶111]


---
<!-- pagina 17 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶112]

- 2.5.1.5.1 The RBC is a computer-based system that elaborates messages to be sent to the train on  basis  of  information  received  from  external  trackside  systems  and  on  basis  of information exchanged with the on-board subsystems. [¶113]

- 2.5.1.5.2 The main objective of these messages is to provide movement authorities to allow the safe movement of trains on the Railway infrastructure area under the responsibility of the RBC. [¶114]

- 2.5.1.5.3 The interoperability requirements for the RBC are mainly related to the data exchange between the RBC and the on-board subsystem. [¶115]

# 2.5.1.6 Euroloop [¶116]

- 2.5.1.6.1 The Euroloop subsystem operates on Level 1 lines, providing signalling information in advance as regard to the next main signal in the train running direction. [¶117]

- 2.5.1.6.2 The Euroloop subsystem is composed of an on-board functionality and by one or more trackside parts. [¶118]

# 2.5.1.7 Radio infill Unit [¶119]

- 2.5.1.7.1 The  RADIO  INFILL  subsystem  operates  on  Level  1  lines,  providing  signalling information in advance as regard to the next main signal in the train running direction. [¶120]

- 2.5.1.7.2 The RADIO INFILL subsystem is composed of an on-board functionality and by one or more trackside parts (named RADIO INFILL Unit). [¶121]

# 2.5.1.8 KMC [¶122]

- 2.5.1.8.1 The role of the KMC is to manage the cryptographic keys, which are used to secure the EURORADIO communications between the ERTMS/ETCS entities (ERTMS/ETCS on-board equipments, RBCs and RIUs). [¶123]

# 2.5.1.9 PKI [¶124]

- 2.5.1.9.1 The role  of  the  PKI  is  to  manage  and  distribute  digital  certificates,  so  as  to  allow  a secure on-line distribution of cryptographic keys between KMCs and from a KMC to the ERTMS/ETCS entities (ERTMS/ETCS on-board equipments, RBCs and RIUs). [¶125]

# 2.5.2 On-board subsystem [¶126]

- 2.5.2.1 Depending of the application level (see further sections), the on-board subsystem can be composed of: [¶127]

- the ERTMS/ETCS on-board equipment; [¶128]

- the on-board part of the GSM-R radio system; [¶129]

# 2.5.2.2 ERTMS/ETCS on-board equipment [¶130]


---
<!-- pagina 18 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶131]

- 2.5.2.2.1 The ERTMS/ETCS on-board equipment is a computer-based system that supervises the movement of the train to which it belongs, on basis of information exchanged with the trackside subsystem. [¶132]

- 2.5.2.2.2 The  interoperability  requirements  for  the  ERTMS/ETCS  on-board  equipment  are related to the functionality and the data exchange between the trackside subsystems and  the  on-board  subsystem  and  to  the  functional  data  exchange  between  the  onboard subsystem and: [¶133]

- the driver; [¶134]

- the train; [¶135]

-  the onboard part of the existing national train control system(s). [¶136]

# 2.5.2.3 Onboard radio communication system (GSM-R) [¶137]

- 2.5.2.3.1 The  GSM-R  on-board  radio  system  is  used  for  the  bi-directional  exchange  of messages between on-board subsystem and RBC or radio infill unit. [¶138]

- 2.5.2.3.2 Intentionally deleted. [¶139]


---
<!-- pagina 19 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶140]

# 2.5.3 ERTMS/ETCS reference architecture [¶141]

![](images/image_0001.png)

# Figure 1: ERTMS/ETCS system and its interfaces [¶142]

- 2.5.3.1 Note: the entities inside the ERTMS/ETCS on-board equipment box are shown only to highlight the scope of the interfaces that are specified in the TSI CCS annex A. [¶143]


---
<!-- pagina 20 -->

# 2.6 Levels and transitions [¶144]

# 2.6.1 Introduction [¶145]

- 2.6.1.1 The different ERTMS/ETCS application levels (short: levels) are a way to express the possible operating relationships between track and train. Level definitions are related to  the  trackside  equipment  used,  to  the  way  trackside  information  reaches  the  onboard units and to which functions are processed in the trackside and in the on-board equipment respectively. [¶146]

- 2.6.1.2 Different  levels  have  been  defined  to  allow  each  individual  railway  administration  to select the appropriate ERTMS/ETCS  application trackside, according to their strategies, to their trackside infrastructure and to the required performance. Furthermore,  the different application levels permit the interfacing of individual signalling systems and train control systems to ERTMS/ETCS. [¶147]

- 2.6.1.3 For the purpose of a consistent specification a level 0 has been defined. This level is used  for  operation  on  non-equipped  (unfitted)  lines  or  on  lines  equipped  with  train control system(s) but operation under their supervision is currently not possible. [¶148]

# 2.6.2 Definitions [¶149]

- 2.6.2.1 A train equipped with ERTMS/ETCS on-board equipment always co-operates with the ERTMS/ETCS trackside equipment in a defined ERTMS/ETCS level. [¶150]

- 2.6.2.2 All transitions between levels are performed according to well-specified rules. [¶151]

- 2.6.2.3 ERTMS/ETCS can be configured to operate in one of the following application levels: [¶152]

-  ERTMS/ETCS Level 0 (train equipped with ERTMS/ETCS operating on a line not equipped with any train control system (ERTMS/ETCS or national system) or on a line  equipped  with  ERTMS/ETCS  and/or  national  system(s)  but  operation  under their supervision is currently not possible) [¶153]

-  ERTMS/ETCS Level NTC (train equipped with ERTMS/ETCS operating on a line equipped with a national system) [¶154]

-  ERTMS/ETCS Application Level 1 with or without infill transmission (train equipped with  ERTMS/ETCS  operating  on  a  line  equipped  with  Eurobalises  and  optionally Euroloop or Radio infill) [¶155]

-  ERTMS/ETCS Application Level 2 (train equipped with ERTMS/ETCS operating on a  line  controlled  by  a  Radio  Block  Centre  and  equipped  with  Eurobalises  and Euroradio) with train position and train integrity proving performed by the trackside [¶156]

-  ERTMS/ETCS Application Level 3 (similar to level 2 but with train position and train integrity supervision based on information received from the train) [¶157]


---
<!-- pagina 21 -->

- 2.6.2.4 It is possible to superimpose several application levels in parallel on the same track, for example  to  run  trains  without  train  integrity  device  in  level  2  and  in  parallel  trains equipped with train integrity device in level 3. Other examples might be a station which is shared by trains arriving over level 1 and level 2 lines (junctions) or parallel operation of a national system with ERTMS/ETCS. Mixed levels are supported. [¶158]

- 2.6.2.5 Intentionally deleted. [¶159]

- 2.6.2.6 Intentionally deleted. [¶160]

- 2.6.2.7 It  is  possible  to  transmit  information  not  intended  for  ERTMS/ETCS  but  for  other systems over the ERTMS/ETCS transmission channels. This information is not used by ERTMS/ETCS. [¶161]


---
<!-- pagina 22 -->

# 2.6.3 ERTMS/ETCS Application Level 0 [¶162]

# 2.6.3.1 General description [¶163]

- 2.6.3.1.1 Level 0 covers operation of ETCS equipped trains on lines not equipped with ETCS or national  systems  or  on  lines  where  trackside  ERTMS/ETCS  infrastructure  and/or national  systems  may  exist  but  operation  under  their  supervision  is  currently  not possible (e.g. commissioning or on-board/trackside failed components). [¶164]

- 2.6.3.1.2 In  Level  0  it  is  authorized  to  operate  trains  without  any  train  control  system  and therefore  line  side  optical  signals  or  other  means  of  signalling  are  used  to  give movement authorities to the driver. [¶165]

- 2.6.3.1.3 ERTMS/ETCS on-board equipment provides no supervision except of  the  maximum design speed of a train and maximum speed permitted in unfitted areas. [¶166]

- 2.6.3.1.4 Train detection and  train integrity supervision are performed  by  the trackside equipment of the underlying signalling system (interlocking, track circuits etc.) and are outside the scope of ERTMS/ETCS. [¶167]

- 2.6.3.1.5 Level  0  uses  no  track-train  transmission  except  Eurobalises  to  announce/command level  transitions.  Eurobalises  therefore  still  have  to  be  read.  No  balise  data  except certain special commands are interpreted. [¶168]

- 2.6.3.1.6 No supervisory information is indicated on the DMI except the train speed. Train data has  to  be  entered  in  order  not  to  have  to  stop  a  train  at  a  level  transition  to ERTMS/ETCS equipped area and to supervise maximum train speed. [¶169]

![](images/image_0002.png)

# Figure 2: ERTMS/ETCS Application Level 0 [¶170]

# 2.6.3.2 Summary of characteristics of Application Level 0 [¶171]

# 2.6.3.2.1 Trackside equipment: [¶172]


---
<!-- pagina 23 -->

-  No ERTMS/ETCS trackside equipment is used except for Eurobalises to announce level transitions and other specific commands. [¶173]

- 2.6.3.2.2 Main ERTMS/ETCS trackside functions: [¶174]

-  None. [¶175]

- 2.6.3.2.3 On-board equipment: [¶176]

-  Onboard equipment with Eurobalise transmission. [¶177]

- 2.6.3.2.4 Main ERTMS/ETCS on-board functions: [¶178]

-  Supervision of maximum train speed. [¶179]

-  Supervision of maximum speed permitted in an unfitted area. [¶180]

-  Reading of Eurobalises to detect level transitions and certain special commands. All other messages are rejected. [¶181]

-  No cab signalling. [¶182]


---
<!-- pagina 24 -->

# 2.6.4 ERTMS/ETCS Application Level NTC [¶183]

# 2.6.4.1 General description [¶184]

- 2.6.4.1.1 Level  NTC  is  used  to  run  ERTMS/ETCS  equipped  trains  on  lines  equipped  with national train control and speed supervision systems. [¶185]

- 2.6.4.1.2 Train  control  information  generated  trackside  by  the  national  train  control  system  is transmitted  to  the  train  via  the  communication  channels  of  the  underlying  national system. [¶186]

- 2.6.4.1.3 Note: Lineside optical signals might be necessary or not, depending on the performance and functionality of the underlying systems. [¶187]

- 2.6.4.1.4 Intentionally deleted. [¶188]

- 2.6.4.1.5 The  achievable  level  of  supervision  is  similar  to  the  one  provided  by  the  underlying national systems. [¶189]

- 2.6.4.1.6 Train detection and train integrity supervision are performed by equipment external to ERTMS/ETCS. [¶190]

- 2.6.4.1.7 Level NTC uses no ERTMS/ETCS track-train information except to announce/command  level transitions and specific commands  related to balise transmission. Eurobalises therefore still have to be read. [¶191]

- 2.6.4.1.8 The information displayed to the driver depends on the functionality of the underlying national  system.  The  active  national  system  is  indicated  to  the  driver  as  part  of  that information. Full train data has to be entered in order not to have to stop a train at a level transition position and to supervise maximum train speed. [¶192]

- 2.6.4.1.9 A combination of national systems can be regarded as one NTC level. [¶193]

- 2.6.4.1.10  Depending  on  the  functionality  and  the  configuration  of  the  specific  national  system installed onboard, the ERTMS/ETCS Onboard system may need to be interfaced to it, in order to perform the transitions from/to the national system and/or in order to give access to ERTMS/ETCS Onboard resources (e.g. DMI). This can be achieved through a device called an STM (Specific Transmission Module) using a standardised interface. [¶194]

- 2.6.4.1.11  Intentionally deleted. [¶195]


---
<!-- pagina 25 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶196]

![](images/image_0003.png)

# Figure 3: ERTMS/ETCS Application Level NTC [¶197]

# 2.6.4.2 Summary of characteristics of Application Level NTC [¶198]

- 2.6.4.2.1 Trackside equipment: [¶199]

-  Level  NTC  uses  the  track-train  transmission  system  from  an  underlying  national system, which is not part of ERTMS/ETCS. [¶200]

-  For level transition purposes Eurobalises are used. [¶201]

- 2.6.4.2.2 Main ERTMS/ETCS trackside functions: [¶202]

-  None. [¶203]

- 2.6.4.2.3 On-board equipment: [¶204]

-  Onboard equipment with Eurobalise transmission. [¶205]

-  Onboard part of the national system. [¶206]

- 2.6.4.2.4 Main ERTMS/ETCS on-board function: [¶207]

-  No train supervision, it is fully handed over to the national system. [¶208]

-  Reading of Eurobalises to detect level transitions and certain special commands. All other messages are rejected. [¶209]

-  Management of the national system through STM, in case the ERTMS/ETCS onboard equipment is interfaced to the national system through an STM. [¶210]


---
<!-- pagina 26 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶211]

-  No cab signalling. [¶212]

# 2.6.5 ERTMS/ETCS Application Level 1 [¶213]

# 2.6.5.1 General description [¶214]

- 2.6.5.1.1 ERTMS/ETCS Level 1 is a spot transmission based train control system to be used as an overlay on an underlying signalling system. [¶215]

- 2.6.5.1.2 Movement  authorities  are  generated  trackside  and  are  transmitted  to  the  train  via Eurobalises. [¶216]

- 2.6.5.1.3 ERTMS/ETCS Level 1 provides a continuous speed supervision  system,  which  also protects against overrun of the authority. [¶217]

- 2.6.5.1.4 Train detection and  train integrity supervision are performed  by  the trackside equipment of the underlying signalling system (interlocking, track circuits etc.) and are outside the scope of ERTMS/ETCS. [¶218]

- 2.6.5.1.5 Level 1 is based on Eurobalises as spot transmission devices. [¶219]

- 2.6.5.1.6 The trackside equipment does not know the train to which it sends information. [¶220]

- 2.6.5.1.7 If  in  level  1  a  lineside  signal  clears,  an  approaching  train  can  not  receive  this information until it passes the Eurobalise group at that signal. The driver therefore has to  observe  the  lineside  signal  to  know  when  to  proceed.  The  train  has  then  to  be permitted  to  approach  the  stopping  location  below  a  maximum  permitted  release speed. [¶221]

- 2.6.5.1.8 Additional Eurobalises can be placed between distant and main signals to transmit infill information, the train will receive new information before reaching the signal. [¶222]

- 2.6.5.1.9 Note: Lineside signals are required in level 1 applications, except if semi-continuous infill is provided. [¶223]

- 2.6.5.1.10  Semi-continuous infill can be provided using Euroloop or radio infill. In this case, the on-board system will  be  able  to  show  new  information  to  the  driver  as  soon  as  it  is available and even at standstill. [¶224]

- 2.6.5.1.11  Euroloop or radio infill  can  improve  the  safety  of  a  level  1  system  as  they  allow  the operation without release speed. [¶225]


---
<!-- pagina 27 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶226]

![](images/image_0004.png)

Figure 4: ERTMS/ETCS Application Level 1 without infill function [¶227]

![](images/image_0005.png)

Figure 5: ERTMS/ETCS Application Level 1 with infill function by Euroloop or Radio infill [¶228]


---
<!-- pagina 28 -->

# 2.6.5.2 Summary of characteristics of Application Level 1 [¶229]

- 2.6.5.2.1 Trackside equipment: [¶230]

-  Eurobalises for spot transmission from track to train. [¶231]

-  Eurobalises must be able to transmit variable information. [¶232]

-  Semi continuous infill transmission by using Euroloop or radio infill is optional. [¶233]

- 2.6.5.2.2 Main ERTMS/ETCS trackside function: [¶234]

-  Determine movement authorities according to the underlying signalling system. [¶235]

-  Transmit movement authorities and track description data to the train. [¶236]

- 2.6.5.2.3 On-board equipment: [¶237]

-  Onboard equipment with Eurobalise transmission. [¶238]

-  Euroloop transmission if infill by Euroloop is required. [¶239]

-  Radio infill transmission if infill by radio is required. [¶240]

- 2.6.5.2.4 Main ERTMS/ETCS on-board function: [¶241]

-  Reception of  movement authority and track description related to the transmitting balise. [¶242]

-  Selection  of  the  most  restrictive  value  of  the  different  speeds  permitted  at  each location ahead. [¶243]

-  Calculation of a dynamic speed profile taking into account the train running/braking characteristics which are known on-board and the track description data. [¶244]

-  Comparison of  the  train  speed  with  the  permitted  speed  and  commanding  of  the brake application if necessary. [¶245]

-  Cab signalling to the driver. [¶246]


---
<!-- pagina 29 -->

# 2.6.6 ERTMS/ETCS Application Level 2 [¶247]

# 2.6.6.1 General description [¶248]

- 2.6.6.1.1 ERTMS/ETCS  Level  2  is  a  radio  based  train  control  system  which  is  used  as  an overlay on an underlying signalling system. [¶249]

- 2.6.6.1.2 Movement  authorities  are  generated  trackside  and  are  transmitted  to  the  train  via Euroradio. [¶250]

- 2.6.6.1.3 ERTMS/ETCS Level 2 provides a continuous speed supervision  system,  which  also protects against overrun of the authority. [¶251]

- 2.6.6.1.4 Train detection and  train integrity supervision are performed  by  the trackside equipment of the underlying signalling system (interlocking, track circuits etc.) and are outside the scope of ERTMS/ETCS. [¶252]

- 2.6.6.1.5 Level 2 is based on Euroradio for track to train communication and on Eurobalises as spot transmission devices mainly for location referencing. [¶253]

- 2.6.6.1.6 The  trackside  radio  block  centre  which  provides  the  information  to  the  trains  knows each  ERTMS/ETCS  controlled  train  individually  by  the  ERTMS/ETCS  identity  of  its leading ERTMS/ETCS on-board equipment. [¶254]

- 2.6.6.1.7 Note: Lineside signals can be suppressed in Level 2. [¶255]

![](images/image_0006.png)

Figure 6: ERTMS/ETCS Application Level 2 [¶256]


---
<!-- pagina 30 -->

# 2.6.6.2 Summary of characteristics of Application Level 2 [¶257]

- 2.6.6.2.1 Trackside equipment: [¶258]

-  Radio block centre. [¶259]

-  Euroradio for bi-directional track-train communication. [¶260]

-  Eurobalises mainly for location referencing. [¶261]

- 2.6.6.2.2 Main ERTMS/ETCS trackside function: [¶262]

-  Knowing each train equipped with and running under ERTMS/ETCS within an RBC area by its ERTMS/ETCS identity. [¶263]

-  Following each ERTMS/ETCS controlled train's location within an RBC area. [¶264]

-  Determine movement authorities according to the underlying signalling system for each train individually. [¶265]

-  Transmit movement authorities and track description  to each train individually. [¶266]

-  Handing over of train control between different RBC's at the RBC-RBC borders. [¶267]

- 2.6.6.2.3 On-board equipment: [¶268]

-  Onboard equipment with Eurobalise and Euroradio transmissions. [¶269]

- 2.6.6.2.4 Main ERTMS/ETCS on-board function: [¶270]

-  The train reads Eurobalises and sends its position relative to the detected balises to the radio block centre. [¶271]

-  The train  receives  a  movement  authority  and  the  track  description    via  Euroradio relating to a balise. [¶272]

-  Selection  of  the  most  restrictive  value  of  the  different  speeds  permitted  at  each location ahead. [¶273]

-  Calculation of a dynamic speed profile taking into account the train running/braking characteristics which are known on-board and the track description data. [¶274]

-  Comparison of  the  train  speed  with  the  permitted  speed  and  commanding  of  the brake application if necessary. [¶275]

-  Cab signalling to the driver. [¶276]


---
<!-- pagina 31 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶277]

# 2.6.7 ERTMS/ETCS Application Level 3 [¶278]

# 2.6.7.1 General description [¶279]

- 2.6.7.1.1 ERTMS/ETCS Level 3 is a radio based train control system. [¶280]

- 2.6.7.1.2 Movement  authorities  are  generated  trackside  and  are  transmitted  to  the  train  via Euroradio. [¶281]

- 2.6.7.1.3 ERTMS/ETCS Level 3 provides a  continuous  speed  supervision  system,  which  also protects against overrun of the authority. [¶282]

- 2.6.7.1.4 Train position and train integrity supervision are performed by the trackside radio block centre  in  co-operation  with  the  train  (which  sends  position  reports  and  train  integrity information). [¶283]

- 2.6.7.1.5 Level 3 is based on Euroradio for track to train communication and on Eurobalises as spot transmission devices mainly for location referencing. [¶284]

- 2.6.7.1.6 The  trackside  radio  block  centre  which  provides  the  information  to  the  trains  knows each train individually  by  the  ERTMS/ETCS identity of its leading ERTMS/ETCS onboard equipment. [¶285]

- 2.6.7.1.7 Note: Lineside signals are not foreseen to be used when operating in Level 3. [¶286]

![](images/image_0007.png)

# Figure 7: ERTMS/ETCS Application Level 3 [¶287]

# 2.6.7.2 Summary of characteristics of Application Level 3 [¶288]


---
<!-- pagina 32 -->

- 2.6.7.2.1 Trackside equipment: [¶289]

-  Radio block centre. [¶290]

-  Euroradio for bi-directional track-train communication. [¶291]

-  Eurobalises for mainly location referencing. [¶292]

- 2.6.7.2.2 Main ERTMS/ETCS trackside function: [¶293]

-  Knowing each train within an RBC area by its ERTMS/ETCS identity. [¶294]

-  Following each trains location within an RBC area. [¶295]

-  Route locking and route releasing based on information received from the trains. [¶296]

-  Determine movement authorities for each train individually. [¶297]

-  Transmit movement authorities and track description  to each train individually. [¶298]

-  Handing over of train control between different RBC's at the RBC-RBC borders. [¶299]

- 2.6.7.2.3 On-board equipment: [¶300]

-  Onboard equipment with Eurobalise and Euroradio transmissions. [¶301]

-  Train integrity proving system. [¶302]

- 2.6.7.2.4 Main ERTMS/ETCS on-board functions: [¶303]

-  The train reads Eurobalises and sends its position relative to the detected balises to the radio block centre. [¶304]

-  The train monitors train integrity (external function, not part of ERTMS/ETCS) and sends this information to the radio block centre. [¶305]

-  The train  receives  a  movement  authority  and  the  track  description    via  Euroradio relating to a balise. [¶306]

-  Selection  of  the  most  restrictive  value  of  the  different  speeds  permitted  at  each location ahead. [¶307]

-  Calculation of a dynamic speed profile, taking into account the train running/braking characteristics which are known on-board and the track description data. [¶308]

-  Comparison of  the  train  speed  with  the  permitted  speed  and  commanding  of  the brake application if necessary. [¶309]

-  Cab signalling to the driver. [¶310]


---
<!-- pagina 33 -->

# 2.6.8 Level transitions [¶311]

- 2.6.8.1 An ERTMS/ETCS equipment which is not isolated always operates in one of the above described  levels.  All  transitions  between  these  levels  are  performed  according  to defined functions and procedures. [¶312]

- 2.6.8.2 Additional national functions and rules which might be used by an individual railway to for  example  prevent  not  equipped  trains  from  entering  a  level  2/3  area  are  not specified here and have to be implemented outside ERTMS/ETCS. [¶313]

- 2.6.8.3 The following table shows all possible transitions (marked with Grey): [¶314]

[¶315]
| to   | 0   | NTC   | 1   | 2   | 3   |
|------|-----|-------|-----|-----|-----|
| from |     |       |     |     |     |
| 0    |     |       |     |     |     |
| NTC  |     | a)    |     |     |     |
| 1    |     |       |     |     |     |
| 2    |     |       |     | b)  |     |
| 3    |     |       |     |     | b)  |

# Table 1: Possible level transitions. [¶316]

- Transitions  between  level  NTC  and  level  NTC  describe  the  switching  from  one national system to another national system. [¶317]

- Transitions  between  level  2  and  level  2  respectively  between  level  3  and  level  3 describe the handover between RBC's. [¶318]


---
<!-- pagina 34 -->

[¶319]
| ERTMS/ETCS                                             | ERTMS/ETCS                                             |
|--------------------------------------------------------|--------------------------------------------------------|
| System Requirements Specification Chapter 3 Principles | System Requirements Specification Chapter 3 Principles |
| REF :                                                  | SUBSET-026-3                                           |
| ISSUE :                                                | 3.6.0                                                  |
| DATE :                                                 | 13/05/2016                                             |


---
<!-- pagina 35 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶320]

# 3.1 Modification History [¶321]

[¶322]
| Issue Number Date   | Section Number                          | Modification / Description                                                                              | Author/Editor      |
|---------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------|
| 1.0.1 990307        | All                                     | Merge of Basic + Detailed Principles Removing redundant material, correcting text and adding proposals. | HE                 |
| 1.1.0 990423        | All                                     | Class P Official Issue                                                                                  | HE                 |
| 1.1.1 990521        | All                                     | Corrections after UNISIG review.                                                                        | KL                 |
| 1.1.2 990713        | All                                     | Additional functions for class 1 and changes related to these functions in other parts                  | KL                 |
| 1.1.3 990722        | All                                     | Changes according to review of version 1.1.2                                                            | KL                 |
| 1.1.4 990729        | All                                     | Editorial corrections, finalisation meeting Stuttgart 990729                                            | HE                 |
| 1.2.0 990730        | Version number                          | Release version                                                                                         | HE                 |
| 1.3.0 991201        | All                                     | Corrections and new functions according to ECSAG and UNISIG comments                                    | KL                 |
| 1.3.1 991217        | All                                     | Corrections after UNISIG review 15 December 99                                                          | KL                 |
| 2.0.0 991222        | Minor editing                           | Release Version                                                                                         | Ch. Frerichs (ed.) |
| 2.0.1 000921        | All                                     | Corrections after UNISIG review 15 June 00                                                              | KL                 |
| 2.1.0 001017        | Most                                    | Corrections after UNISIG review 11 October 00                                                           | KL                 |
| 2.2.0 010108        | Section 3.18.4.6.6 - 3.18.4.6.8 removed | Changes as decided on Steering Committee meeting 13 December 2000 (changes from 2.0.0                   | KL                 |


---
<!-- pagina 36 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶323]

[¶324]
| 2.2.2 020201            | Refer to document: SUBSET-026 Corrected Paragraphs, Issue 2.2.2                                                                                                                                               | KL      |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| 2.2.4 SG checked 040528 | Including all CLRs agreed with the EEIG (see 'List of CLRs agreed with EEIG for SRS v2.2.4' dated 28/05/04) Affected clauses see change marks                                                                 | H. Kast |
| 2.2.5 210105            | Incorporation of solution proposal for CLR 007 with EEIG users group comments Corrections according to erratum list agreed in SG meeting 170105                                                               | AH      |
| 2.2.6 050301            | Including all CLRs being in state 'EEIG pending' as per list of CLRs extracted on 28/01/05.                                                                                                                   | OG      |
| 2.2.7 220705            | Including all CLRs extracted from 'CR- Report_10.6.05-by number.rtf' and mentioned in column 2.2.7 in 'CR status 13.6.05.xls' 22/07/05 Changes for CR 126 included (HK)                                       | OG      |
| 2.2.8 211105            | Change marks cleaned up and updated according to last CRs decisions (including split of CRs7&126)                                                                                                             | OG      |
| 2.2.9 24/02/06          | Including all CRs that are classified as 'IN' as per SUBSET-108 version 1.0.0 Removal of all CRs that are not classified as 'IN' as per SUBSET-108 version 1.0.0, with the exception of CRs 63,98,120,158,538 | OG      |
| 2.3.0 24/02/06          | Release version                                                                                                                                                                                               | HK      |
| 2.3.1 12/06/06          |                                                                                                                                                                                                               | OG      |
| 2.3.2 17/03/08          | Including all CRs that are classified as 'IN' as per SUBSET-108 version 1.2.0 and all CRs that are in state 'Analysis completed' according to ERA CCM                                                         | AH      |
| 2.9.1 06/10/08          | Including all enhancement CR's retained for baseline 3 and all other error CR's For editorial reasons, the following CR's are also included: CR656, CR804, CR821                                              | AH      |
| 3.0.0 13/12/08          | Release version                                                                                                                                                                                               | AH      |


---
<!-- pagina 37 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶325]

[¶326]
| 3.0.1 22/12/09   | Including the results of the editorial review of the SRS 3.0.0 and the other error CR's that are in state 'Analysis completed' according to ERA CCM   | AH   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| 3.1.0 22/02/10   | Release version                                                                                                                                       | AH   |
| 3.1.1 08/11/10   | Including all CR's that are in state 'Analysis completed' according to ERA CCM, plus CR731, 972 and 1000.                                             | AH   |
| 3.2.0 22/12/10   | Release version                                                                                                                                       | AH   |
| 3.2.1 13/12/11   | Including all CR's that are in state 'Analysis completed' according to ERA CCM, plus CR772                                                            | AH   |
| 3.3.0 07/03/12   | Baseline 3 release version                                                                                                                            | AH   |
| 3.3.1 04/04/14   | CR's 944, 1109,1124, 1127, 1149, 1150, 1183, 1185                                                                                                     | OG   |
| 3.3.2 23/04/14   | Baseline 3 1 st maintenance pre-release version                                                                                                       | OG   |
| 3.3.3 06/05/14   | CR 1223 Baseline 3 1 st maintenance 2 nd pre-release version                                                                                          | OG   |
| 3.4.0 12/05/14   | Baseline 3 1 st maintenance release version                                                                                                           | OG   |
| 3.4.1 23/06/15   | CR's 239, 852, 1014, 1117, 1163, 1164, 1172, 1260                                                                                                     | OG   |
| 3.4.2 17/11/15   | CR's 299, 933, 1084, 1086, 1087, 1107, 1152, 1163 (update), 1184, 1190, 1197, 1249, 1254, 1262, 1265, 1266, 1273, 1277                                | OG   |
| 3.4.3 16/12/15   | CR1283 plus update due to overall CR consolation phase                                                                                                | OG   |
| 3.5.0 18/12/15   | Baseline 3 2 nd release version as recommended to EC (see ERA-REC-123-2015/REC)                                                                       | OG   |
| 3.5.1 28/04/16   | CR 1249 reopening following RISC #75                                                                                                                  | OG   |
| 3.6.0 13/05/16   | Baseline 3 2 nd release version                                                                                                                       | AH   |


---
<!-- pagina 38 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶327]

# 3.2 Table of Contents [¶328]

| 3.1                                                                                                                            | Modification History...........................................................................................................2     | Modification History...........................................................................................................2   |
|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| 3.2                                                                                                                            | Table of Contents..............................................................................................................5     |                                                                                                                                    |
| 3.3                                                                                                                            | Introduction.......................................................................................................................9 |                                                                                                                                    |
| 3.3.1                                                                                                                          | Scope and purpose....................................................................................................9               |                                                                                                                                    |
| 3.4 Balise configuration and linking.........................................................................................9 | 3.4 Balise configuration and linking.........................................................................................9       |                                                                                                                                    |
| 3.4.1                                                                                                                          | Balise Configurations - Balise Group Definition.........................................................9                            |                                                                                                                                    |
| 3.4.2                                                                                                                          | Balise Co-ordinate System.........................................................................................9                  |                                                                                                                                    |
| 3.4.3                                                                                                                          | Balise Information Types and Usage                                                                                                   | .......................................................................14                                                          |
| 3.4.4                                                                                                                          | Linking .....................................................................................................................14      |                                                                                                                                    |
| 3.5 Management of Radio Communication ...........................................................................17            | 3.5 Management of Radio Communication ...........................................................................17                  |                                                                                                                                    |
| 3.5.2                                                                                                                          | General....................................................................................................................17        |                                                                                                                                    |
| 3.5.3                                                                                                                          | Establishing a communication session.....................................................................17                          |                                                                                                                                    |
| 3.5.4                                                                                                                          | Maintaining a communication session......................................................................21                          |                                                                                                                                    |
| 3.5.5                                                                                                                          | Terminating a communication session.....................................................................22                           |                                                                                                                                    |
| 3.5.6                                                                                                                          | Registering to the Radio Network.............................................................................23                      |                                                                                                                                    |
| 3.5.7                                                                                                                          | Safe Radio Connection Indication ............................................................................24                      |                                                                                                                                    |
| 3.6                                                                                                                            | Location Principles, Train Position and Train Orientation ................................................26                         |                                                                                                                                    |
| 3.6.1                                                                                                                          | General....................................................................................................................26        |                                                                                                                                    |
| 3.6.2                                                                                                                          | Location of Data Transmitted to the On-Board Equipment.......................................28                                      |                                                                                                                                    |
| 3.6.3                                                                                                                          | Validity direction of transmitted Information..............................................................31                        |                                                                                                                                    |
| 3.6.4                                                                                                                          | Train Position Confidence Interval and Relocation...................................................34                               |                                                                                                                                    |
| 3.6.5                                                                                                                          | Position Reporting to the RBC.................................................................................38                     |                                                                                                                                    |
| 3.6.6                                                                                                                          | Geographical position reporting                                                                                                      | ...............................................................................42                                                  |
| 3.7                                                                                                                            | Completeness of data for safe train movement...............................................................44                        |                                                                                                                                    |
| 3.7.1                                                                                                                          | Completeness of data..............................................................................................44                 |                                                                                                                                    |
| 3.7.2                                                                                                                          | Responsibility for completeness of information                                                                                       | ........................................................45                                                                         |
| 3.7.3                                                                                                                          | Extension, replacement of track description and linking information ........................46                                       |                                                                                                                                    |
| 3.8                                                                                                                            | Movement authority.........................................................................................................48        |                                                                                                                                    |
| 3.8.1                                                                                                                          | Characteristics of a MA............................................................................................48                |                                                                                                                                    |
| 3.8.2                                                                                                                          | MA request to the RBC............................................................................................49                  |                                                                                                                                    |
| 3.8.3                                                                                                                          | Structure of a Movement Authority (MA) ..................................................................50                          |                                                                                                                                    |
| 3.8.4                                                                                                                          | Use of the MA on board the train .............................................................................53                     |                                                                                                                                    |
| 3.8.5                                                                                                                          | MA Update...............................................................................................................56           |                                                                                                                                    |
| 3.8.6                                                                                                                          | Co-operative shortening of MA (Level 2 and 3 only).................................................63                                |                                                                                                                                    |
| 3.9 Means to transmit Infill information (Level 1                                                                              | only)                                                                                                                                | ...........................................................64                                                                      | [¶329]


---
<!-- pagina 39 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶330]

| 3.9.1                                                                                                                                | General....................................................................................................................64        |                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| 3.9.2                                                                                                                                | Infill by loop..............................................................................................................64       |                                                                                                                 |
| 3.9.3                                                                                                                                | Infill by radio.............................................................................................................65       |                                                                                                                 |
| 3.10 Emergency Messages.................................................................................................68           | 3.10 Emergency Messages.................................................................................................68           |                                                                                                                 |
| 3.10.1                                                                                                                               | General....................................................................................................................68        |                                                                                                                 |
| 3.10.2                                                                                                                               | Emergency Stop                                                                                                                       | ......................................................................................................69        |
| 3.10.3                                                                                                                               | Revocation of an Emergency Message....................................................................69                             |                                                                                                                 |
| 3.11 Static Speed Restrictions and Gradients .....................................................................70                 | 3.11 Static Speed Restrictions and Gradients .....................................................................70                 |                                                                                                                 |
| 3.11.1                                                                                                                               | Introduction..............................................................................................................70         |                                                                                                                 |
| 3.11.2                                                                                                                               | Definition of Static Speed Restriction                                                                                               | .......................................................................70                                       |
| 3.11.3                                                                                                                               | Static Speed Profile (SSP).......................................................................................71                  |                                                                                                                 |
| 3.11.4                                                                                                                               | Axle load Speed Profile............................................................................................73                |                                                                                                                 |
| 3.11.5                                                                                                                               | Temporary Speed Restrictions.................................................................................73                      |                                                                                                                 |
| 3.11.6                                                                                                                               | Signalling related speed restrictions.........................................................................74                     |                                                                                                                 |
| 3.11.7                                                                                                                               | Mode related speed restrictions                                                                                                      | ...............................................................................75                               |
| 3.11.8                                                                                                                               | Train related speed restriction..................................................................................75                  |                                                                                                                 |
| 3.11.9                                                                                                                               | LX speed restriction                                                                                                                 | .................................................................................................75             |
| 3.11.10                                                                                                                              | Override function related Speed Restriction                                                                                          | .........................................................76                                                     |
| 3.11.11                                                                                                                              | Speed restriction to ensure permitted braking distance                                                                               | ........................................76                                                                      |
| 3.11.12                                                                                                                              | Gradients..............................................................................................................79            |                                                                                                                 |
| 3.12 Other Profiles ..............................................................................................................80 | 3.12 Other Profiles ..............................................................................................................80 |                                                                                                                 |
| 3.12.1                                                                                                                               | Track Conditions......................................................................................................80             |                                                                                                                 |
| 3.12.2                                                                                                                               | Route Suitability                                                                                                                    | .......................................................................................................82       |
| 3.12.3                                                                                                                               | Text Transmission....................................................................................................83              |                                                                                                                 |
| 3.12.4                                                                                                                               | Mode profile                                                                                                                         | .............................................................................................................86 |
| 3.12.5                                                                                                                               | Level Crossings                                                                                                                      | .......................................................................................................86       |
| 3.13                                                                                                                                 | Speed and distance monitoring ...................................................................................87                  |                                                                                                                 |
| 3.13.1                                                                                                                               | Introduction..............................................................................................................87         |                                                                                                                 |
| 3.13.2                                                                                                                               | Inputs for speed and distance monitoring                                                                                             | ................................................................88                                              |
| 3.13.3                                                                                                                               | Conversion Models                                                                                                                    | ................................................................................................101             |
| 3.13.4                                                                                                                               | Acceleration / Deceleration due to gradient............................................................103                           |                                                                                                                 |
| 3.13.5                                                                                                                               | Determination of locations without special brake contribution and with                                                               | reduced                                                                                                         |
| adhesion conditions .............................................................................................................105 | adhesion conditions .............................................................................................................105 |                                                                                                                 |
| 3.13.6                                                                                                                               | Calculation of the deceleration and brake build up time                                                                              | .........................................105                                                                    |
| 3.13.7                                                                                                                               | Determination of Most Restrictive Speed Profile (MRSP).......................................112                                     |                                                                                                                 |
| 3.13.8                                                                                                                               | Determination of targets and brake deceleration curves ........................................112                                   |                                                                                                                 |
| 3.13.9                                                                                                                               | Supervision limits                                                                                                                   | ...................................................................................................115          | [¶331]


---
<!-- pagina 40 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶332]

| 3.13.10             | Speed and distance monitoring commands........................................................131                              |                                                                                                                          |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 3.13.11             | Perturbation location...........................................................................................150            |                                                                                                                          |
| 3.14                | Brake Command Handling and Protection against Undesirable Train Movement......152                                              |                                                                                                                          |
| 3.14.1              | Brake Command Handling.....................................................................................152                 |                                                                                                                          |
| 3.14.2              | Roll Away Protection..............................................................................................153          |                                                                                                                          |
| 3.14.3              | Reverse Movement Protection...............................................................................154                  |                                                                                                                          |
| 3.14.4              | Standstill supervision                                                                                                         | .............................................................................................154                         |
| 3.15                | Special functions .......................................................................................................154   |                                                                                                                          |
| 3.15.1              | RBC/RBC Handover                                                                                                               | ..............................................................................................154                        |
| 3.15.2              | Handling of Trains with Non Leading Engines........................................................159                         |                                                                                                                          |
| 3.15.3              | Splitting/joining.......................................................................................................159    |                                                                                                                          |
| 3.15.4              | Reversing of movement direction...........................................................................159                  |                                                                                                                          |
| 3.15.5              | Track ahead free....................................................................................................161        |                                                                                                                          |
| 3.15.6              | Handling of National Systems................................................................................161                |                                                                                                                          |
| 3.15.7              | Tolerance of Big Metal Mass..................................................................................162               |                                                                                                                          |
| 3.15.8              | Cold Movement Detection......................................................................................162               |                                                                                                                          |
| 3.15.9              | Virtual Balise Cover................................................................................................163        |                                                                                                                          |
| 3.15.10             | Advance display of route related information......................................................163                          |                                                                                                                          |
| 3.16                | Data Consistency ......................................................................................................164     |                                                                                                                          |
| 3.16.1              | Criteria of consistency............................................................................................164         |                                                                                                                          |
| 3.16.2              | Balises                                                                                                                        | ...................................................................................................................164   |
| 3.16.3              | Radio                                                                                                                          | .....................................................................................................................169 |
| 3.16.4              | Error reporting to RBC...........................................................................................172           |                                                                                                                          |
| 3.17                | System Version Management....................................................................................173               |                                                                                                                          |
| 3.17.1              | Introduction............................................................................................................173    |                                                                                                                          |
| 3.17.2              | Determination of the operated system version                                                                                   | .......................................................173                                                               |
| 3.17.3              | Handling of trackside data in relation to system version.........................................174                           |                                                                                                                          |
| 3.18                | System Data..............................................................................................................176   |                                                                                                                          |
| 3.18.1              | Fixed Values                                                                                                                   | ..........................................................................................................176            |
| 3.18.2              | National / Default Values........................................................................................176           |                                                                                                                          |
| 3.18.3              | Train Data..............................................................................................................178    |                                                                                                                          |
| 3.18.4              | Additional Data.......................................................................................................180      |                                                                                                                          |
| 3.18.5              | Date and Time                                                                                                                  | .......................................................................................................182               |
| 3.18.6              | Data view...............................................................................................................183    |                                                                                                                          |
| 3.19                | Intentionally deleted...................................................................................................183    |                                                                                                                          |
| 3.20                | Juridical Data.............................................................................................................183 |                                                                                                                          |
| Appendix to Chapter | Appendix to Chapter                                                                                                            | 3............................................................................................................184         | [¶333]


---
<!-- pagina 41 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶334]

| A.3.1   | List of Fixed Value Data.........................................................................................184   |
|---------|------------------------------------------------------------------------------------------------------------------------|
| A.3.2   | List of National / Default Data ................................................................................185    |
| A.3.3   | Handling of information received from trackside ....................................................187                |
| A.3.4   | Handling of Accepted and Stored Information in specific Situations.......................189                           |
| A.3.5   | Handling of Actions in Specific Situations ..............................................................194           |
| A.3.6   | Deletion of accepted and stored information when used........................................195                       |
| A.3.7   | Calculation of the basic deceleration......................................................................196         |
| A.3.8   | Calculation of the emergency brake equivalent time..............................................197                    |
| A.3.9   | Calculation of the full service brake equivalent time...............................................198                |
| A.3.10  | Service brake feedback .........................................................................................199    |
| A.3.11  | Data unit, range and resolution ..............................................................................203      | [¶335]


---
<!-- pagina 42 -->

# 3.3 Introduction [¶336]

# 3.3.1 Scope and purpose [¶337]

- 3.3.1.1 The  chapter  3,  Principles,  specifies  the  system  principles  of  ETCS/ERTMS.  These principles apply to on-board and trackside subsystems. [¶338]

- 3.3.1.2 The principles define the operational and technical behaviour of the system in general and functional terms. [¶339]

- 3.3.1.3 The  chapter  is divided into subchapters.  In  each  subchapter  normally  several requirements  are  defined.  Each  requirement  is  identified  with  a  unique  identification number. [¶340]

- 3.3.1.4 Notes, Justifications and Examples are only informative and shall not be regarded as requirements. [¶341]

# 3.4 Balise configuration and linking [¶342]

# 3.4.1 Balise Configurations - Balise Group Definition [¶343]

- 3.4.1.1 A balise group shall consist of between one and eight balises. [¶344]

- 3.4.1.2 In every balise shall at least be stored: [¶345]

- The internal number (from 1 to 8) of the balise [¶346]

- The number of balises inside the group [¶347]

-  The balise group identity. [¶348]

- 3.4.1.3 The internal  number  of  the  balise  describes  the  relative  position  of  the  balise  in  the group. [¶349]

# 3.4.2 Balise Co-ordinate System [¶350]

- 3.4.2.1.1 Every balise group has its own co-ordinate system. [¶351]

- 3.4.2.1.2 The orientation of the co-ordinate system of a balise group (i.e., nominal or reverse direction) is identified as balise group orientation. [¶352]

# 3.4.2.2 Balise groups composed of two or more balises [¶353]

- 3.4.2.2.1 The  origin  of  the  co-ordinate  system  for  each  balise  group  is  given  by  the  balise number 1 (called location reference) in the balise group. [¶354]

- 3.4.2.2.2 The  nominal  direction  of  each  balise  group  is  defined  by  increasing  internal  balise numbers. [¶355]


---
<!-- pagina 43 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶356]

![](images/image_0008.png)

Figure 1: Orientation of the balise group [¶357]

# 3.4.2.3 Balise groups composed of a single balise [¶358]

- 3.4.2.3.1 Balise  groups  consisting  of  only  one  single  balise  are  referred  to  as  "single  balise groups" in the following. [¶359]

No inherent coordinate system [¶360]

![](images/image_0009.png)

Figure 1a: Single balise group [¶361]

# 3.4.2.3.2 Level 1: [¶362]

- 3.4.2.3.2.1 The assignment of the co-ordinate system shall be by means of linking data. [¶363]

- 3.4.2.3.2.2 For balise groups consisting of a single balise, the information "direction with which the linked balise group will be passed over" received from a previous balise group shall assign a co-ordinate system to the balise. [¶364]


---
<!-- pagina 44 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶365]

![](images/image_0010.png)

Figure 2: Assignment of a co-ordinate system to a single balise group by linking [¶366]

- 3.4.2.3.2.3 The  reference  for  the  linking  data  shall  be  either  a  single  balise  group  if  a  coordinate system has been assigned to it before, or a balise group consisting of two or more balises (with "inherent" co-ordinate system) [¶367]

# 3.4.2.3.3 Level 2/3: [¶368]

- 3.4.2.3.3.1 If the ERTMS/ETCS on-board equipment cannot evaluate the orientation of the last balise  group  detected,  being  a  single  balise  group,  i.e.  no  linking  information  is available to identify the orientation of the co-ordinate system of this single balise group, the ERTMS/ETCS on-board equipment shall report its position by means of a position report based on two balise groups reporting the train position in reference to the LRBG and the 'previous LRBG', if any. [¶369]

- 3.4.2.3.3.1.1 Note: Receiving this type of position report advises the RBC of the need to assign a co-ordinate system to this single balise group. [¶370]

- 3.4.2.3.3.2 When  a  single  balise  group  is  detected  and  the  previous  LRBG  is  known,  the position  report  based  on  two  balise  groups  shall  use  as  direction  reference  a  move from  the  'previous  LRBG'  towards  this  single  balise  group  (being  the  new  LRBG): directional  information  in  the  position  report  pointing  in  the  same  direction  as  the direction reference shall be reported as 'nominal', otherwise as 'reverse'. [¶371]

- 3.4.2.3.3.3 If  the  'previous  LRBG  '  is  not  known,  the  'previous  LRBG'  and  all  directional information  of  the  position  report  based  on  two  balise  groups  shall  be  reported  as 'unknown'. [¶372]

- 3.4.2.3.3.4 If  a  new  single  balise  group  (BG2),  different  from  the  current  LRBG  (BG1), becomes  LRBG  while  the  running  direction  of  the  train  is  opposite  to  the  running direction when this current LRBG (BG1) was last passed, the 'previous LRBG' and all [¶373]


---
<!-- pagina 45 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶374]

directional  information  of  the  position  report  based  on  two  balise  groups  shall  be reported as 'unknown' (see Figure 2a). [¶375]

![](images/image_0011.png)

Figure 2a: Position report based on two balise groups versus train running direction [¶376]

- 3.4.2.3.3.5 If  a  single  balise  group,  being  the  LRBG,  is  detected  again,  the  LRBG  and  the 'previous  LRBG'  of  the  position  report  based  on  two  balise  groups  shall  remain unchanged. [¶377]

- 3.4.2.3.3.6 The assignment of a co-ordinate system received from the RBC shall identify the balise  group  for  which  the  assignment  is  given,  and  shall  assign  a  balise  group orientation 'nominal' or 'reverse' to this balise group relative to the on-board direction reference reported in the position report based on two balise groups (see 3.4.2.3.3.2). [¶378]

- 3.4.2.3.3.6.1 Note: From the sequence of reported balise groups, the RBC can derive the balise group orientation with which the balise group was passed. [¶379]


---
<!-- pagina 46 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶380]

![](images/image_0012.png)

Figure 2b: Example for assigning a co-ordinate system [¶381]

- 3.4.2.3.3.7 For  single  balise  groups  reported  as  LRBG  and  stored  according  to  3.6.2.2.2c, awaiting an assignment of a  co-ordinate  system,  the  ERTMS/ETCS  on-board equipment shall be able to discriminate if a single balise has been reported more than once and with different 'previous LRBGs' to the RBC. [¶382]

- 3.4.2.3.3.7.1 Note: For a single balise group reported as LRBG awaiting the assignment of a coordinate system also the rules for LRBGs reported to the RBC (see 3.6.2.2.2) apply. [¶383]

- 3.4.2.3.3.8 A co-ordinate system assignment received from trackside shall be rejected by the ERTMS/ETCS on-board equipment if the referred LRBG is memorised (see 3.6.2.2.2c) to have been reported more than once and with different 'previous LRBGs'. [¶384]

- 3.4.2.3.3.8.1 Note:  If  a  single  balise  group  is  memorised,  according  to  3.6.2.2.2c,  more  than once, and with different 'previous LRBGs', the assignment of the co-ordinate system is ambiguous. [¶385]

# 3.4.2.4 Balise groups composed of one pair of duplicated balises [¶386]

- 3.4.2.4.1 A group of two balises duplicating each other shall be treated as a single balise group in case where only one balise is correctly read. [¶387]


---
<!-- pagina 47 -->

# 3.4.3 Balise Information Types and Usage [¶388]

- 3.4.3.1 In  level  1,  all  information  to  the  on-board  system  is  given  from  balise  groups  or additionally  from  EUROLOOPS  or  Radio  Infill  Units  (see  section  3.9).  In  level  2/3, balise groups are mostly used for location information. [¶389]

- 3.4.3.2 A balise may contain directional information, i.e. valid either for nominal or for reverse direction, or may  contain  information  valid  for  both  directions. In level 1, this information can be of the following type (please refer to section 3.8.5): [¶390]

- Non-infill [¶391]

- Intentionally deleted

-  Infill. [¶392]

- 3.4.3.2.1 Intentionally deleted. [¶393]

- 3.4.3.2.2 Note:  Infill  information  is  referring  to  the  location  reference  of  an  announced  balise group. [¶394]

- 3.4.3.3 Some information shall be read also in sleeping mode and when no linking information is  available  (see  Chapter  4  Use  of  received  information).  If  such  information  is transmitted by balises, and if the information is directional, balise groups consisting of at least two balises shall be used. [¶395]

# 3.4.4 Linking [¶396]

# 3.4.4.1 Introduction [¶397]

- 3.4.4.1.1 Aim of linking: [¶398]

-  To  determine  whether  a  balise  group  has  been  missed  or  not  found  within  the expectation window (see section 3.4.4.4) and take the appropriate action. [¶399]

-  To assign a co-ordinate system to balise groups consisting of a single balise. [¶400]

-  To correct the confidence interval due to odometer inaccuracy (see section 3.6.4). [¶401]

- 3.4.4.1.2 A balise group is linked when its linking information (see section 3.4.4.2) is known in advance. [¶402]

- 3.4.4.1.2.1 Note:  In  cases  where  a  balise  group  contains  repositioning  information,  the  term linked also applies since the balise group is announced, marked as linked and contains repositioning information marked accordingly. [¶403]

# 3.4.4.2 Content of linking information [¶404]

- 3.4.4.2.1 Linking information shall be composed of: [¶405]

- The identity of the linked balise group. [¶406]

- Where the location reference of the group has to be found. [¶407]


---
<!-- pagina 48 -->

-  The accuracy of this location. [¶408]

Note: If the reference balise is duplicated, it is the trackside responsibility to define the location accuracy to cover at least the location of the two duplicated balises. [¶409]

- The direction with which the linked balise group will be passed over (nominal or reverse). [¶410]

- The reaction required if a data consistency problem occurs with the expected balise group. [¶411]

- 3.4.4.2.1.1 "Linking  information  is  used"  shall  be  interpreted  as  when  balise  group(s)  are announced and the minimum safe antenna position has not yet passed the expectation window of the furthest announced balise group. [¶412]

- 3.4.4.2.2 Instead of the identity of a linked balise group it shall be possible to identify a following linked balise group as unknown but containing repositioning information [¶413]

- 3.4.4.2.2.1 Intentionally deleted. [¶414]

- 3.4.4.2.2.2 Note 1: Regarding the repositioning information, see chapter 3.8.5.3.5 and 3.8.5.2. [¶415]

- 3.4.4.2.2.3 Note 2: In case the identity of the next balise group is not unambiguously known because the route is not known by the trackside, this feature allows to link this balise group. [¶416]

- 3.4.4.2.3 For each linked balise group, the trackside shall select one of the following reactions to be used in case of data inconsistencies: [¶417]

- Train trip  (Trip mode, see Chapter 4) [¶418]

- Command service brake [¶419]

-  No reaction [¶420]

For further details see section 3.16.2. [¶421]

# 3.4.4.3 Unlinked Balise Groups [¶422]

- 3.4.4.3.1 A  balise  group,  which  contains  information  that  must  be  considered  even  when  the balise group is not announced by linking, is called an unlinked balise group. [¶423]

- 3.4.4.3.2 Unlinked balise groups shall consist at minimum of two balises. [¶424]

- 3.4.4.3.3 Unlinked balise groups shall always contain the unlinked balise group qualifier. [¶425]

# 3.4.4.4 Rules related to linking [¶426]

- 3.4.4.4.1 When no linking  information  is  used  on-board,  all  balise  groups  shall  be  taken  into account. [¶427]

- 3.4.4.4.2 When linking information is used on-board, only balise groups marked as linked and included in the linking information and balise groups marked as unlinked shall be taken into account. [¶428]


---
<!-- pagina 49 -->

- 3.4.4.4.2.1 When linking information is used on-board and the expected balise group is referred in the linking information with a balise group with ID 'unknown', a balise group marked as linked shall only be taken into account if: [¶429]

- the on-board equipment can determine the orientation of the linked balise group by information  from  the  balise  group  itself  (therefore  excluding  for  example  single balise groups), AND [¶430]

- the  balise  group  contains  repositioning  information  valid  for  the  train  orientation, AND [¶431]

-  the balise group is crossed with the direction announced in the linking information. [¶432]

- 3.4.4.4.3 The on-board equipment shall accept a balise group marked as linked and included in the linking information (i.e. the balise giving the location reference) from [¶433]

-  when the max safe front end of the train has passed the first possible location of the balise group [¶434]

until [¶435]

-  the  min  safe  front  end  of  the  train  has  passed  the  last  possible  location  of  the balise group [¶436]

taking the offset between the front of the train and the balise antenna into account. [¶437]

- 3.4.4.4.3.1 Note: The first possible location and the last possible location of the balise group are defined by the linking distance and the location accuracy. [¶438]

- 3.4.4.4.3.2 Note: The interval between the outer limits to accept the balise group defines the expectation window. [¶439]

- 3.4.4.4.4 In case of a balise group containing repositioning information, the first possible location shall start from the previously linked balise group. [¶440]

- 3.4.4.4.5 The on-board equipment shall expect balise groups one by one (i.e., it shall supervise only  one  expectation  window  at  a  time)  according  to  the  order  given  by  linking information. [¶441]

- 3.4.4.4.6 The ERTMS/ETCS on-board equipment shall stop expecting a balise group and shall expect the next one announced in the linking information (if any) when: [¶442]

- the balise group is found inside its expectation window [¶443]

- a linking consistency error is found, see 3.16.2.3.1 [¶444]

- 3.4.4.4.6.1 Linking consistency error due to early reception of balise group expected later (see 3.16.2.3.1  c)):  if  the  balise  group  found  is  the  next  one  announced  in  the  linking information, the ERTMS/ETCS on-board equipment shall check its linking consistency and apply again clause 3.4.4.4.6, i.e. it will immediately expect the further next balise group announced in the linking information. [¶445]


---
<!-- pagina 50 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶446]

# 3.5 Management of Radio Communication [¶447]

- 3.5.1.1 Note: the following section refers to the behaviour of the user application interacting with Euroradio protocols. How the messages are actually transported from the sender to the receiver user application is not relevant for this description. [¶448]

# 3.5.2 General [¶449]

- 3.5.2.1 Each communication session managed by an entity allows the exchange of data with only one other entity. [¶450]

- 3.5.2.2 Note:  in  the  following  sections  reference  is  made  to  safe  radio  connections,  whose definition and management is contained in Euroradio specification. [¶451]

- 3.5.2.3 Note: The  information Initiation  of  a  Communication  Session  and  Version  not Compatible (see sections 3.5.2.4 and 3.17) are the same in every system version. [¶452]

- 3.5.2.4 The  ERTMS/ETCS  on-board  equipment  shall  be  able  to  manage  simultaneous communication sessions with at least two different entities. [¶453]

# 3.5.3 Establishing a communication session [¶454]

- 3.5.3.1 Only the ERTMS/ETCS on-board equipment can initiate a communication session. [¶455]

- 3.5.3.2 Intentionally deleted. [¶456]

- 3.5.3.3 Note:  Only  communication  sessions  between  an  ERTMS/ETCS  on-board  equipment and a trackside equipment (RBC or Radio Infill Unit) are considered here. [¶457]

- 3.5.3.4 The on-board shall establish a communication session [¶458]

- At Start of Mission (only if level 2 or 3). [¶459]

- If ordered from trackside. [¶460]

-  If  a  mode  change,  neither  considered  as  an  End  of  Mission  nor  triggered  from condition g) below, has to be reported to the RBC (only if level 2 or 3) [¶461]

- If the driver has manually changed the level to 2 or 3 [¶462]

- When the train front reaches the end of an announced radio hole [¶463]

-  When the previous communication session is considered as terminated due to loss of safe radio connection (refer to 3.5.4.2.1) [¶464]

- When a Start of Mission procedure, during which no communication session could be established, is completed in level 2 or 3 [¶465]

- When outside the Start of Mission procedure, the driver has manually selected the RBC contact information (only if level 2 or 3) [¶466]


---
<!-- pagina 51 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶467]

- 3.5.3.4.1 In respect of a), b), c), d), e) and h) of 3.5.3.4, the on-board shall not establish a new communication session with an RBC/RIU in case a communication session is currently being established or is already established with this RBC/RIU. [¶468]

- 3.5.3.5 The order to contact an RBC shall include [¶469]

- The identity of the RBC. [¶470]

- The telephone number of the RBC. [¶471]

-  The action to be performed (establish/terminate the session). [¶472]

- Whether this applies also to Sleeping units. [¶473]

- 3.5.3.5.1 See table at the end of section 3.5.3. [¶474]

- 3.5.3.5.2 If  the  ERTMS/ETCS  on-board  equipment  has  to  establish  a  communication  session with an RBC whilst in session with another RBC, the existing communication session shall  be  terminated  (see  3.5.5.2  for  details)  and  the  new  one  shall  be  established. Exception: the order to contact an Accepting RBC  shall not terminate the communication session with the Handing Over RBC. [¶475]

- 3.5.3.5.3 The order to contact an Accepting RBC shall be part of the RBC transition order and shall include: [¶476]

- The identity of the Accepting RBC. [¶477]

- The telephone number of the Accepting RBC. [¶478]

-  Whether this applies also to Sleeping unit. [¶479]

- 3.5.3.6 The order to contact a Radio Infill Unit shall include [¶480]

- The identity of the Radio Infill Unit [¶481]

- The telephone number of the Radio Infill Unit [¶482]

-  The action to be performed (establish/terminate the session). [¶483]

- 3.5.3.7 The  establishment  of  a  communication  session  shall  be  performed  according  to  the following steps: [¶484]

- The on-board shall request the set-up of a safe radio connection with the trackside. If  this request is part of an ongoing Start of Mission procedure or is related to the establishment  of  a  communication  session  due  to  condition  3.5.3.4  c),  it  shall  be repeated until successful or a defined number of times (see Appendix A.3.1). [¶485]

If this request is not part of an ongoing Start of Mission procedure and is not related to the establishment of a communication session due to condition 3.5.3.4 c), it shall be repeated until successful. [¶486]

A  request  shall  be  repeated  immediately  after  EURORADIO  has  indicated  that setting up the safe radio connection has failed. [¶487]


---
<!-- pagina 52 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶488]

- As  soon  as  the  safe  radio  connection  is  set-up,  the  on-board  shall  send  the message Initiation of communication session to the trackside. [¶489]

- As soon as the trackside receives the information, it shall send the system version. [¶490]

-  When the on-board receives the system version it shall consider the communication session established and: [¶491]

-  If  one  of  its  supported  system  versions  is  compatible  with  the  one  sent  by trackside,  it  shall  send  a  session  established  report,  including  its  supported system versions, to the trackside. [¶492]

-  If  none  of  its  supported  system  versions  is  compatible  with  the  one  sent  by trackside, it shall send a version independent message indicating 'No compatible version supported'. It shall inform the driver and shall terminate the communication session. [¶493]

- When the trackside receives the session established report or the information that no  compatible  system  version  is  supported  by  the  on-board,  it  shall  consider  the communication session established. [¶494]

- 3.5.3.8 When a communication session is currently being established (i.e. at any time from the first  request  the  set-up  of  a  safe  radio  connection  to  the  reception  of  the  system version from trackside), the on-board shall no longer apply 3.5.3.7 a), 3.5.3.7 b) and 3.5.3.7 d) (i.e. it aborts the process of establishing it) and shall release the safe radio connection (if any) if at least one of the following conditions is met: [¶495]

- The driver closes the desk during Start of Mission [¶496]

- End of Mission is performed [¶497]

-  An order to terminate the communication session is received from trackside [¶498]

![](images/image_0013.png)

Figure 3: Establishment initiated by on-board [¶499]


---
<!-- pagina 53 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶500]

- The train passes with its front end a level transition border from a level 2/3 area to an area where level 2/3 operation is not supported [¶501]

- An order to establish a communication session with a different RBC is received from trackside and the order does not request to contact an Accepting RBC [¶502]

-  The train passes an RBC/RBC border with its front end [¶503]

- The train front passes the start of an announced radio hole [¶504]

- Regards RIUs only: Level 1 is left [¶505]

- 3.5.3.9 Intentionally deleted. [¶506]

- 3.5.3.9.1 Intentionally deleted. [¶507]

- 3.5.3.10 Intentionally deleted. [¶508]

# Figure 4: Intentionally deleted

- 3.5.3.11 If the driver selects 'Use of EIRENE short number' to contact the RBC, the on-board shall not use the stored RBC ID/phone number, if any. [¶509]

- 3.5.3.11.1  Note:  The  on-board  stored  short  number  for  calling  the  'most  appropriate  RBC'  is defined by EIRENE. [¶510]

- 3.5.3.11.2  Justification: In case of EIRENE short number selection by the driver, the termination of  the  connection  if  the  'most  appropriate  RBC'  does  not  match  the  one  previously stored on-board (EURORADIO functionality) must not occur. [¶511]

- 3.5.3.12 Intentionally deleted. [¶512]

- 3.5.3.13 An order to contact the RBC may contain a special value for the RBC identity indicating that  the  on-board  shall  contact  the  last  known  RBC  (i.e.,  using  the  stored  RBC ID/phone number, if any); the phone number indicated in the order shall be ignored by the on-board equipment. [¶513]

- 3.5.3.13.1  If there is no RBC ID/ phone number stored on-board, the order to contact the RBC shall be ignored. [¶514]

- 3.5.3.14 Note: If a short number is used (considering trackside call routing), that number can be programmed into the balise instead of the normal phone number. [¶515]

- 3.5.3.15 An order to contact the RBC may contain a special value for the RBC phone number indicating that the on-board shall use the on-board short number. [¶516]

- 3.5.3.15.1  Intentionally deleted. [¶517]

# 3.5.3.16 [¶518]


---
<!-- pagina 54 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶519]

[¶520]
|   Option | Balise data content                                                                               | Train reaction                                                                                                                                                                                            |
|----------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        1 | Order to contact RBC Special value for RBC ID: Contact last known RBC RBC Phone number irrelevant | Contact last known RBC (order is ignored in case no RBC ID/ phone number is stored on- board)                                                                                                             |
|        2 | Order to contact RBC RBC ID Special value for RBC phone number: use on-board stored short number  | Contact given RBC by using RBC ID and the on-board short number. Note: If the short number does not direct to the RBC with the given RBC ID, the connection will be terminated (EURORADIO functionality). |
|        3 | Order to contact RBC RBC ID + RBC phone number                                                    | Contact given RBC by using RBC ID and the RBC phone number                                                                                                                                                |

# 3.5.4 Maintaining a communication session [¶521]

- 3.5.4.1 When  a  communication  session  is  established,  in  case  of  a  loss  of  the  safe  radio connection, i.e., if the disconnection has not been ordered (see 3.5.5.1), the involved entities shall consider the communication session still established for a defined time. The defined time shall start as soon as EURORADIO has indicated the loss of the safe radio connection. [¶522]

- 3.5.4.2 When EURORADIO indicates the loss of the safe radio connection, the ERTMS/ETCS on-board equipment shall immediately try to set-up a new safe radio connection. [¶523]

- 3.5.4.2.1 If  the safe radio connection is not re-established after the defined time (as defined in A.3.1),  both,  on-board  equipment  and  trackside,  shall  consider  the  session  as terminated . [¶524]

- 3.5.4.3 The attempts shall be repeated, until at least one of the following conditions is met: [¶525]

-  The safe radio connection is set-up. [¶526]

-  The session is considered as terminated. [¶527]

-  The train passes the location indicated in the RIU order 'Terminate the communication session' [¶528]

- 3.5.4.3.1 Note: if the session is considered as terminated due to 3.5.4.2.1, the attempts will be resumed immediately according to 3.5.3.4 f). [¶529]


---
<!-- pagina 55 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶530]

- 3.5.4.4 Exception to 3.5.4.2 and 3.5.4.3: the on-board equipment shall not try to set up a new safe radio connection and shall stop any ongoing attempts if the train front is inside an announced  radio  hole  (see  3.12.1.3).  The  on-board  equipment  shall  try  to  set  it  up again when the train front reaches the end of the radio hole. [¶531]

- 3.5.4.5 In  case  a  message has to be sent during the loss of the safe radio connection, this message shall be considered as sent. [¶532]

# 3.5.5 Terminating a communication session [¶533]

- 3.5.5.1 The termination of a communication session shall be initiated only by the on-board and in the following cases: [¶534]

- If  an  order  is  received  from  trackside  (RBC,  RIU  or  balise  groups)  (see  sections 3.5.3.5 and 3.5.3.6 concerning the content of the order). [¶535]

- If  a  condition  requiring  the  termination  of  the  communication  session  is  fulfilled without  any  explicit  trackside  order.  The  situations  in  which  such  condition  is  met are detailed in other sections of this specification. [¶536]

-  Intentionally deleted. [¶537]

- Intentionally deleted. [¶538]

- Intentionally deleted. [¶539]

-  Intentionally deleted. [¶540]

- 3.5.5.2 In case  a  session  is  established,  the  on-board  equipment  shall  terminate  the communication session according to the following steps: [¶541]

- The  on-board  equipment  shall  send  a  Termination  of  communication  session message. [¶542]

- As soon as this information is received, the trackside shall consider the communication session terminated and send an acknowledgement to the on-board. [¶543]

-  When the acknowledgement is received the on-board shall consider the communication  session  terminated  and  request  the  release  of  the  safe  radio connection with trackside. [¶544]


---
<!-- pagina 56 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶545]

![](images/image_0014.png)

Figure 5: Termination of a communication session [¶546]

- 3.5.5.3 No further message shall be sent by the on-board after the message Termination of communication session. [¶547]

- 3.5.5.3.1 Exception: In case a communication session is established and no acknowledgement is  received  within  a  fixed  waiting  time  (see  Appendix  A.3.1)  after  sending  the 'Termination of communication session' message, the message shall be repeated with the fixed waiting time after each repetition. [¶548]

- 3.5.5.3.2 After a defined number of repetitions (see Appendix A.3.1), and if no acknowledgment is  received  within  the  fixed  waiting  time  from  the  time  of  the  last  sending  of 'Termination of communication session', the ERTMS/ETCS onboard equipment shall consider the communication session terminated. [¶549]

- 3.5.5.4 No further message shall be sent by the trackside after the message Acknowledgement of the termination of communication session. [¶550]

- 3.5.5.5 Note:  The  information  Termination  of  Communication  Session  and  corresponding Acknowledgement are the same in every system version. [¶551]

- 3.5.5.6 Messages  from  the  RBC  received  onboard  after  the  message  'Termination  of communication  session'  has  been  sent  shall  be  ignored  with  the  exception  of  the Acknowledgement of the termination of communication session. [¶552]

- 3.5.5.7 Intentionally deleted. [¶553]

# 3.5.6 Registering to the Radio Network [¶554]

- 3.5.6.1 ERTMS/ETCS on-board equipment shall order the registration of its connected Mobile Terminal(s) to a Radio Network: [¶555]

- At power-up [¶556]


---
<!-- pagina 57 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶557]

- Following driver entry of a new Radio Network identity [¶558]

-  If ordered from the trackside [¶559]

- 3.5.6.2 When  powered-off,  ERTMS/ETCS  on-board  equipment  shall  memorize  the  last received Radio Network identity (from trackside or from driver) and shall use it when powered-up again. [¶560]

- 3.5.6.3 If  no  Radio  Network  identity  received  from  trackside  or  from  driver  could  have  been memorized by ERTMS/ETCS on-board equipment (e.g. after a System Failure or at very  first  power-up),  this  latter  shall  nevertheless  order  the  registration  of  its  Mobile Terminal(s) to a default Radio Network. [¶561]

- 3.5.6.3.1 Note  1:  the  source  used  to  retrieve  the  default  Radio  Network  identity  (on-board equipment  permanent  storage,  Mobile  Terminal  itself,  or  other  external  source)  is implementation dependent. [¶562]

- 3.5.6.3.2 Note 2: if ERTMS/ETCS on-board equipment is powered-up in an area not covered by the memorized or default Radio Network, attempts to register to this Radio Network will be  repeated  unconditionally  by  the  Mobile  Terminal(s)  until  either  an  attempt  is successful or a new Radio Network identity is received from trackside or from driver, preventing Mobile Terminal(s) from registering to any unwanted Radio Network . [¶563]

- 3.5.6.4 Intentionally deleted. [¶564]

- 3.5.6.5 On  reception of the trackside order,  ERTMS/ETCS  on-board  equipment  shall immediately order the Radio Network registration of each Mobile Terminal that fulfils the following conditions: [¶565]

- it is not yet registered to the ordered Radio Network, AND [¶566]

- it is not used for an established communication session, AND [¶567]

-  no safe radio connection is being set-up [¶568]

- 3.5.6.6 If  a  Mobile  Terminal  is  not  currently  registered  to  the  Radio  Network  ordered  by trackside and if one of the conditions b) or c) is not fulfilled, ERTMS/ETCS on-board equipment shall initiate the Radio Network registration once communication session is terminated and safe radio connection is released. [¶569]

- 3.5.6.7 If  no  Mobile Terminal is duly registered to a Radio Network, any order to contact an RBC or an RIU received from trackside shall be rejected by ERTMS/ETCS on-board equipment. [¶570]

# 3.5.7 Safe Radio Connection Indication [¶571]

- 3.5.7.1 The ERTMS/ETCS on-board equipment shall inform the driver about the status of the safe  radio  connection.  To  that  purpose,  the  following  indication  statuses  of  the  safe radio  connection  are  defined:  'No  Connection',  'Connection  Lost/Set-Up  failed', 'Connection Up'. [¶572]


---
<!-- pagina 58 -->

- 3.5.7.2 In  addition,  the  ERTMS/ETCS  on-board  equipment  shall  use  a  'connection  status' timer (see Appendix A.3.1), in order to manage properly the transitions to the indication status 'Connection Lost/Set-Up failed'. [¶573]

- 3.5.7.2.1 Note: The purpose of the 'connection status' timer is to avoid distracting the driver for any short disturbance of the safe radio connection. [¶574]

- 3.5.7.3 The  ERTMS/ETCS  on-board  equipment  shall  start  the  'connection  status'  timer  as soon as the first request to set-up a safe radio connection with the relevant RBC/RIU is sent: [¶575]

- for what regards the session establishment, see items b), c), d), e) in 3.5.3.4. [¶576]

- for what regards maintaining a communication session, see 3.5.4.2 and 3.5.4.4 [¶577]

- 3.5.7.4 If the 'connection status' timer is ongoing, it shall be stopped if the requests to set-up a safe radio connection are stopped with the relevant RBC/RIU. [¶578]

- 3.5.7.5 The  ERTMS/ETCS  on-board  equipment  shall  execute  the  transitions  between  the different indication statuses of the safe radio connection with the relevant RBC/RIU as described  in  Table  1  according  to  the  conditions  in  Table  2  (see  section  4.6.1  for details about the symbols). [¶579]

[¶580]
| No Connection   | < 3 -p2-                        | < 5, 6, 7 -p1-   |
|-----------------|---------------------------------|------------------|
| 1, 2 > -p2-     | Connection Lost / Set-Up failed | <2 -p2-          |
| 4 > -p1-        | 4 > -p1-                        | Connection Up    |

Table 1: Transitions between the indication statuses of the safe radio connection [¶581]


---
<!-- pagina 59 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶582]

[¶583]
| Condition Id   | Content of the conditions                                                                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [1]            | (a Start of mission procedure is ongoing) AND (the final attempt to set-up the safe radio connection failed)                                                                      |
| [2]            | (the 'connection status' timer expires)                                                                                                                                           |
| [3]            | (no Start of mission procedure is ongoing) AND (the requests to set-up a safe radio connection are stopped with the relevant RBC/RIU for reason other than the successful set-up) |
| [4]            | (the safe radio connection is set-up)                                                                                                                                             |
| [5]            | (the safe radio connection is released)                                                                                                                                           |
| [6]            | (the safe radio connection is lost) AND (the requests to set-up a safe radio connection are stopped with the relevant RBC/RIU for reason other than the successful set-up)        |
| [7]            | (the safe radio connection is lost) AND (the train front is inside an announced radio hole)                                                                                       |

# Table 2: Transition conditions for the indication statuses of the safe radio connection [¶584]

- 3.5.7.6 For  the  case  of  an  RBC/RBC  transition,  the  safe  radio  connection  indicated  to  the driver  shall  switch  from  the  indication  status  of  the  safe  radio  connection  with  the Handing over RBC to the one with the Accepting RBC as soon as one of the following conditions is met: [¶585]

- the  ERTMS/ETCS  on-board  equipment  sends  a  position  report  directly  to  the Accepting  RBC  with  its  maximum  safe  front  end  having  passed  the  border,  see 3.15.1.3.5 (i.e. the Accepting RBC becomes the supervising RBC), [¶586]

- the safe radio connection is released with the Handing over RBC and the minimum safe rear end of the train has crossed the border, see 3.15.1.2.7 and 3.15.1.3.9. [¶587]

- 3.5.7.6.1 Note:  During  an  RBC/RBC  handover  procedure,  an  indication  status  transition  table and a connection status timer might have to be managed at the same time, for each RBC. [¶588]

- 3.5.7.7 For the case of safe radio connection with RIU's, the safe radio connection indicated to the driver shall be the one related to the current infill area. [¶589]

# 3.6 Location Principles, Train Position and Train Orientation [¶590]

# 3.6.1 General [¶591]

- 3.6.1.1 Two types of location based data are defined: [¶592]

- Data  that  refers  only  to  a  given  location,  referred  to  as  Location  data  (e.g.  level transition orders, linking) [¶593]


---
<!-- pagina 60 -->

- Data that remains valid for a certain distance, referred to as Profile data (e.g. SSP, gradient). [¶594]

- 3.6.1.2 Note: Determination of the Train Position is always longitudinal along the route, even though the route might be set through a complex track layout. [¶595]

![](images/image_0015.png)

Figure 6: Actual route of the train [¶596]

1 [¶597]

# Figure 7: Route known by the train [¶598]

- 3.6.1.3 The  Train  Position  information  defines  the  position  of  the  train  front  in  relation  to  a balise group, which is called LRBG (the Last Relevant Balise Group). It includes: [¶599]

-  The estimated train front end position, defined by the estimated distance between the LRBG and the front end of the train [¶600]

-  The train position confidence interval (see 3.6.4) [¶601]

-  Directional  train  position  information  in  reference  to  the  balise  group  orientation (see 3.4.2, also Figure 14) of the LRBG, regarding: [¶602]

-  the position of the train front end (nominal or reverse side of the LRBG) [¶603]

-  the train orientation [¶604]

-  the train running direction [¶605]

In  case  of  an  LRBG  being  a  single  balise  group  with  no  co-ordinate  system assigned, directional information is defined in reference to the pair of LRBG and 'previous LRBG', see 3.4.2.3.3 [¶606]

-  A  list  of  LRBGs,  which  may  alternatively  be  used  by  trackside  for  referencing location dependent information (see 3.6.2.2.2 c)). [¶607]

- 3.6.1.4 Balise groups, which are marked as unlinked, shall never be used as LRBG. [¶608]

5 [¶609]

7 [¶610]


---
<!-- pagina 61 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶611]

- 3.6.1.4.1 Justification: The location of an unlinked balise group, or the balise group itself, may not be known to the RBC. [¶612]

- 3.6.1.5 If there is an active cab, this one defines the orientation of the train, i.e. the side of the active  cab  shall  be  considered  as  the  front  of  the  train.  If  no  cab  is  active,  the  train orientation shall be as when a cab was last active. [¶613]

- 3.6.1.6 The 'train orientation relative to LRBG' is defined as the train orientation related to the orientation of the LRBG, see Figure 14. It can be either 'nominal' or 'reverse'. [¶614]

- 3.6.1.6.1 Note: The train orientation cannot be affected by the direction controller position. [¶615]

# 3.6.2 Location of Data Transmitted to the On-Board Equipment [¶616]

# 3.6.2.1 Data Transmitted by Balises [¶617]

- 3.6.2.1.1 All location and profile data transmitted by a balise shall refer to the location reference and orientation of the balise group to which the balise belongs. [¶618]

- 3.6.2.1.2 Exception: Regarding infill information the section 3.6.2.3.1 shall apply. [¶619]

# 3.6.2.2 Data Transmitted by Radio from RBC [¶620]

- 3.6.2.2.1 All  location  and  profile  data  transmitted  from  the  RBC  shall  refer  to  the  location reference and orientation of the LRBG given in the same message. [¶621]

- 3.6.2.2.2 For the LRBG the following requirements have to be met: [¶622]

- The  on-board  equipment  shall  use  the  last  balise  group  passed  as  a  reference when reporting its position to the RBC (in the following termed as LRBGONB). Only [¶623]

-  balise groups marked as linked and contained in the previously received linking information, if linking information is used on-board [¶624]

or [¶625]

-  the last  balise  group not marked as unlinked, if no linking was used when this balise group was passed [¶626]

shall be regarded. [¶627]

- The RBC shall use a balise group which was reported by the on-board equipment as a reference (in the following termed as LRBGRBC). At a certain moment LRBGRBC and LRBGONB can be different. [¶628]

-  The on-board equipment shall be able to accept information referring to one of at least eight LRBGONB last reported to the RBC. [¶629]

- 3.6.2.2.2.1 Exception  to  a):  When  on-board  position  is  unknown  or  when  position  data  has been  deleted  during  SoM  procedure,  the  on-board  equipment  shall  use  an  LRBG identifier set to "unknown" until the onboard has validated its position again by passing a balise group. [¶630]


---
<!-- pagina 62 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶631]

- 3.6.2.2.2.2 Exception to b): When the RBC has received from the onboard an unknown position (as per 3.6.2.2.2.1) or during SoM procedure an invalid position which it is not able to confirm,  the  RBC  shall  use  an  LRBG  identifier  set  to  "unknown"  until  it  receives  a position  report  from  the  onboard  having  validated  its  position  by  passing  a  balise group. [¶632]

- 3.6.2.2.2.3 Regarding  c):  From  the  time  it  has  reported  an  unknown  position,  or  an  invalid position during SoM procedure, to the time it has received from the RBC a message with  an  LRBG  not  set  to  'unknown',  the  on-board  equipment  shall  also  be  able  to accept messages from the RBC containing LRBG 'unknown'. [¶633]

- 3.6.2.2.3 Example: The following figure illustrates the on-board and RBC views of LRBGs: [¶634]

![](images/image_0016.png)

Balise groups A, C have been reported to the RBC and can be used by the RBC as LRBG [¶635]

Balise groups D - F : are known thanks to previously received linking information and can be used in the future as onboard reference [¶636]

# Figure 8: On-board and RBC views of LRBG when train is reporting new LRBGONB "D" [¶637]

- 3.6.2.2.3.1 Note:  Figure  8  illustrates  the  case  where  the  RBC  uses  as  reference  the  last received LRBGONB. The RBC could also use a previously received one (see 3.6.2.2.2 b)). [¶638]

# 3.6.2.3 Data transmitted as Infill information [¶639]

- 3.6.2.3.1 All  location  and profile data transmitted  as infill information shall refer to the location reference of the balise group at the next main signal (identified by the infill information) and to the orientation given by the infill device. (See note after justification). [¶640]


---
<!-- pagina 63 -->

- 3.6.2.3.1.1 Justification: [¶641]

-  At  locations  where  routes  join:  Infill  information  is  the  same  for  all  routes,  only linking information is different for different routes, see figure below (infill by means of balise group(s), loop or radio) [¶642]

-  In  case  of  an  infill  area  with  multiple  balise  groups:  all  balise  groups  transmit identical information, as the information of all groups refers to the balise group at the main signal. [¶643]

- 3.6.2.3.1.2 Note:  The  orientation  of  infill  information  given  by  an  infill  device  is  defined  in reference to (see also section 3.9): [¶644]

-  In  case  of  a  balise  group,  the  orientation  of  the  balise  group  sending  the  infill information [¶645]

-  In case of loop, the orientation indicated by the End Of Loop Marker [¶646]

-  In case of radio, the orientation of the LRBG indicated in the message [¶647]

![](images/image_0017.png)

Figure 9: Routes Join in Rear of InFill Area [¶648]

![](images/image_0018.png)

Figure 10 : Location referencing of infill information transmitted by balise groups [¶649]

# 3.6.2.4 Data transmitted by Loop [¶650]

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶651]


---
<!-- pagina 64 -->

- 3.6.2.4.1 It shall be possible to transmit non-infill location data by loop, which refers to a balise group as location reference. [¶652]

- 3.6.2.4.1.1 Note: Regarding infill information see section 3.6.2.3. [¶653]

- 3.6.2.4.2 The orientation of data transmitted by a loop is determined by the EOLM information which indicates  how  the  directional  information  contained  in  loop  messages  is  to  be interpreted. [¶654]

# 3.6.3 Validity direction of transmitted Information [¶655]

# 3.6.3.1 General [¶656]

- 3.6.3.1.1 The direction for which transmitted information is valid shall refer to: [¶657]

- the direction of the LRBG for information sent by radio [¶658]

- the direction of the balise group sending the information. [¶659]

- 3.6.3.1.2 Data transmitted to the on-board equipment (by balise or radio) shall be identified as being valid for [¶660]

- both directions [¶661]

- the nominal direction [¶662]

-  the reverse direction [¶663]

of the referenced balise group. [¶664]

- 3.6.3.1.2.1 Deleted. [¶665]

- 3.6.3.1.3 When  receiving  information  from  any  transmission  medium,  the  ERTMS/ETCS  onboard equipment shall only take into account information valid for its orientation. Other information  shall  be  ignored.  Exception:  for  SL,  PS  and  SH  engines,  balise  group crossing direction shall be considered. [¶666]

- 3.6.3.1.3.1 If the train position is unknown, data received from any transmission medium valid for one direction only (nominal or reverse) shall be rejected by the onboard equipment. Data valid for both directions shall be evaluated (see section 4.8). [¶667]

- 3.6.3.1.4 If no co-ordinate system has been assigned to a single balise group, data transmitted by trackside, which refers to that balise group requiring the co-ordinate system to be known (i.e. all data which are only valid for one direction (nominal or reverse)) shall be rejected by the ERTMS/ETCS on-board equipment. Data valid for both directions shall be evaluated (see section 4.8). [¶668]

- 3.6.3.1.4.1 Exception:  if  not  rejected  due  to  balise  group  message  consistency  check  (see 3.16.2.4.4.1 and 3.16.2.5.1.1), data to be forwarded to a National System (see section 3.15.6)  shall  be  accepted.  Justification:  the  co-ordinate  system  of  the  balise  group might  be  known  to  the  National  System  by  other  means  inherent  to  the  National System itself. [¶669]


---
<!-- pagina 65 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶670]

# Figure 11: Intentionally deleted

# 3.6.3.2 Location, Continuous Profile Data and Non-continuous Profile Data [¶671]

- 3.6.3.2.1 Location and profile data shall have the structure shown in Figure 12 below [¶672]

- 3.6.3.2.2 With regard to Figure 12 the following applies to continuous profile data: [¶673]

- Value (n) shall be valid for distance (n+1) [¶674]

- For distance (1) the previously received data shall be used (in case of an SSP this includes train length delay, refer to 3.11.3.1.3). [¶675]

-  Distances shall be given as unsigned incremental values representing the distance between value(n) and value(n-1). [¶676]

- The last value (n) transmitted shall be valid for an unlimited distance unless value(n) represents a special "end of profile" value. [¶677]

![](images/image_0019.png)

Figure 12: General Structure of location and profile data [¶678]


---
<!-- pagina 66 -->

- If distance (n+1) = 0 then the corresponding profile value n shall still be taken into account. [¶679]

- 3.6.3.2.3 With regard to Figure 12 the following shall apply to location data: [¶680]

- Distances shall be given as unsigned incremental values representing the distance between value(n) and value(n-1). [¶681]

- For distance (1) the previously received data shall be used. [¶682]

-  Each value (n) may represent a single value or a set of data. [¶683]

- 3.6.3.2.4 According  to  Figure  12  the  structure  for  non-continuous  profile  data  shall  allow  to contain multiple elements (value(n) for length(n)) inside the profile. [¶684]

- Distance  to  the  start  of  each  element  (value(n)  for  length(n))  shall  be  given  as unsigned  incremental  values,  each  increment  representing  the  distance  between starts of element (n) and element (n-1). [¶685]

- For  distance  (1)  the  previously  received  data  (or  initial  data/default  values,  see section 3.7) shall be used. [¶686]

-  Each value (n) may represent a single value or a set of data. [¶687]

- Note: There is no relationship between length of element (n-1) and distance (n), i.e., elements may overlap. [¶688]

- 3.6.3.2.5 It shall be possible for the RBC to shift the location reference, e.g., after a change of train orientation or running direction. [¶689]

- 3.6.3.2.5.1 Justification: Refer to Figure 13. To make it possible to shift the location reference if - due to the location of the LRBG and the start location - distance (1) would become a negative value. [¶690]


---
<!-- pagina 67 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶691]

![](images/image_0020.png)

# Figure 13: Shifted Location Reference (shown for continuous data /location profile, but also valid for non continuous data profile) . [¶692]

- 3.6.3.2.6 With regards to Figure 12 the following applies to linking information [¶693]

- The  distance  (1)  shall  be  given  to  the  first  balise  group  included  in  the  linking information [¶694]

- The  distance  (n)  shall  be  given  as  the  distance  between  two  consecutive  balise groups [¶695]

-  Each value (n) shall represent the linking information related to that balise group. [¶696]

# 3.6.4 Train Position Confidence Interval and Relocation [¶697]

- 3.6.4.1 All location related information transmitted from trackside equipment shall be used by the  on-board  equipment  taking  into  account  the  confidence  interval  to  the  train position, if required for safe operation. [¶698]

- 3.6.4.2 The confidence interval to the train position shall refer to the distance to the LRBG and shall take into account [¶699]

- On-board over-reading amount and under-reading amount (odometer accuracy plus the error in detection of the balise group location reference) [¶700]

- The location accuracy of the LRBG. [¶701]

- 3.6.4.2.1 Distance information received from trackside shall be evaluated on-board as nominal information (without taking into account any tolerances). [¶702]


---
<!-- pagina 68 -->

- 3.6.4.2.2 Note: The confidence interval increases in relation to the distance travelled from the LRBG depending on the accuracy of odometer equipment until it is reset when another balise group becomes the LRBG. [¶703]

- 3.6.4.2.3 The  value  of  the  Location  Accuracy  shall  be  determined  by  Linking  information  if available,  if  not,  by  the  corresponding  National  Value,  or  the  corresponding  Default Value if the National Value is not applicable. [¶704]

- 3.6.4.3 When another balise group becomes the LRBG or when evaluating (see section 4.8) location related trackside information, which is referred to a previously received balise group different from the LRBG, all the location related information shall be relocated by subtracting from the distances that are counted from the reference balise group of the location related information: [¶705]

- the distance between the reference balise group of the location related information and the LRBG, retrieved from linking information if it is available and it includes both the reference balise group and the LRBG, OR [¶706]

- in  all  other  cases,  the  estimated  travelled  distance  between  the  reference  balise group of the location related information and the LRBG. [¶707]

- 3.6.4.3.1 Justification:  it  is  always  the  trackside  responsibility  to  provide  linking  in  due  course, knowing this rule; if the location related information is to be used in situations where linking is not provided (e.g. TSR transmitted by balise group marked as unlinked), the trackside can include provisions, if deemed necessary, when engineering the distance information. [¶708]


---
<!-- pagina 69 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶709]

![](images/image_0021.png)

Confidence Interval = Function [Q_LOCACC; Odometer Error] [¶710]

When the ERTMS/ETCS on-board has read the balise group 1 [¶711]

-  the Confidence Interval is reset taking into account the location accuracy of balise group 1, and on-board tolerances when determining the reference location of the balise group, [¶712]

-  the nominal distance to EOA is relocated by subtracting D_LINK (1) from nominal distance (1), resulting in nominal distance (2). (Nominal distance (1) may be the distance to EOA received in the MA or the result of a previous relocation.) [¶713]

Figure 13a: Reset of confidence interval and relocation, on change of LRBG [¶714]


---
<!-- pagina 70 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶715]

![](images/image_0022.png)

When the on-board performs the transition to level 2, the MA stored on-board (referred to balise group 0) is relocated prior to its evaluation: [¶716]

-  If balise group 1 is still the LRBG, the first MA Section distance is relocated by subtracting D_LINK (1) from MA Section (1), resulting in MA section (1') [¶717]

-  If balise group 2 is already the LRBG, the first MA Section distance is relocated by subtracting (D_LINK (1) + D_LINK (2)) from MA Section (1), resulting in MA section (1') [¶718]

-  MA Section (2) distance remains unchanged [¶719]

# Figure  13b:  Relocation  of  trackside  information  referred  to  previously  passed balise group, different from the current LRBG [¶720]

- 3.6.4.4 The train front end position shall be identified in the following way [¶721]

- The estimated front end position. [¶722]

- The max(imum) safe front end position, differing from the estimated position by the under-reading amount in the distance measured from the LRBG plus the location accuracy of the LRBG. [¶723]

- I.e. in relation to the orientation of the train this position is in advance of the estimated position. [¶724]

-  The min(imum) safe front end position, differing from the estimated position by the over-reading amount in the distance measured from the LRBG plus the location accuracy of the LRBG. [¶725]

- I.e. in relation to the orientation of the train this position is in rear of the estimated position. [¶726]

- 3.6.4.4.1 Note: The rear end position is referenced in the same way. However min safe rear end is only safe if sent together with train integrity information. [¶727]


---
<!-- pagina 71 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶728]

![](images/image_0023.png)

Figure 13c: Train confidence interval and train front end position [¶729]

- 3.6.4.5 Intentionally deleted. [¶730]

- 3.6.4.6 The estimated front end shall be used when supervising location information, unless stated otherwise. [¶731]

- 3.6.4.7 Supervision  of  location  related  information  transmitted  by  a  balise  group  marked  as unlinked and referred to this balise group: [¶732]

- 3.6.4.7.1 By exception to clause 3.6.1.3, the train position is referred to this balise group marked as  unlinked.  The  ERTMS/ETCS  on-board  equipment  shall  temporarily  apply  by analogy  clauses  3.6.4.2,  3.6.4.2.1,  3.6.4.2.3  and  3.6.4.4  to  determine  an  additional confidence  interval,  until  a  further  received  balise  group  becomes  the  LRBG  or  the location related information is deleted on-board. [¶733]

- 3.6.4.7.2 If another balise group marked as unlinked is received before the additional confidence interval is deleted: [¶734]

- the additional confidence interval shall be reset in relation to this new balise group marked as unlinked [¶735]

- the  location  related  information  referred  to  the  previous  balise  group  marked  as unlinked shall be relocated by subtracting the estimated travelled distance between both  balise  groups  from  the  distances  that  are  counted  from  this  previous  balise group marked as unlinked. [¶736]

# 3.6.5 Position Reporting to the RBC [¶737]

# 3.6.5.1 General [¶738]

- 3.6.5.1.1 The position shall refer to the front end of the respective engine with regards to the train orientation. [¶739]


---
<!-- pagina 72 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶740]

- 3.6.5.1.1.1 Intentionally deleted. [¶741]

- 3.6.5.1.2 The position report shall contain at least the following position and direction data [¶742]

- The distance between the LRBG and the estimated front end of the train. [¶743]

- The distance from the estimated front end position to the min safe front end position and the distance from the estimated front end position to the max safe front end position. [¶744]

-  The identity of the location reference, the LRBG. [¶745]

- The orientation of the train in relation to the LRBG orientation. Note: Driver selected running direction is only handled by the on-board system. [¶746]

- The position of the front end of the train in relation to the LRBG (nominal or reverse side of the LRBG). [¶747]

-  The estimated speed [¶748]

- Train integrity information. [¶749]

- Direction of train movement in relation to the LRBG orientation [¶750]

- Optionally, the previous LRBG (see 3.4.2.3.3). [¶751]


---
<!-- pagina 73 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶752]

![](images/image_0024.png)

LRBG orientation [¶753]

nominal reverse c) [¶754]

LRBG identity d) [¶755]

Train orientation in relation to LRBG [¶756]

nominal reverse Active cab distance [¶757]

Estimated distance travelled [¶758]

b) [¶759]

distance [¶760]

to min safe [¶761]

front end to max safe front end [¶762]

# Figure  14:  Information  given  in  a  position  report  (two  examples  to  show  the relation between LRBG and train orientation) [¶763]

- 3.6.5.1.3 Intentionally deleted. [¶764]

- 3.6.5.1.4 The on-board equipment shall send position reports as requested by the RBC in the position report parameters. In addition, it shall also send a position report if at least one of the events listed hereafter occurs: [¶765]

- The train reaches standstill, if applicable to the current mode. [¶766]

- The mode changes. [¶767]

-  The driver confirms train integrity. [¶768]

- A loss of train integrity is detected. [¶769]

- The train passes a RBC/RBC border with its min safe rear end. [¶770]

-  The train passes with its min safe rear end a level transition border which led to a transition from level 2/3 to level 0, NTC or 1. [¶771]

- The level changes. [¶772]

a) [¶773]


---
<!-- pagina 74 -->

- A communication session is successfully established. [¶774]

- Intentionally moved. [¶775]

- The  train  passes  an  LRBG  compliant  balise  group  (see  3.6.2.2.2),  if  no  position report parameters are stored on-board. [¶776]

-  The train passes a RBC/RBC border with its max safe front end. [¶777]

- An error as defined in 3.16.4 is detected. [¶778]

- 3.6.5.1.4.1 If the position report results from one or more events listed in 3.6.5.1.4, its content shall reflect the consequences of these events. [¶779]

- 3.6.5.1.5 For  the  position  report  parameters  requested  by  the  RBC  the  following  possibilities shall be available, individually or in combination [¶780]

- Periodically in time. [¶781]

- Periodically in space. [¶782]

-  When  the  max  safe  front  end  or  min  safe  rear  end  of  the  train  has  passed  a specified location. [¶783]

- At every passage of an LRBG compliant balise group (see 3.6.2.2.2). [¶784]

- Immediately. [¶785]

- 3.6.5.1.5.1 Note: d) and e) can not be combined. [¶786]

- 3.6.5.1.6 Deleted. [¶787]

- 3.6.5.1.7 The  given  position  report  parameters  shall  be  valid  until  new  parameters  are  given from the RBC. [¶788]

- 3.6.5.1.8 The mode and level reported in a position report shall be consistent (e.g., no mode that relates to the previous level). [¶789]

# 3.6.5.2 Report of Train Rear End Position for Level 3 [¶790]

- 3.6.5.2.1 Train integrity information shall be given by external device or by driver. [¶791]

- 3.6.5.2.2 Driver input of train integrity shall only be permitted at standstill. [¶792]

- 3.6.5.2.3 The train integrity information shall consist of [¶793]

- Train integrity status information [¶794]

-  No train integrity information [¶795]

-  Train integrity information confirmed by integrity monitoring device [¶796]

-  Train integrity information confirmed (entered) by driver [¶797]

-  Train integrity lost [¶798]


---
<!-- pagina 75 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶799]

- Safe train length information (only valid if train integrity is confirmed at the same time). [¶800]

- 3.6.5.2.4 The safe train  length  information  shall  represent  the  distance  between  the  min  safe rear end (by subtracting the train length from the min. safe front end position at the time when integrity was established last time) and the estimated position of the train front. [¶801]

- 3.6.5.2.5 The safe train length information shall be re-calculated for every position report using the same last value of min safe rear end position until a new min safe rear end position is established on-board taking into account the time to detect train integrity. [¶802]

![](images/image_0025.png)

Figure 15: Calculation of Safe Train Length when train integrity was established [¶803]

# 3.6.6 Geographical position reporting [¶804]

- 3.6.6.1 The  ERTMS/ETCS  on-board  equipment  shall  display,  only  on  driver  request,  the geographical  position  of  the  estimated  front  end  of  the  train  in  relation  to  the  track kilometre.  The  display  of  the  geographical  position  shall  also  be  stopped  on  driver request. [¶805]

- 3.6.6.2 The resolution of the position indication shall be 1 metre (sufficient to allow the driver to report the train position when communicating with the signalman). [¶806]

- 3.6.6.3 When  receiving  new  geographical  position  information  (from  radio  or  from  balise group),  the  ERTMS/ETCS  on-board  equipment  shall  replace  the  currently  stored [¶807]


---
<!-- pagina 76 -->

geographical  position  information  (if  any)  by  this  new  received  one,  continuing  the ongoing geographical position calculation until at least one of the condition of 3.6.6.9 applies. [¶808]

- 3.6.6.4 Geographical  position  information  shall  always  use  a  balise  group  as  geographical position  reference  balise  group  and  if  needed  an  offset  from  that  balise  group.  A geographical position reference balise group shall be either: [¶809]

- part of the last reported balise groups memorised on-board, in case the information is transmitted by radio, OR [¶810]

- the balise group transmitting the information, in case the information is transmitted by balise group, OR [¶811]

-  any balise group not yet passed at the time of reception of the information. [¶812]

- 3.6.6.4.1 In  case  the  information  is  received  by  radio  and  at  least  one  of  the  announced geographical  position  reference  balise  group(s)  is  part  of  the  last  reported  balise groups memorised on-board, the on-board equipment shall use the data related to the most recently reported balise group. [¶813]

- 3.6.6.4.2 From  the  currently  stored  geographical  position  information,  the  track  kilometre reference  given  for  a  geographical  reference  location  shall  become  applicable  if  the train  has  detected  the  related  geographical reference balise group and has travelled the offset distance from this reference balise group. [¶814]

- 3.6.6.4.3 The announced and not applicable geographical references shall be deleted on-board if the train changes orientation. [¶815]

- 3.6.6.5 The  distance  travelled  from  the  geographical  reference  location  shall  be  taken  into account when calculating the geographical position. [¶816]

- 3.6.6.6 In  cases  where  the  track  kilometre  is  not  incremental  (jumps,  changes  in  counting direction,  scaling  error)  the  reported  position  might  be  wrong  between  the  point  of irregularity and the next new reference. [¶817]

- 3.6.6.7 In cases where single balise groups are used as a reference for geographical position information and where no linking information is available (and therefore no orientation can  be  assigned  to  the  balise  group),  the  on-board  equipment  shall  ignore  the geographical position information related to these single balise groups. [¶818]

- 3.6.6.8 Intentionally deleted. [¶819]

- 3.6.6.9 The on-board equipment shall continue calculating the position from a track kilometre reference (i.e. this track kilometre reference shall remain applicable) until: [¶820]

- a new track kilometre reference becomes applicable, OR [¶821]

- it is told not to do so, OR [¶822]

-  the calculated geographical position becomes negative, OR [¶823]


---
<!-- pagina 77 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶824]

- no  more  geographical  position  information  is  available  (e.g.,  deleted  according  to conditions in SRS chapter 4) [¶825]

- 3.6.6.9.1 Once a track kilometre reference is no longer applicable, it shall be deleted. [¶826]

- 3.6.6.10 The following data shall be included in a message for geographical position (for every track kilometre reference): [¶827]

-  Identity of the geographical position reference balise group [¶828]

-  Distance from geographical position reference balise group to the track kilometre reference (offset) [¶829]

-  Value of the track kilometre reference [¶830]

-  Counting  direction  of  the  track  kilometre  in  relation  to  the  geographical  position reference balise group orientation. [¶831]

![](images/image_0026.png)

Figure 16: Geographical position example [¶832]

# 3.7 Completeness of data for safe train movement [¶833]

# 3.7.1 Completeness of data [¶834]

- 3.7.1.1 To control the train movement in an ERTMS/ETCS based system the ERTMS/ETCS on-board  equipment  shall  be  given  information  from  the  trackside  system  both concerning  the  route  set  for  the  train  and  the  track  description  for  that  route.  The following information shall be given from the trackside [¶835]

- Permission and distance to run, the Movement Authority (MA) (see section 3.8) [¶836]

- When needed, limitations related to the movement authority, i.e. Mode profile for On Sight, Limited Supervision or Shunting and signalling related speed restriction (see [¶837]


---
<!-- pagina 78 -->

sections  3.12.4  and  3.11.6).  Mode  profile  and  Signalling  related  Speed  restriction shall always be sent together with the MA to which the information belongs [¶838]

-  Track  description  covering  as  a  minimum  the  whole  distance  defined  by  the  MA. Track description includes the following information [¶839]

-  The Static Speed Profile (SSP) (see section 3.11.3). [¶840]

-  The gradient profile (see section 3.11.12). [¶841]

-  Optionally Axle load Speed Profile (ASP) (see section 3.11.4) [¶842]

-  Optionally  Speed  restriction  to  ensure  a  given  permitted  braking  distance  (see section 3.11.11) [¶843]

-  Optionally track conditions (see section 3.12.1). [¶844]

-  Optionally route suitability data (see section 3.12.2). [¶845]

-  Optionally areas where reversing is permitted (see section 3.15.4). [¶846]

-  Optionally changed adhesion factor (see section 3.18.4.5.5). [¶847]

- Linking information when available. [¶848]

# 3.7.2 Responsibility for completeness of information [¶849]

- 3.7.2.1 The Movement Authority (MA) shall be given to the on-board equipment [¶850]

-  Together with the other information ( as listed in section 3.7.1.1 c) and d)) or [¶851]

-  Separately, if the other information has already been correctly received by the onboard equipment. [¶852]

- 3.7.2.2 The trackside shall be responsible for that the on-board equipment has received the information valid for the distance covered by the Movement Authority. [¶853]

- 3.7.2.2.1 In  case  of  LOA,  trackside  shall  be  responsible  for  including  any  track  description beyond the LOA relevant for calculating safe supervision limits. [¶854]

- 3.7.2.3 The MA and the related mode profile, if any, shall not be accepted by the on-board equipment if the SSP and gradient already available on-board or given together with the MA do not cover the full length of the MA. [¶855]

- 3.7.2.3.1 Full length means at least from the estimated front end of the train to the supervised location. [¶856]

- 3.7.2.4 It shall be possible for the trackside to send additional information when needed. The information referred to is [¶857]

-  Emergency messages (from RBC only) [¶858]

-  Request to stop earlier (from RBC only) [¶859]

-  Temporary speed restrictions [¶860]

-  National values [¶861]


---
<!-- pagina 79 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶862]

-  Level transition information [¶863]

-  LX speed restrictions [¶864]

-  Inhibition of revocable TSRs from balises in L2/3 (from RBC only) [¶865]

-  Virtual Balise Cover orders [¶866]

# 3.7.3 Extension, replacement of track description and linking information [¶867]

- 3.7.3.1 New track description and linking information shall replace (in the ERTMS/ETCS onboard equipment) stored information as detailed below: [¶868]

- New Static  Speed  Profile  information  shall  replace  all  stored  Static  Speed  Profile information from the start location of the new information. [¶869]

- New Gradient Profile information shall replace all stored Gradient Profile information from the start location of the new information. [¶870]

-  New Axle Load Speed Profile information shall replace all stored Axle Load Speed Profile information from the start location of the first element of the new information. [¶871]

- New  Speed  Restriction  to  ensure  Permitted  Braking  Distance  information  shall replace all stored Speed  Restriction to ensure Permitted Braking Distance information from the start location of the first element of the new information. [¶872]

- New track condition Change of Traction System information shall replace all stored Change of Traction System information. [¶873]

-  New track condition Big Metal Masses information shall replace all stored Big Metal Masses  information  from  the  start  location  of the first  element  of  the  new information. [¶874]

- New track condition information of at least one of the types listed here, i.e., sound horn, non stopping area, tunnel stopping area, powerless section -lower pantograph,  powerless  section  -  switch  off  the  main  power  switch,  radio  hole,  air tightness,  switch  off  regenerative  brake,  switch  off  eddy  current  brake  for  service brake, switch off eddy current brake for emergency brake, switch off magnetic shoe brake, shall replace all stored track condition information of the listed types from the start location of the first element of the new information. [¶875]

- New  route  suitability  loading  gauge  information  shall  replace  all  stored  route suitability loading gauge information. [¶876]

- New  route  suitability  traction  system  information  shall  replace  all  stored  route suitability traction system information. [¶877]

- New route suitability  axle  load  information  shall  replace  all  stored  route  suitability axle load information. [¶878]

-  New reversing area information shall replace all stored reversing area information. [¶879]

- New adhesion factor information shall replace all stored adhesion factor information from the start location of the new information. [¶880]


---
<!-- pagina 80 -->

-  New  linking  information  received  as  non-infill  information  shall  replace  all  stored linking information from the LRBG. [¶881]

- New linking information received as infill information shall replace all stored linking information from the reference location of the infill information (i.e. the balise group at next main signal). [¶882]

- New  track  condition  Station  Platform  information  shall  replace  all  stored  Station Platform  information  from  the  start  location  of  the  first  element  of  the  new information. [¶883]

- New  track  condition  Allowed  Current  Consumption  information  shall  replace  all stored Allowed Current Consumption information. [¶884]

- 3.7.3.1.1 Intentionally deleted. [¶885]

- 3.7.3.1.2 Intentionally deleted. [¶886]

- 3.7.3.2 When requested  by  trackside,  the  ERTMS/ETCS  on-board  equipment  shall  resume initial states beyond a given location individually: [¶887]

- for stored Speed Restriction to ensure Permitted Braking Distance information (for initial state, refer to 3.11.11.11) [¶888]

- for stored axle load speed profile information (for initial state, refer to 3.11.4.5) [¶889]

-  through a single request, for all stored track condition information of the following types:  sound  horn,  non  stopping  area,  tunnel  stopping  area,  powerless  section  lower pantograph, powerless section - switch off the main power switch, radio hole, air tightness, switch off regenerative brake, switch off eddy current brake for service brake, switch off eddy current brake for emergency brake and switch off magnetic shoe brake (for initial states, refer to 3.12.1.3) [¶890]

- through a single request, for all stored route suitability information (for initial state, refer to 3.12.2.10). [¶891]

- through a single request, for all stored track condition information of the type Station Platform (for initial state, refer to 3.12.1.3). [¶892]

- 3.7.3.3 In  some  situations,  the  track  description  and  linking  information  shall  be  deleted  (or initial state shall be resumed) by the on-board equipment. These various cases where the  data  is  affected  (e.g.  the  MA  is  shortened)  are  described  in  detail  in  Appendix A.3.4. [¶893]

- 3.7.3.4 Intentionally deleted. [¶894]

- 3.7.3.5 Deleted. [¶895]

- 3.7.3.6 Note: regarding the handling of Temporary Speed Restrictions and Level Crossings, see sections 3.11.5 and 3.12.5. [¶896]


---
<!-- pagina 81 -->

# 3.8 Movement authority [¶897]

# 3.8.1 Characteristics of a MA [¶898]

- 3.8.1.1 The following characteristics can be used in a Movement Authority (see Figure 17: Structure of an MA): [¶899]

- The End of Movement Authority is the location to which the train is authorised to move. [¶900]

- When  the  Target  Speed  at  the  End  of  Movement  Authority  is  zero,  the  End  of Movement Authority is called EOA (End of Authority); when the target speed is not zero, it is called the LOA (Limit of Authority). This non zero target speed can be time limited. [¶901]

-  If  no  overlap  exists,  the  Danger  Point  is  a  location  beyond  the  End  of  Movement Authority  that  can  be  reached  by  the  front  end  of  the  train  without  a  risk  for  a hazardous situation. [¶902]

- The  end  of  an  overlap  (if  used  in  the  existing  interlocking  system)  is  a  location beyond the Danger Point that can be reached by the front end of the train without a risk  for  a  hazardous  situation.  This  additional  distance  is  only  valid  for  a  defined time. [¶903]

- A release speed is a speed limit under which the train is allowed to run in the vicinity of  the  End  of  Movement  Authority,  when  the  target  speed  is  zero.  One  release speed can be associated with the Danger Point, and another one with the overlap. Release speed can also be calculated on-board the train (see section 3.13.9.4). [¶904]

-  The MA can be split into several sections, The last one is called End Section. [¶905]

-  A first time-out value can be attached to each section. This value will be used for the revocation of the associated route when the train has not entered into it yet. It is called the Section time-out. [¶906]

-  In addition, a second time-out value can be attached to the End Section of the MA. This second time-out will be used for the revocation of the last section when it is occupied by the train; it is called the End Section time-out. [¶907]

- 3.8.1.2 The values of the time-outs possibly given in an MA shall take into account the time elapsed from the start of validity of information to the sending of the message. [¶908]

- 3.8.1.3 Note: A Danger Point can be (not exhaustive list): [¶909]

-  the  entry  point  of  an  occupied  block  section  (if  the  line  is  operated  according  to fixed block principles) [¶910]

-  the  position  of  the  safe  rear  end  of  a  train  (if  the  line  is  operated  according  to moving block principles) [¶911]


---
<!-- pagina 82 -->

-  the  fouling  point  of  a  switch,  positioned  for  a  route,  conflicting  with  the  current direction  of  movement  of  the  train  (both  for  fixed  and  moving  block  mode  of operation) [¶912]

- 3.8.1.4 Note: Traditionally the overlap is a piece of track (beyond the danger point), that is put at disposal of a train, to guarantee a non hazardous situation, also in case the driver should misjudge the stopping distance for the train. In ERTMS/ETCS the overlap can be used to improve the efficiency of the braking supervision. [¶913]

- 3.8.1.5 Note:  Time-out  values  can  be  given  in  the  MA  to  cope  with  the  following  situations depending on the interlocking operations, i.e. the timers on-board will only reflect the situation trackside and when expired (on-board) the actions taken are restrictive: [¶914]

- Section time-out or time-out for the speed at the LOA: When a signalman requests a route release of a part of a route not yet entered by the approaching train. [¶915]

- End  Section  time-out:  When  the  train  has  entered  the  last  part  of  a  route,  the automatic route release can be delayed to make sure that the train has come to a standstill before any switches inside the route can be moved. [¶916]

-  Time-out  for  an  overlap:  When  the  train  has  entered  the  last  part  of  a  route,  the overlap associated with the route remains valid for a certain time to make sure that the  train  has  successfully  stopped  before  its  End  of  Movement  Authority.  If  the overlap  is  still  unoccupied  when  the  timer  expires  the  interlocking  revokes  the overlap. [¶917]

- 3.8.1.6 Note: If the trackside equipment does not have enough information to give the distance to  the  End  of  Movement Authority with a target speed equal to zero, a target speed higher than zero can be given (LOA, Limit of Authority). It is the responsibility of the trackside to ensure that the safe distance beyond the LOA is long enough to brake the train  from  the  target  speed  to  a  stand  still  without  any  hazardous  situation.  It  is  the responsibility of the on-board equipment to apply the brakes if no new information is received when the Limit of Authority is passed. [¶918]

# 3.8.2 MA request to the RBC [¶919]

- 3.8.2.1 It shall be possible for the on-board equipment to request a new Movement Authority from the RBC. [¶920]

- 3.8.2.2 The parameters for requesting a new MA shall be given by the RBC. [¶921]

- 3.8.2.3 In level 2/3, the following possibilities shall be available: [¶922]

- A  defined  time  before  the  train  reaches  the  perturbation  location  assuming  it  is running at the warning speed (see section 3.13.11 for details). [¶923]

- A defined time before the Section timer (not the End Section timer, not the Overlap timer) for any section of the MA expires, or before the LOA speed timer expires. [¶924]


---
<!-- pagina 83 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶925]

- 3.8.2.3.1 Regards to the above possibilities, the MA request shall be triggered when the train front has passed the resulting location (regards a)/ time (regards b) [¶926]

- 3.8.2.4 The parameters given by the RBC also define whether the MA request shall be repeated until a new MA is received or not and if so, the time between each repetition. [¶927]

- 3.8.2.5 The given data shall be valid until new MA request parameters are given from the RBC. [¶928]

- 3.8.2.6 In case no MA request parameters are stored on-board and following an MA request no MA has been received, the request shall be repeated with a repetition cycle according to a fixed value (see appendix). [¶929]

- 3.8.2.7 In level 2/3: an MA request shall be sent to the RBC when the driver selects start. [¶930]

- 3.8.2.7.1 In level 0, 1, NTC: if a level 2/3 transition is announced and a communication session is already established, an MA request shall be sent to the RBC when the information "Track ahead free up to level 2/3 transition location" is received from balise group. [¶931]

- 3.8.2.7.2 In level 0, 1, NTC: the ERTMS/ETCS on-board equipment shall also inform the RBC about the identity of the level 2/3 transition location balise group, as received through the information "Track ahead free up to level 2/3 transition location". [¶932]

- 3.8.2.7.3 In  level  2/3:  An  MA  request  shall  be  sent  to  the  RBC  when  any  part  of  the  track description is deleted according to A.3.4, except for situations a, b, f, k. [¶933]

- 3.8.2.8 Together with the MA request the on-board shall inform the RBC about the reason(s) why the MA request is sent: [¶934]

- Start selection by driver, [¶935]

- Time before reaching perturbation location reached, [¶936]

-  Time before a section timer or the LOA speed timer expires reached, [¶937]

- The track description has been deleted, [¶938]

- Track ahead free up to level 2/3 transition location. [¶939]

# 3.8.3 Structure of a Movement Authority (MA) [¶940]

- 3.8.3.1 The distance to the End of Movement Authority can be composed of several sections. [¶941]

- 3.8.3.2 For each section composing the MA the following information shall be given; [¶942]

- Length of the section [¶943]

- Optionally, Section time-out value and distance from beginning of section to Section timer stop location [¶944]

- 3.8.3.3 In addition, it shall be possible to define for the End Section of the MA: [¶945]


---
<!-- pagina 84 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶946]

- End Section time-out value and distance from the End Section timer start location to the end of the last section [¶947]

- Danger  point  information  (distance  from  end  of  section  to  danger  point,  release speed related to danger point) [¶948]

-  Overlap  information  (distance  from  end  of  section  to  end  of  overlap,  time-out, distance from Overlap timer start location to end of section, release speed related to overlap) [¶949]

- 3.8.3.3.1 Note: If only one section is given in the MA it is regarded as the End Section. [¶950]

- 3.8.3.4 The Section timer stop location shall be inside of the corresponding section. [¶951]

- 3.8.3.4.1 Note:  the  End  Section  and  Overlap  timer  start  locations  may  be  outside  their corresponding section. One example can be seen referring to figure 22c: An infill MA towards  a  signal  at  stop  will  replace  the  previous  End  Section  by  a  new  short  End Section  starting  at  the  infill  location  reference  and  ending  at  the  next  main  signal, however the End Section and Overlap timer start locations still have to be consistent with  the  Interlocking  timer  start  locations.  Another  example  is  when  a  timer  start location is in rear of the LRBG. [¶952]

- 3.8.3.5 In level 3, no time-outs shall be used. [¶953]

- 3.8.3.5.1 Note:  For  level  3  functionality  the  split  of  responsibility  between  the  RBC  and  the Interlocking has to be considered. Time-out of routes and related overlap can not be based on train position reports since the position report can be delayed compared to [¶954]

![](images/image_0027.png)

Figure 17: Structure of an MA [¶955]


---
<!-- pagina 85 -->

the  real  position  of  the  train.  The  route  release  and  revocation  of  routes  can  not  be carried out by the interlocking until permitted by the RBC. [¶956]

- 3.8.3.6 When an MA is transmitted by a balise group, the length of the first section shall refer to the balise co-ordinate system of that balise group. [¶957]

- 3.8.3.7 In case a main signal is at danger in level 1, the first section shall give the distance from  the  balise  group  at  the  main  signal  to  the  location  of  the  main  signal,  i.e.  the distance to EOA is given. Where available, information concerning danger point and overlap for this EOA may also be given. [¶958]

- 3.8.3.7.1 Justification:  The  balise  group  is  not  necessarily  placed  at  the  same  location  as  the signal and thus an infill message (which includes the same information as the balise group at the main signal) could change the location of the EOA to a position closer to the train. [¶959]

- 3.8.3.8 Note: In case the main signal is at danger in level 1, the on-board will supervise the given distance (specified in section 3.8.3.7) as the distance to EOA. [¶960]

- 3.8.3.9 When an MA is transmitted by radio from the RBC, the length of the first section shall refer to the balise co-ordinate system of the LRBG given in the same message. [¶961]

- 3.8.3.10 It shall be possible to give the length of a section to any location in the track. [¶962]

- 3.8.3.10.1  Note:  A  section  can  cover  several  blocks  and  is  not  restricted  to  block  ends  (see figures). [¶963]

![](images/image_0028.png)

Figure 18: Distance to End of Movement Authority when no time-outs are needed [¶964]


---
<!-- pagina 86 -->

![](images/image_0029.png)

# Figure  19  :  Distance  to  End  of  Movement  Authority  when  time-outs  might  be needed [¶965]

- 3.8.3.11 In  moving  block  operation  the  MA  shall  never  exceed  the  min  safe  rear  end  of  the preceding train. [¶966]

![](images/image_0030.png)

Figure 20: MA in moving block operation. [¶967]

# 3.8.4 Use of the MA on board the train [¶968]

# 3.8.4.1 End Section Time-Out [¶969]

- 3.8.4.1.1 The  End  Section  timer  shall  be  started  on-board  when  the  train  passes  the  End Section timer start location given by trackside with its max safe front end. [¶970]

- 3.8.4.1.2 When the End Section timer value becomes greater than the time-out value given by trackside, the following shall apply: [¶971]

- The  EOA/LOA  shall  be  withdrawn  to  the  current  position  of  the  train.  Refer  to appendix A.3.4 for the exhaustive list of location based information stored on-board, which shall be deleted accordingly; [¶972]

- if any, a non zero target speed value at the End of Movement Authority shall be set to zero (i.e. an LOA at the End of Movement Authority becomes an EOA withdrawn to the current position of the train). [¶973]

- 3.8.4.1.3 In case no End Section timer is running when the on-board receives a new MA with an End Section timer start location in rear of the max safe front end of the train, the onboard shall consider that the End Section timer value became greater than its time-out value and apply 3.8.4.1.2. [¶974]


---
<!-- pagina 87 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶975]

- 3.8.4.1.3.1 Justification:  in  this  case  the  train  is  already  beyond  the  timer  start  location, therefore  it  is  impossible  to  determine  when  that  location  was  crossed  and  so  what share of the time-out value has elapsed since the crossing event. The safe assumption is  to  consider that the time-out value has been exceeded and therefore that the End Section will soon be released by the Interlocking. [¶976]

- 3.8.4.1.4 In case an End Section timer is already running when the on-board receives a new MA with an End Section timer start location in rear of the max safe front end of the train, the on-board shall keep the End Section timer running but replace the time-out value with the value received with the new MA. [¶977]

- 3.8.4.1.4.1 Justification:  this  allows  repetition  of  the  MA  via  RBC  (e.g.  acknowledgment  of current MA was lost) without unintentionally affecting the End Section timer. [¶978]

# 3.8.4.2 Section Time-Outs [¶979]

- 3.8.4.2.1 The on-board shall start a Section timer for each section: [¶980]

- For Level 2: at the value of the time stamp of the message including the MA. [¶981]

- For Level 1: at the time of passage over the first encountered balise of the balise group giving the MA. [¶982]

- 3.8.4.2.1.1 Justification for b): This is to ensure that the timer is always started before or at the same  time  as  the  related  variable  information  is  received.  Thus  the  timer  start  is independent of in which balise the variable information is given. [¶983]

- 3.8.4.2.2 When  a  Section  timer  value  becomes  greater  than  the  time-out  value  given  by trackside, the following shall apply: [¶984]

- the  EOA/LOA  and  the  SvL  shall  be  withdrawn  to  the  entry  point  of  the  revoked section. Refer to appendix A.3.4 for the exhaustive list of location based information stored on-board, which shall be deleted accordingly; [¶985]

- the National/ Default Value of the Release Speed shall apply ; [¶986]

-  if any, a non zero target speed value at the End of Movement Authority shall be set to zero (i.e. an LOA at the End of Movement Authority becomes an EOA withdrawn to the entry point of the revoked section). [¶987]

- 3.8.4.2.2.1 Intentionally deleted. [¶988]

- 3.8.4.2.3 The Section timer shall be stopped when the min safe front end of the train has passed the associated Section timer stop location. [¶989]

# 3.8.4.3 Time-out  of  the  speed  associated  with  the  End  of  Movement  Authority  (LOA speed time out) [¶990]

- 3.8.4.3.1 The on-board shall start a timer for the LOA speed: [¶991]

- For Level 2: at the value of the time stamp of the message including the MA. [¶992]


---
<!-- pagina 88 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶993]

- For Level 1: at the time of passage over the first encountered balise of the balise group giving the MA. [¶994]

- 3.8.4.3.1.1 Justification for b): This is to ensure that the timer is always started before or at the same  time  as  the  related  variable  information  is  received.  Thus  the  timer  start  is independent of in which balise the variable information is given. [¶995]

- 3.8.4.3.2 When the LOA speed timer value becomes greater than the time-out value given by trackside,  the  speed  associated  with  the  LOA  shall  be  set  to  zero  (i.e.  the  Limit  of Authority becomes an End of Authority and the SvL is defined on-board according to 3.8.4.5). Refer to appendix A.3.4 for the exhaustive list of location based information stored on-board, which shall be deleted accordingly. [¶996]

# 3.8.4.4 Time-out of Overlap [¶997]

- 3.8.4.4.1 The Overlap timer shall be started on-board when the train passes the Overlap timer start  location  given  by  trackside  with  its  max  safe  front  end.  The  timer  shall  be considered as started even if a time-out value 'infinite' is given. [¶998]

- 3.8.4.4.2 When  the  Overlap  timer  value  becomes  greater  than  the  time-out  value  given  by trackside, the following shall apply: [¶999]

- the  overlap  information  shall  be  deleted  and  the  Supervised  Location  shall  be determined in accordance with 3.8.4.5. Refer to appendix A.3.4 for the exhaustive list of location based information stored on-board, which shall be deleted accordingly. [¶1000]

- the release speed associated with the Overlap shall be deleted [¶1001]

-  if any, a non zero target speed value at the End of Movement Authority shall be set to zero (i.e. an LOA at the End of Movement Authority becomes an EOA). [¶1002]

- 3.8.4.4.3 If the train comes to a standstill after the Overlap timer has been started, the on-board shall consider that the Overlap timer value became greater than its time-out value and shall apply 3.8.4.4.2. [¶1003]

- 3.8.4.4.4 In  case  no  Overlap  timer  is  running  when  the  on-board  receives  a  new  MA  with  an Overlap timer start location in rear of the max safe front end of the train, the on-board shall consider that the Overlap timer value became greater than its time-out value and shall apply 3.8.4.4.2. [¶1004]

- 3.8.4.4.4.1 Justification:  in  this  case  the  train  is  already  beyond  the  timer  start  location, therefore  it  is  impossible  to  determine  when  that  location  was  crossed  and  so  what share of the time-out value has elapsed since the crossing event. The safe assumption is  to  consider  that  the  time-out  value  has  been  exceeded  and  therefore  that  the Overlap will soon be released by the Interlocking. [¶1005]

- 3.8.4.4.5 In case an Overlap timer is already running when the on-board receives a new MA with an Overlap timer start location in rear of the max safe front end of the train, the on- [¶1006]


---
<!-- pagina 89 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1007]

board shall keep the Overlap timer running but replace the Overlap time-out value with the value received with the new MA. [¶1008]

- 3.8.4.4.5.1 Justification:  this  allows  repetition  of  the  MA  via  RBC  (e.g.  acknowledgment  of current MA was lost) without unintentionally affecting the Overlap timer. [¶1009]

# 3.8.4.5 Supervised Location [¶1010]

- 3.8.4.5.1 The Supervised Location (SvL) shall be defined on-board as: [¶1011]

- the end of overlap (if any and before time-out). [¶1012]

- if not, the Danger Point (if any). [¶1013]

-  if not, the End Of Authority. [¶1014]

- 3.8.4.5.2 As long as a Limit of Authority is supervised, no SvL shall be defined on-board. [¶1015]

# 3.8.4.6 Infill MA (level 1 only) [¶1016]

- 3.8.4.6.1 An MA given by an infill device is called an infill MA. [¶1017]

- 3.8.4.6.2 An infill MA shall be evaluated on-board only if the on-board equipment is in FS or LS mode. [¶1018]

- 3.8.4.6.3 The  infill  information  shall  include  the  identity  of  the  balise  group  at  the  next  main signal i.e. the identity of the balise group giving the information that is transmitted in advance by the infill device. [¶1019]

- 3.8.4.6.4 An infill  MA shall be evaluated on-board only if the linking information, regarding the main signal balise group to which it refers, is available. [¶1020]

- 3.8.4.6.5 The on-board shall start a Section timer for each section beyond the next main signal: [¶1021]

- When the infill information is received from a balise group at the time of passing the first encountered balise of the infill balise group. [¶1022]

- When the infill information is received from a loop at the time of receiving the loop message. [¶1023]

-  When the infill information is received from a radio infill unit at the value of the time stamp of the radio infill message including the MA. [¶1024]

# 3.8.5 MA Update [¶1025]

- 3.8.5.1 A new MA shall replace a previously received MA in the following ways: [¶1026]

- When the new MA is given from a balise group at a main signal (i.e. not infill information) or from the RBC all data included in the previous MA shall be replaced by the new data. [¶1027]

- When the new MA is given as infill information all data beyond the announced balise group at the next main signal shall be replaced. [¶1028]


---
<!-- pagina 90 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1029]

- 3.8.5.1.1 Note: This refers to all information included in the MA as listed in section 3.8.1.1 and the Signalling related speed restriction (see section 3.11.6). [¶1030]

- 3.8.5.1.2 When an infill MA is received, the on-board shall start a new MA section at the infill location reference, i.e. the balise group at the next main signal (see 3.6.2.3.1). [¶1031]

- 3.8.5.1.3 If the SvL defined from the new MA is closer than the one supervised with the former MA, this shall be considered by the on-board equipment as an MA shortening. Refer to appendix A.3.4 for the exhaustive list of location based information stored on-board, which shall be deleted accordingly. [¶1032]

- 3.8.5.1.4 If  a  new  MA  defines  an  SvL  while  the  on-board  was  supervising  an  LOA,  this  shall always be considered by the on-board equipment as an MA shortening regardless of the  SvL  location.  Refer  to  appendix  A.3.4  for  the  exhaustive  list  of  location  based information stored on-board, which shall be deleted accordingly. [¶1033]

- 3.8.5.2 It  shall  be  possible  to  update the length of  an MA section by means of repositioning information contained in a balise group message (see section 3.8.5.3). [¶1034]

- 3.8.5.2.1 Note: The concerned MA section need not be the end section. [¶1035]

- 3.8.5.2.2 Upon  reception  of  repositioning  information and  only  if linking  information  has announced a following balise group as unknown but containing repositioning information, the on-board shall update the length of the current MA section in which the train front end is. [¶1036]

- 3.8.5.2.3 A balise group message containing a movement authority shall not contain repositioning information for the same direction. [¶1037]

- 3.8.5.2.3.1 Note: It is possible to combine repositioning with an infill MA. [¶1038]

- 3.8.5.2.4 The reception of repositioning information or of a new MA with an LOA shall not be considered as an MA shortening by the on-board equipment. [¶1039]

# 3.8.5.3 Examples of MA update [¶1040]

- 3.8.5.3.1 Note: In the following examples on how to update an MA are given. The examples are not exhaustive. [¶1041]

- 3.8.5.3.2 Example: Extension of MA via a main balise group in Level 1 [¶1042]

-  by giving a new longer section, see Figure 21a [¶1043]

-  by giving a first section to the same location as in the previous MA and a second section, see Figure 21b [¶1044]


---
<!-- pagina 91 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1045]

![](images/image_0031.png)

Figure 21a: Extension of an MA in Level 1, one section in the new MA [¶1046]

![](images/image_0032.png)

Figure 21b: Extension of an MA in level 1, two sections in the new MA [¶1047]

- 3.8.5.3.3 Example:  MA  update  via  infill  information  in  Level  1.  (Refer  to  section  3.6.2.3  for location reference of infill information) [¶1048]

-  MA extension, by giving two new sections, see Figure 22a [¶1049]

-  MA shortening, see Figure 22b [¶1050]

-  MA repetition, see Figure 22c [¶1051]


---
<!-- pagina 92 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1052]

![](images/image_0033.png)

Figure 22a: Extension of an MA with Infill information [¶1053]


---
<!-- pagina 93 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1054]

![](images/image_0034.png)

Figure 22b: Shortening of an MA with Infill information [¶1055]

![](images/image_0035.png)

Figure 22c: Repetition of an MA with Infill information [¶1056]

# 3.8.5.3.4 Example: Extension of MA in Levels 2 and 3 [¶1057]


---
<!-- pagina 94 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1058]

-  by using the same LRBG as in previous MA, see Figure 23a [¶1059]

-  by using a new LRBG, see Figure 23b [¶1060]

- 3.8.5.3.5 Example:  Extension  of  MA  in  level  1  using  a  balise  group  containing  repositioning information. [¶1061]

- 3.8.5.3.5.1 Note: In some existing systems, information about the locked route is not complete. [¶1062]

- 3.8.5.3.5.2 History of the situation (refer to the figure below): [¶1063]

- Signal A gives an aspect to proceed up to signal Cx because it has received information about the locked route. [¶1064]

- Signal A can determine whether track 3 or track 1 / 2 is locked but is unable to distinguish between track 1 and 2. [¶1065]

-  In the situation described the route is set to track 1 or 2. [¶1066]

![](images/image_0036.png)

Figure 23a: Extension of an MA in level 2/3, using same LRBG [¶1067]

![](images/image_0037.png)

Figure 23b: Extension of an MA in Level 2/3, using a new LRBG [¶1068]


---
<!-- pagina 95 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1069]

![](images/image_0038.png)

Figure 24: Information on set route not complete at signal A [¶1070]

- 3.8.5.3.5.3 In balise group A the following information is given: [¶1071]

- The most restrictive track description from all routes (which could be a combination from the routes); [¶1072]

- The  linking  distance  given  to  the  farthest  balise  group  containing  repositioning information, the identification of the repositioning balise group is not known; [¶1073]

-  For a given aspect of signal A, the most restrictive MA from all routes (the shortest sections  from  the  routes  and  the  lowest  target  speed  at  the  End  of  Movement Authority); [¶1074]

- If some sections are time limited, the most restrictive timer. [¶1075]

- 3.8.5.3.5.4 Balise groups B (B1 or B2) give the following static information: [¶1076]

- This is repositioning information [¶1077]

- Linking to the next balise group C [¶1078]

-  The distance to the end of the current section (i.e. the distance to the end of section B1 - C1, or the distance to the end of section B2 - C2) [¶1079]

- The track description related to this track. [¶1080]


---
<!-- pagina 96 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1081]

![](images/image_0039.png)

Figure 25: Information contained in A and B1 (for clarity purposes, only SSPs are drawn but the procedure has to be applied for all track description) [¶1082]

# 3.8.6 Co-operative shortening of MA (Level 2 and 3 only) [¶1083]

- 3.8.6.1 It shall be possible to shorten a given MA using a special procedure between on-board equipment and RBC. The procedure is as follows: [¶1084]

- The RBC proposes a new MA with an EOA closer to the train than the current EOA/LOA, optionally with a mode profile. [¶1085]


---
<!-- pagina 97 -->

- The ERTMS/ETCS on-board equipment shall check the train front end position versus the Indication supervision limit of the proposed shortened MA. [¶1086]

-  If it is in rear, the on-board equipment shall accept the new MA. [¶1087]

-  If it is in advance, the request shall be rejected and the previously received MA remains valid [¶1088]

-  The RBC shall be informed about the decision. [¶1089]

- 3.8.6.2 If the request from the RBC is granted by the on-board, refer to appendix A.3.4 for the exhaustive list of location based information, which shall be deleted accordingly. [¶1090]

# 3.9 Means to transmit Infill information (Level 1 only) [¶1091]

# 3.9.1 General [¶1092]

- 3.9.1.1 It shall be possible to transmit infill information to the on-board equipment using [¶1093]

- Balise groups [¶1094]

- Euroloops [¶1095]

-  Radio infill units. [¶1096]

- 3.9.1.1.1 If  the  information  transmitted  by  Balise  groups,  Euroloops,  and  Radio  includes  infill information, those devices are also identified as infill devices. [¶1097]

- 3.9.1.2 The  principle  used  for  the  infill  information  shall  be  the  same  independent  of transmission media. [¶1098]

- 3.9.1.3 If the on-board system is not equipped with the infill transmission media as requested by the announcement balise group, the announcement information shall be ignored by the  on-board  equipment  and  the  train  shall  proceed  according  to  the  previously received information. [¶1099]

- 3.9.1.4 Note: No additional description is needed for infill by balise group (other than already covered in previous chapters). [¶1100]

# 3.9.2 Infill by loop [¶1101]

- 3.9.2.1 An End Of Loop Marker (EOLM) is by definition a device to mark the beginning or the end of a loop. When receiving this information, the on-board equipment knows that it is entering/leaving  a  track  equipped  with  a  loop.  In  unidirectional  applications  it  is possible to have an EOLM only at the entry side of a loop. [¶1102]

- 3.9.2.2 Balise groups shall be used as EOLMs. They act as an EOLM by sending the EOLM information to the passing train. [¶1103]

- 3.9.2.3 EOLMs have an orientation that is identical to the balise group orientation. The general rules for balise orientation therefore also apply to EOLMs. [¶1104]


---
<!-- pagina 98 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1105]

- 3.9.2.4 EOLM information might be contained in a balise group that contains other information. [¶1106]

- 3.9.2.5 The EOLM shall send the identity of the announced loop. [¶1107]

- 3.9.2.6 The on-board shall only accept information coming from the loop with the announced identity. [¶1108]

- 3.9.2.7 Deleted. [¶1109]

- 3.9.2.8 Deleted. [¶1110]

- 3.9.2.9 The  following  information  shall  be  sent  in  advance  by  the  EOLM  to  prepare  for reception of the loop information: [¶1111]

-  Loop identity used to identify the loop. [¶1112]

-  Key to select the spread spectrum key necessary to receive the loop telegrams. [¶1113]

-  Distance to the loop giving the distance from the EOLM to the location from where on loop messages can be received. [¶1114]

-  Length  of  the  loop  giving  the  length  of  the  loop  over  which  messages  can  be received. [¶1115]

-  Indicator  telling  the  on-board  whether  the  orientation  of  the  loop  is  identical  or reverse to the orientation of the announcing EOLM. [¶1116]

- 3.9.2.10 The on-board shall be prepared to receive messages from the Euroloop after passing the EOLM. [¶1117]

- 3.9.2.11 When  the  on-board  equipment  reads  the  next  main  signal  balise  group  or  when  it detects  that  the  next  main  signal  balise  group  was  missed,  new  infill  information possibly received from the loop shall be ignored. [¶1118]

- 3.9.2.12 The  distances  given  in  an  EOLM  (distance  to  loop,  length  of  loop)  are  used  for diagnostic purpose only. They shall therefore not be used to restrict reception of loop telegrams to specific locations. [¶1119]

# 3.9.3 Infill by radio [¶1120]

- 3.9.3.1 In  level  1  areas  it  shall  be  possible  to  send  to  the  on-board  equipment  orders  to establish/terminate a communication session with a radio infill unit. [¶1121]

- 3.9.3.2 The orders shall be sent via balise groups or via Radio Infill units. [¶1122]

- 3.9.3.3 The order to establish a communication session shall be ignored: [¶1123]

- Intentionally deleted. [¶1124]

- If the on-board equipment does not include radio. [¶1125]

- 3.9.3.4 If  the  on-board  equipment  includes  radio,  the  communication  session  shall  be established using the same protocols and interfaces as for Level 2/3 operations. [¶1126]


---
<!-- pagina 99 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1127]

- 3.9.3.5 If the order to establish a communication session with a radio infill unit sent via balise groups is  received,  the  on-board  equipment  shall,  once  the  location  indicated  in  the order is reached: [¶1128]

- terminate  any  existing  communication  session(s)  with  RIU(s)  not  indicated  in  the order [¶1129]

- as soon as a new communication session can be handled, establish a communication session with the RIU indicated in the order [¶1130]

- 3.9.3.5.1 Intentionally deleted. [¶1131]

- 3.9.3.5.1.1 Intentionally deleted. [¶1132]

- 3.9.3.5.2 Intentionally deleted. [¶1133]

- 3.9.3.6 If the order to establish a communication session with a radio infill unit sent via Radio Infill unit is received, the on-board equipment shall: [¶1134]

- If only one RIU communication session is ongoing, maintain the existing communication session and establish a new one with the RIU indicated in the order. [¶1135]

- If  two  RIU  communication  sessions  are  ongoing,  maintain  the  communication session related to the current infill area, terminate the other one and establish a new one with the RIU indicated in the order. [¶1136]

- 3.9.3.6.1 Exception  (degraded  situation):  if  the  on-board  can  handle  only  one  communication session, the order shall be ignored. [¶1137]

- 3.9.3.7 A  Radio  Infill  Unit  shall  not  initiate  a  communication  session  with  an  on-board equipment. [¶1138]

- 3.9.3.8 The order to establish/terminate a communication session sent via balise groups shall be sent together with the following radio infill area information: [¶1139]

- Location  where  to  perform  the  action  (referred  to  the  balise  group  containing  the order).Note:  if  the  action  is  to  establish  a  communication  session,  this  location marks the beginning of the Radio Infill Area. [¶1140]

- Next  main  signal  balise  group  identifier  (ignored  by  the  on-board  if  the  action  is Terminate communication session).Note: the reference location of this balise group marks the end of the Radio Infill Area. [¶1141]

- 3.9.3.8.1 The  order  to  establish/terminate  a  communication  session  sent  via  Radio  Infill  units (see 3.5.3.6) shall not be sent together with any radio infill area information. [¶1142]

- 3.9.3.9 The  establishment  of  a  communication  session  for  radio  infill  shall  not  change  the operational level of the on-board i.e. the information in the balise group shall be taken into account as usual in level 1. [¶1143]

- 3.9.3.10 The on-board equipment shall inform the radio infill unit [¶1144]


---
<!-- pagina 100 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1145]

- As soon as the location indicated in the order sent via balise groups is passed (i.e. entry of the train in the infill area) [¶1146]

- As soon as the next main signal balise group indicated in the order sent via balise groups is read or the on-board equipment detects that it was missed. [¶1147]

- 3.9.3.11 The information sent to the radio infill unit by the on-board equipment shall include [¶1148]

- Train identity (ETCS-ID of the on-board equipment) [¶1149]

- Position report [¶1150]

-  Identifier of the next main signal balise group [¶1151]

- Time stamp [¶1152]

- 3.9.3.11.1  Justification: [¶1153]

- The train identity is used for conformity with other train to track messages [¶1154]

- The  identifier  of  the  next  main  signal  balise  group  allows  the  radio  infill  unit  to identify safely where the train is going, even in the case of a points area [¶1155]

- 3.9.3.12 As soon as the radio infill unit is informed that a train has entered an infill area under its responsibility, it shall [¶1156]

- Terminate a possible previous sending  of infill information to the  on-board equipment, AND [¶1157]

- Send cyclically the infill information corresponding to the message currently sent by the  next  main  signal  balise  group  indicated  in  the  information  from  the  on-board equipment. [¶1158]

- 3.9.3.12.1  Justification: case a) refers to the possibility that a report from the on-board equipment, after having passed the previous main signal, was lost. [¶1159]

- 3.9.3.12.2  Note: A Radio infill unit  may manage several signals, thus several Radio Infill Areas (see Figure 25a) [¶1160]


---
<!-- pagina 101 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1161]

![](images/image_0040.png)

-  NMBG = Next Main signal Balise Group [¶1162]

-  RIU1 manages Radio Infill Area 1 [¶1163]

-  RIU2 manages Radio Infill Area 2 and 3 [¶1164]

-  RIU3 manages Radio Infill Area 4 [¶1165]

# Figure 25a: Line equipped with radio infill. Example of radio infill area information transmitted by balise. [¶1166]

- 3.9.3.13 The  radio  infill  unit  shall  terminate  the  sending  of  infill  information  as  soon  as information  is  received,  that  the  on-board  equipment  has  read  the  next  main  signal balise group indicated in the order or that the on-board equipment has detected that it was missed. [¶1167]

- 3.9.3.14 The radio infill unit shall evaluate the time stamp according to the principles of section 3.16.3.2. [¶1168]

- The on-board equipment shall check the consistency of radio infill data, according to the principles of section 3.16.3.1 and 3.16.3.3. [¶1169]

- 3.9.3.15 When  the  on-board  equipment  reads  the  next  main  signal  balise  group  or  when  it detects  that  the  next  main  signal  balise  group  was  missed,  new  infill  information related to this balise group possibly received shall be ignored. [¶1170]

- 3.9.3.16 The  ERTMS/ETCS  on-board  equipment  shall  terminate  the  communication  session according to the orders received from the trackside (balise group or Radio Infill units) or when the level 1 is left. [¶1171]

- 3.9.3.17 Intentionally deleted. [¶1172]

# 3.10 Emergency Messages [¶1173]

# 3.10.1 General [¶1174]

- 3.10.1.1 Emergency messages shall be sent individually to each on-board equipment, either as high priority data or as normal priority data of the same radio connection, as described [¶1175]


---
<!-- pagina 102 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1176]

in  Euroradio  specification.  Only  emergency  messages  can  be  sent  as  high  priority data, not their acknowledgement or their revocation. [¶1177]

- 3.10.1.1.1  Justification: In case of hazardous events, it is possible to use high priority data in the radio connection between RBC and on-board equipment to get a quick reaction. [¶1178]

- 3.10.1.2 An emergency message shall contain an identifier decided by the trackside. [¶1179]

- 3.10.1.3 The same identifier shall be used in case the emergency message is repeated. [¶1180]

- 3.10.1.3.1  If  the  on-board  receives a new message with the same identifier it shall replace the previous one. [¶1181]

- 3.10.1.4 Each emergency message to an on-board equipment shall be acknowledged, using the corresponding emergency message identification number. [¶1182]

- 3.10.1.4.1  Note:  This  acknowledgement  informs  the  RBC  about  the  use  of  the  emergency message by on-board equipment and is independent from the general acknowledgement for track-to-train messages, as specified in section 3.16.3.5. [¶1183]

# 3.10.2 Emergency Stop [¶1184]

- 3.10.2.1 It  shall  be  possible  to  stop  a  train  with  a  conditional  or  an  unconditional  emergency stop message. [¶1185]

- 3.10.2.2 A  conditional  emergency  stop  message  shall  contain  the  information  of  a  new  stop location, referred to the LRBG. In case, when receiving this message [¶1186]

-  the train has already passed with its min safe front end the new stop location, the emergency stop message shall be rejected and the RBC shall be informed. [¶1187]

-  the train has not yet passed with its min safe front end the new stop location, the emergency stop message shall be accepted, however this location shall be used by the  onboard  to  define  a  new  EOA/SvL  only  if  not  beyond  the  current  EOA/LOA. Refer to appendix A.3.4 for the exhaustive list of location based information stored on-board, which shall be deleted accordingly. [¶1188]

- 3.10.2.3 When receiving an unconditional emergency stop message the train shall be tripped immediately. [¶1189]

- 3.10.2.4 New movement authority received after any accepted emergency stop message and before the emergency message has been revoked, shall be rejected. [¶1190]

- 3.10.2.5 Intentionally deleted. [¶1191]

- 3.10.2.6 Intentionally deleted. [¶1192]

# 3.10.3 Revocation of an Emergency Message [¶1193]

- 3.10.3.1 The  revocation  message  shall  refer  to  the  identity  of  the  concerned  emergency message. [¶1194]


---
<!-- pagina 103 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1195]

- 3.10.3.2 The  revocation  messages  shall  be  acknowledged  by  the  on-board  equipment, according to the general acknowledgement procedure (see section 3.16.3.5) [¶1196]

- 3.10.3.3 The revocation of an emergency message shall have no effect on the management of other emergency messages possibly received. [¶1197]

- 3.10.3.4 Intentionally deleted. [¶1198]

# 3.11 Static Speed Restrictions and Gradients [¶1199]

# 3.11.1 Introduction [¶1200]

- 3.11.1.1 The permitted speed at which the train is allowed to travel shall be limited to different kinds of Static Speed Restrictions. [¶1201]

- 3.11.1.2 A  Static  Speed  Restriction  shall  be  handled  in  the  same  way  independent  of  ETCS level. [¶1202]

# 3.11.2 Definition of Static Speed Restriction [¶1203]

- 3.11.2.1 Static Speed Restrictions are imposed by the trackside infrastructure, the train characteristics, the signalling and the mode of the on-board equipment. [¶1204]

- 3.11.2.2 There are eleven categories of Static Speed Restrictions: [¶1205]

- Static Speed Profile (SSP) [¶1206]

- Axle load Speed Profile (ASP) [¶1207]

-  Temporary Speed Restrictions (TSR) [¶1208]

- Maximum Train Speed [¶1209]

- Signalling related speed restriction (only level 1) [¶1210]

-  Mode related Speed Restriction. [¶1211]

- STM Max speed (for details refer to Subset-035) [¶1212]

- STM System speed (for details refer to Subset-035) [¶1213]

- Level Crossing speed restriction (LX SR) [¶1214]

-  Override function related Speed Restriction [¶1215]

-  Speed  restriction  to  ensure  a  given  permitted  braking  distance  (PBD  SR)  (see 3.11.11) [¶1216]

- 3.11.2.3 The Static Speed Restriction categories  are independent of each other. This means that  one  speed  restriction  category  cannot  affect,  nor  be  affected  by,  any  other category of Static Speed Restrictions. [¶1217]


---
<!-- pagina 104 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1218]

![](images/image_0041.png)

Figure 26: Example of Static Speed Restriction categories on a piece of track . [¶1219]

- 3.11.2.4 Depending on the type of Static Speed Restriction train length may have to be used to ensure that the full length of the train has passed a Static Speed Restriction discontinuity before a speed increase shall be taken into account. [¶1220]

- 3.11.2.5 Intentionally deleted. [¶1221]

- 3.11.2.6 Intentionally deleted. [¶1222]

# 3.11.3 Static Speed Profile (SSP) [¶1223]

- 3.11.3.1.1  The  Static  Speed  Profile  (SSP)  is  a  description  of  the  fixed  speed  restrictions  of  a given piece of track. The speed restrictions can be related to e.g. maximum line speed, curves, points, tunnel profiles, bridges. [¶1224]

- 3.11.3.1.2  The Static Speed Profile is based on factors, which are both track and train dependent. The  relationship  between  track  and  train  characteristics  determines  the  individual Static Speed Profile for each train. [¶1225]

- 3.11.3.1.3  It shall be possible for every element (distance between two discontinuities) of a static speed  profile  to  define,  if  a  transition  to  a  higher  speed  limit  than  the  speed  limit specified for this element is permitted before the complete train has left the element. [¶1226]

# 3.11.3.2 Static Speed Profile Categories [¶1227]

- 3.11.3.2.1  It shall be possible to transmit several Static Speed Profile Categories; one Basic SSP category and specific SSP categories related to the international train categories. [¶1228]

- 3.11.3.2.1.1 The specific SSP categories are decomposed into two types: [¶1229]


---
<!-- pagina 105 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1230]

- The 'Cant Deficiency' SSP categories: the cant deficiency value assigned to one category  shall  define  the  maximum  speed,  determined  by  suspension  design,  at which a particular train can traverse a curve and thus can be used to set a specific speed limit in a curve with regards to this category. [¶1231]

- The  'other  specific'  SSP  categories:  it  groups  all  other  specific  SSP  categories corresponding to the other international train categories [¶1232]

- 3.11.3.2.1.2 Whenever  the  type  of  specific  SSP  category  is  not  explicitly  specified  in  the following  requirements,  it  shall  be  interpreted  as  being  applicable  for  both  types  of specific SSP categories. [¶1233]

- 3.11.3.2.2  For each part of the Static Speed Profile, the ERTMS/ETCS trackside shall: [¶1234]

- always  give  the  Basic  SSP,  which  shall  be  considered  as  the  default  'Cant Deficiency' SSP [¶1235]

- optionally give one or more specific SSPs [¶1236]

-  specify,  for  each  'other  specific'  SSP,  whether  it  replaces  or  not  the  'Cant Deficiency' SSP as selected by the ERTMS/ETCS on-board equipment according to 3.11.3.2.3 [¶1237]

- 3.11.3.2.3  For each part of the Static Speed Profile, the ERTMS/ETCS on-board equipment shall select  the  SSP  best  suiting  its  'Cant  Deficiency'  train  category,  according  to  the following order of preference: [¶1238]

- if available, the 'Cant Deficiency' SSP matching its 'Cant Deficiency' train category, OR [¶1239]

- if available, the 'Cant Deficiency' SSP with the highest Cant Deficiency value below the value of its 'Cant Deficiency' train category, OR [¶1240]

-  the Basic SSP [¶1241]

- 3.11.3.2.3.1 Intentionally deleted. [¶1242]

- 3.11.3.2.4  Intentionally deleted. [¶1243]

- 3.11.3.2.5  'Other Specific' SSP categories not relevant to the current train shall be ignored. [¶1244]

- 3.11.3.2.6  For each part of the Static Speed Profile, the ERTMS/ETCS on-board equipment in a train belonging to at least one or more 'other international' train categories shall use the most restrictive speed amongst: [¶1245]

- the  '  Cant  Deficiency'  SSP  as  selected  in  3.11.3.2.3,  only  if  none  of  the  'other specific' SSP  categories  matching  the  train  categories  replaces  the  '  Cant Deficiency' SSP, AND [¶1246]

- all  the  'other  specific'  SSP  categories  matching  the  'other  international'  train categories. [¶1247]

# 3.11.3.3 Train categories [¶1248]


---
<!-- pagina 106 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1249]

- 3.11.3.3.1  A maximum of 31 train categories is defined to match the SSP categories. 16 'Cant Deficiency' train categories and 15 'other international' train categories. [¶1250]

- 3.11.3.3.2  A train shall always belong to one and only one 'Cant Deficiency' train category and may optionally belong to one or more 'other international' train categories. [¶1251]

- 3.11.3.3.3  The train category(ies) to which a train belongs is a part of its Train Data. [¶1252]

# 3.11.4 Axle load Speed Profile [¶1253]

- 3.11.4.1 It shall be possible to define an Axle load Speed Profile as a non-continuous profile. [¶1254]

- 3.11.4.2 For each section with a speed restriction due to axle load, the different speed value(s) and  for  which  minimum  axle  load  category  this  speed  value(s)  applies  shall  be specified. [¶1255]

- 3.11.4.2.1  Note:  Different  speed  restrictions  depending  on  the  axle  load  category  can  be applicable to the same distance. [¶1256]

- 3.11.4.3 The  ERTMS/ETCS  on-board  equipment  shall  consider  the  most  restrictive  speed restriction that is associated with any axle load category lower than, or equal to that of the train. [¶1257]

- 3.11.4.4 For trains with an axle load category lower than the minimum axle load category given in  the  profile,  the  ERTMS/ETCS  on-board  equipment  shall  not  consider  any  speed restriction due to axle load. [¶1258]

- 3.11.4.5 The initial state for Axle load Speed Profile shall be 'no restriction due to axle load'. [¶1259]

- 3.11.4.6 Whether a speed increase after the axle load speed restriction shall be delayed with train length, shall be determined by the axle load speed profile information sent to the on-board equipment. [¶1260]

# 3.11.5 Temporary Speed Restrictions [¶1261]

- 3.11.5.1 The temporary speed restriction is defined in order to enable a separate category of track infrastructure speed restriction, which can be used for working areas etc. [¶1262]

- 3.11.5.2 All Temporary Speed Restrictions are independent of each other. This means that an individual  Temporary  Speed  Restriction  cannot  affect,  nor  be  affected  by,  any  other individual Temporary Speed Restriction. [¶1263]

- 3.11.5.3 Whether a speed increase after the temporary speed restriction shall be delayed with train length, shall be determined by the temporary speed restriction information sent to the on-board equipment. [¶1264]

- 3.11.5.4 When two or more temporary speed restrictions overlap, the most restrictive speed of the overlapping temporary speed restrictions shall be used in the area of overlap. [¶1265]


---
<!-- pagina 107 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1266]

- 3.11.5.5 Each Temporary Speed Restriction shall have an identity to make it possible to revoke the  Temporary  Speed  Restriction  using  its  identity.  The  speed  restriction  shall  be revoked immediately when revocation is received from trackside, without delay for the train length. [¶1267]

- 3.11.5.6 It  shall  be  possible  to  identify  whether  a  Temporary  Speed  Restriction  is  possible  to revoke or not. [¶1268]

- 3.11.5.7 A new Temporary Speed Restriction shall not replace a previously received Temporary Speed Restriction with another identity. [¶1269]

- 3.11.5.8 Temporary Speed Restrictions shall only be revoked on request from the trackside. [¶1270]

- 3.11.5.9 If the on-board equipment receives a new Temporary Speed Restriction (TSR) with the same identity as an already received TSR, the new Temporary Speed Restriction shall replace the previous one, except when the Temporary Speed Restriction is identified as non revocable in which case this shall be considered as an additional TSR. [¶1271]

- 3.11.5.10 In case the train has changed its orientation any Temporary Speed Restriction shall be deleted (operational requirement: will be executed due to the mode change). [¶1272]

- 3.11.5.11 Intentionally deleted. [¶1273]

- 3.11.5.12 It shall be possible for the RBC to order an ERTMS/ETCS on-board equipment in Level 2 or 3 to reject revocable TSRs from balises. [¶1274]

- 3.11.5.13 When ERTMS/ETCS on-board equipment has accepted an order to reject revocable TSRs from balises, this inhibition  shall  be  stored  and shall be effective immediately, but only for revocable TSRs received from balises thereafter. [¶1275]

- 3.11.5.14 The inhibition of revocable TSRs from balises shall be deleted if any of the following occurs: [¶1276]

-  the communication session established with the RBC that ordered the inhibition is terminated, OR [¶1277]

-  in case of RBC/RBC handover, the train front end crosses the RBC/RBC border. [¶1278]

- 3.11.5.15 Note:  this  inhibition  may  be  useful  in  Level  1  /  Level  2  mixed  signalling  applications when the RBC has more precise information about restrictions than can be given from balises.  The  RBC  may  then  order  inhibition  of  revocable  TSRs  from  balises  and instead send more precise TSRs to the train. [¶1279]

# 3.11.6 Signalling related speed restrictions [¶1280]

- 3.11.6.1 In level 1, it shall be possible to send to the on-board equipment a speed restriction with a value depending on the current state of signalling. [¶1281]

- 3.11.6.2 This speed value shall be taken into account by the on-board equipment as soon as it is  received on-board, with the exception of a signalling related speed restriction from [¶1282]


---
<!-- pagina 108 -->

an  infill  device.  In  case  of  infill  information  the  speed  restriction  shall  be  taken  into account from the location reference of the balise group at the next main signal. [¶1283]

- 3.11.6.3 The speed restriction shall be valid until a new signalling related speed restriction is received. [¶1284]

- 3.11.6.3.1  If  the  ERTMS/ETCS  on-board  equipment  switches  from  level  1  to  level  2/3,  the signalling related speed restriction shall remain valid until a L2/3 MA is accepted by the ERTMS/ETCS on-board equipment [¶1285]

- 3.11.6.4 In case of a signal at danger the signalling related speed restriction shall have value zero,  which  shall  be  evaluated  by  the  ERTMS/ETCS  on-board  equipment  not  as  a speed limit but as a train trip order. [¶1286]

- 3.11.6.5 In  case  of  infill  information  the  signalling  related  speed  restriction  at  zero  shall  be ignored. [¶1287]

- 3.11.6.5.1  Note: The infill information will also include an EOA at the next main signal that will be supervised according to the normal rules. [¶1288]

# 3.11.7 Mode related speed restrictions [¶1289]

- 3.11.7.1 The  value of the mode  related speed  restriction shall be determined  by  the corresponding national value or the corresponding default values if the national values are not applicable. [¶1290]

- 3.11.7.1.1   Exception  1:  For  the  modes  On-sight,  Limited  Supervision  and  Shunting  the  speed limit  can  also  be  given  from  the  trackside.  The  speed  limit  given  from  the  trackside shall prevail over the National value and the default value. [¶1291]

- 3.11.7.1.2  Exception  2:  For  the  mode  Reversing  there  is  no  National/Default  value.  The  speed limit is always given from trackside. [¶1292]

- 3.11.7.1.3  Exception 3: For the mode Staff Responsible the speed limit can also be entered by the  driver.  The  speed  limit  given  by  the  driver  shall  prevail  over  the  National/Default value. [¶1293]

# 3.11.8 Train related speed restriction [¶1294]

- 3.11.8.1 It shall  be  possible  to  define  the  maximum  train  speed  related  to  the  actual performance and configuration of the train. [¶1295]

# 3.11.9 LX speed restriction [¶1296]

- 3.11.9.1 It shall be possible to define a LX speed restriction when the train has to pass a non protected Level Crossing. [¶1297]


---
<!-- pagina 109 -->

# 3.11.10 Override function related Speed Restriction [¶1298]

- 3.11.10.1 While the 'override' function is active, the override speed limit (national /default value) shall be taken into account. [¶1299]

# 3.11.11 Speed restriction to ensure permitted braking distance [¶1300]

- 3.11.11.1 It  shall be possible for trackside to request the ERTMS/ETCS on-board equipment to calculate a speed restriction based on a permitted braking distance given by trackside. [¶1301]

- 3.11.11.2 The order shall be given by means of a non-continuous profile defining: [¶1302]

-  The start and end location for the speed restriction [¶1303]

-  The permitted braking distance (PBD) used to calculate the speed restriction value [¶1304]

-  Whether the permitted braking distance is to be achieved with the Service Brake or Emergency Brake [¶1305]

-  A single gradient value applicable for the calculation [¶1306]

- 3.11.11.3 The speed restriction shall be calculated when the ERTMS/ETCS on-board equipment receives  the  permitted  braking  distance  information  from  trackside,  and  shall  be  recalculated only if any of the inputs taken into account for the calculation of the speed restriction changes. [¶1307]

- 3.11.11.4 The calculation of the speed restriction by the ERTMS/ETCS on-board equipment shall take into account that: [¶1308]

-  The single gradient value received from trackside shall be compensated in value according to the rotating mass as defined in 3.13.4.3. [¶1309]

-  The safe deceleration shall be computed as in 3.13.6.2.1 but without considering the adhesion profiles, the track conditions related to brake inhibition and the track conditions related to powerless section given by trackside. [¶1310]

-  The  expected  deceleration  shall  be  computed  as  in  3.13.6.3.1  but  without considering the track conditions related to brake inhibition and the track conditions related to powerless section given by trackside. [¶1311]

-  The  ERTMS/ETCS  on-board  equipment  shall  calculate  an  Emergency  Brake Deceleration  (EBD)  curve  based  on  the  safe  deceleration  and  that  reaches  zero speed at a distance equal to the permitted braking distance. [¶1312]

-  If  the  permitted  braking  distance  is  to  be  achieved  with  the  service  brake,  the ERTMS/ETCS on-board equipment shall also calculate a Service Brake Deceleration  (SBD)  curve  based  on  the  expected  deceleration  and  that  reaches zero speed at a distance equal to the permitted braking distance. [¶1313]

-  The estimated acceleration shall be set to 'zero'. [¶1314]

-  If not inhibited by National Value, the compensation of the inaccuracy of the speed measurement shall be set to a value calculated from the PBD speed, as defined in SUBSET-041  §  5.3.1.2:  V_delta0PBD  =  f41(V_PBD  +  dV_EBI(V_PBD))  if  the [¶1315]


---
<!-- pagina 110 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1316]

permitted braking distance is to be achieved with the emergency brake; V_delta0PBD = f41(V_PBD + dV_SBI(V_PBD)) if the permitted braking distance is to be achieved with the service brake. [¶1317]

-  The  train  will  travel  a  distance  from  the  last  encountered  balise  of  a  group  that provides  restrictive  information  until  initiating  the  brake  command.  This  travelled distance  shall  be  set  to  a  value  calculated  from  the  PBD  speed  considering  a processing delay (T41) equal to SUBSET-041 § 5.2.1.1. [¶1318]

-  Regardless  of  how  the  service  brake  feedback  is  actually configured  (see 3.13.2.2.7.2), T_bs1 and T_bs2 (see 3.13.9.3.3) shall be defined as if the service brake feedback was not implemented. [¶1319]

-  Regardless  of  how  the  traction  cut-off  interface  is  actually  configured  (see 3.13.2.2.8), T_traction (see 3.13.9.3.2) shall be defined as if the traction cut-off was not implemented. [¶1320]

- 3.11.11.4.1  Note: Knowing how the PBD speed restriction is computed by the ERTMS/ETCS onboard  equipment,  it  is  the  responsibility  of  the  trackside  to  set  the  appropriate permitted braking distance with regard to the risk of not initiating the brake command in due time when encountering a further balise group providing restrictive information. In  other  words,  if  deemed  necessary,  the  trackside  can include provisions based on the  characteristics  of  the  balise  group  providing  restrictive  information  e.g.  distances between  balises  in that group  with regards  to validity direction of transmitted information and balise group orientation, accuracy of balise location. [¶1321]

- 3.11.11.4.2  Note: If the permitted braking distance is to be achieved with the service brake, it is the responsibility  of  the  trackside  to  also  consider  an  estimation  of  the  on-board  overreading and under-reading amounts at the time the brake command is initiated in order to  lower  the  likelihood  of  the  max  safe  front  end  of  the  train  reaching  the  EBI supervision limit. [¶1322]

- 3.11.11.5 Note: Throughout the following formulas, all the distances marked with 'd' (lower case) are counted from a single arbitrary reference location. [¶1323]

- 3.11.11.6 If  the  permitted  braking  distance  is  to  be  achieved  with  the  emergency  brake,  the ERTMS/ETCS  on-board  equipment  shall  seek  the  PBD  speed  restriction  value (V_PBD) which satisfies the two following inequalities. The resulting value shall then be rounded down to the next lower multiple of 5km/h: [¶1324]

$$
A B S \left \{ & ( V _ { P B D } + d V _ { e b i } ) - ( V _ { E B D } \left ( d _ { o f f s e t } + D _ { b e c } \right ) - V _ { d e l t a 0 P B D } \right ) \right \} \leq 1 k m / h \\ d _ { o f f s e t } + & D _ { b e c } \leq d _ { P B D }
$$ [¶1325]

With ebi dV as defined in 3.13.9.2.3 by substituting MRSP V with PBD V [¶1326]

With   ebi PBD delta PBD dV V f V   41 0 or 0 0  delta PBD V (if  compensation  of  speed inaccuracy is inhibited by National Value) [¶1327]


---
<!-- pagina 111 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1328]

$$
\text {with } D _ { b e c } = \left ( V _ { P B D } + d V _ { e b i } + V _ { d e l t a 0 P B D } \right ) \cdot \left ( T _ { t r a c t i o n } + T _ { b e r e m } \right )
$$ [¶1329]

$$
\text {With } T _ { r a c t i o n } \text { and } T _ { b e r e m } \text { as defined in } 3 . 1 3 . 9 . 3 . 2
$$ [¶1330]

With PBD d being the permitted braking distance given by trackside [¶1331]

With   d VEBD being the EBD curve that reaches zero speed at PBD d [¶1332]

$$
\text {with } d _ { o f f o s e t } = L _ { a n t e n n a - f r o n t } + T _ { 4 1 } . \text {($V_{PBD}+dV_{e b i}+V_{d e l t a 0 PBD} $)} \, \text { )}
$$ [¶1333]

If no speed value fulfils the above inequalities, then: [¶1334]

$$
V _ { P B D } = 0
$$ [¶1335]

- 3.11.11.7 If  the  permitted  braking  distance  is  to  be  achieved  with  the  service  brake,  the  PBD speed restriction (V_PBD) shall be equal to the most restrictive value amongst the one computed from  the  EBD  (see  3.11.11.8)  and  the  one  computed  from  the  SBD  (see 3.11.11.9). The resulting value shall then be rounded down to the next lower multiple of 5km/h. [¶1336]

- 3.11.11.8 If  the  permitted  braking  distance  is  to  be  achieved  with  the  service  brake,  the ERTMS/ETCS  on-board  equipment  shall  seek  the  PBDEBD  speed  restriction  value which satisfies the two following inequalities: [¶1337]

$$
\text { which satisfies the two following inequalities:} \\ \text {ABS} \begin{cases} \left ( V _ { P B D } + d V _ { s b i } \right ) - \\ \left ( V _ { E B D } \left ( d _ { o f f e s t } + D _ { b e c } + \left ( V _ { P B D } + d V _ { s b i } \right ) \cdot T _ { b s 2 } \right ) - V _ { d e l t a 0 P B D } \right ) \right ) \leq 1 k m / h \\ \\ d _ { o f f e s t } + D _ { b e c } + \left ( V _ { P B D } + d V _ { s b i } \right ) \cdot T _ { b s 2 } \leq d _ { P B D } \end{cases}
$$ [¶1338]

With sbi dV as defined in 3.13.9.2.5 by substituting MRSP V with PBD V [¶1339]

With   sbi PBD delta PBD dV V f V   41 0 or 0 0  delta PBD V (if  compensation  of  speed inaccuracy is inhibited by National Value) [¶1340]

$$
\text {with } D _ { b e c } = \left ( V _ { P B D } + d V _ { s b i } + V _ { d e l t a 0 P B D } \right ) \cdot \left ( T _ { t r a c t i o n } + T _ { b e r e m } \right )
$$ [¶1341]

With traction T and berem T as defined in 3.13.9.3.2 [¶1342]

With 2 bs T as defined in 3.13.9.3.3 [¶1343]

With PBD d being the permitted braking distance given by trackside [¶1344]

With   d VEBD being the EBD curve that reaches zero speed at PBD d [¶1345]

$$
\text {with } d _ { o f f o s e t } = L _ { a n t e n n a \text {-front} } + T _ { 4 1 } . \text {($V_{PBD}$} + $dV_{s b i}$} + V _ { d e l t a 0 P B D } \text { )}
$$ [¶1346]


---
<!-- pagina 112 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1347]

If no speed value fulfils the above inequalities, then: [¶1348]

$$
V _ { P B D } = 0
$$ [¶1349]

- 3.11.11.9 If  the  permitted  braking  distance  is  to  be  achieved  with  the  service  brake,  the ERTMS/ETCS  on-board  equipment  shall  seek  the  PBDSBD  speed  restriction  value which satisfies the two following inequalities: [¶1350]

$$
\ A B S \left \{ \left ( V _ { _ { P B D } } + d V _ { _ { s b i } } \right ) - \left ( V _ { _ { S B D } } \left ( d _ { _ { o f f s e t } } + \left ( V _ { _ { P B D } } + d V _ { _ { s b i } } \right ) \cdot T _ { _ { b s 1 } } \right ) \right ) \right \} \leq 1 k m / h
$$ [¶1351]

$$
d _ { o f f s e t } + \left ( V _ { P B D } + d V _ { s b i } \right ) \cdot T _ { b s 1 } \leq d _ { P B D }
$$ [¶1352]

$$
P B D
$$ [¶1353]

With sbi dV as defined in 3.13.9.2.5 by substituting MRSP V with PBD V [¶1354]

With 1 bs T as defined in 3.13.9.3.3 [¶1355]

With PBD d being the permitted braking distance given by trackside [¶1356]

With   d VSBD being the SBD curve that reaches zero speed at PBD d [¶1357]

$$
\text {with } d _ { o f f s e t } = L _ { a n t e n n a - f r o n t } + T _ { 4 1 } . \left ( V _ { P B D } + d V _ { s b i } \right )
$$ [¶1358]

If no speed value fulfils the above inequalities, then: [¶1359]

$$
V _ { P B D } = 0
$$ [¶1360]

- 3.11.11.10 Note:  The  method  chosen  (e.g.  iterative  algorithm)  to  compute  the  PBD  speed restriction(s) is an implementation issue. [¶1361]

- 3.11.11.11 The initial state for Speed Restrictions to Ensure Permitted Braking Distance shall be 'no speed restriction'. [¶1362]

# 3.11.12 Gradients [¶1363]

- 3.11.12.1 The gradient information for a given piece of track shall be transmitted to the on-board equipment in form of a gradient profile. [¶1364]

- 3.11.12.2 The gradient profile shall  be continuous, i.e., give a gradient value for each location within the piece of track covered by the profile. [¶1365]

- 3.11.12.3 A gradient value shall be identified as a positive value for an uphill slope, and with a negative value for a downhill slope. [¶1366]

- 3.11.12.4 The gradient profile shall contain the gradient information as a sequence of gradient values, constant between two defined locations each, see Figure 27. [¶1367]


---
<!-- pagina 113 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1368]

![](images/image_0042.png)

Figure 27: Gradient profile [¶1369]

- 3.11.12.4.1  Note: The figure above symbolises the engineering process to provide the values of gradients.  Following  the  track  height,  the  track  must  be  split  in  segments  giving  for each segment a gradient value. [¶1370]

- 3.11.12.5 It  shall  be  possible  via  balise  groups  to  send  to  the  on-board  equipment  a  default gradient  for  TSR,  to  be  used  for  the  parts  of  the  track  not  covered  by  the  gradient profile. [¶1371]

- 3.11.12.6 The  Default  Gradient  for  TSR  stored  on-board  shall  be  valid  until  a  new  Default Gradient for TSR is received. [¶1372]

# 3.12 Other Profiles [¶1373]

# 3.12.1 Track Conditions [¶1374]

- 3.12.1.1 The Track Condition function is used to inform the driver and/or the train of a condition in front of the train. [¶1375]

- 3.12.1.2 A Track Condition shall be given as profile data (e.g. non-stopping area), i.e. start and end  of  the  data  is  given,  or  location  data  (e.g.  change  of  traction  system)  i.e.  start location given, depending on the type of track condition. [¶1376]

- 3.12.1.2.1  The  starting  point  of  a  profile  type  track  condition  shall  be  evaluated  taking  into account the max safe front end of the train, the end of the profile taking into account the  min  safe  rear  end  of  the  train.  Location  type  data  shall  be  evaluated  taking  into account the max safe front of the train. [¶1377]

- 3.12.1.2.1.1 Note:  The  timing  of  output  data  to  control  train  equipment  (e.g.  pantograph)  is application specific. [¶1378]

- 3.12.1.2.1.2 Exception  1:  The  starting  point  of  a  Big  Metal  Mass  type  track  condition  shall  be evaluated  taking  into  account  the  max  safe  antenna  position,  the  end  of  the  profile taking into account the min safe antenna position. [¶1379]


---
<!-- pagina 114 -->

- 3.12.1.2.1.3 Exception 2: The end of the Powerless section and the end of the Station Platform shall be evaluated taking into account the min safe front end of the train. [¶1380]

- 3.12.1.2.1.4 Exception 3: The start and end of a tunnel stopping area and of a sound horn track condition shall be evaluated taking into account the estimated front end of the train. [¶1381]

- 3.12.1.3 The types of track conditions to be covered by this function are: [¶1382]

-  Powerless  section,  lower  pantograph  (initial  state:  no  powerless  section,  i.e. pantograph not to be lowered) [¶1383]

-  Powerless section, switch off main power switch (initial state: no powerless section, i.e. main power switch not to be switched off) [¶1384]

-  Air tightness (initial state: no request for air tightness) [¶1385]

-  Sound horn (initial state: no request for sound horn) [¶1386]

-  Non stopping area (initial state: stopping permitted) [¶1387]

-  Tunnel stopping area (initial state: no tunnel stopping area) [¶1388]

-  Change of traction system, switch traction system on-board, used for train capable of handling several traction systems (initial state: no initial state - keep the current setting) [¶1389]

-  Change of allowed current consumption, limit current consumed by the train, used to  adapt  the  maximum  current  consumption  of  the  train  to  the  maximum  current allowed by the trackside (initial state: no initial state - keep the current setting) [¶1390]

-  Big  metal  masses,  ignore  onboard  integrity  check  alarms  of  balise  transmission. (initial state: alarms not ignored) [¶1391]

-  Radio hole, stop supervision of the loss of safe radio connection (initial state: loss of safe radio connection supervised) [¶1392]

-  Switch off regenerative brake (initial state: regenerative brake on) [¶1393]

-  Switch off eddy current brake for service brake (initial state: eddy current brake on for service brake) [¶1394]

-  Switch off eddy current brake for emergency brake (initial state: eddy current brake on for emergency brake) [¶1395]

-  Switch off magnetic shoe brake (initial state: magnetic shoe brake on). [¶1396]

-  Station  platform,  enable  passenger  doors  with  or  without  steps  according  to platform  location,  side  and  height  (initial  state:  no  platform,  i.e.  passenger  doors not enabled). [¶1397]

- 3.12.1.3.1  Note: In case of regenerative brake switch off or magnetic shoe brake switch off, the deceleration  of  the  emergency  brake  might  be  affected  if  the  effect  of  these  brakes was included in the calculation of the deceleration value . [¶1398]


---
<!-- pagina 115 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1399]

- 3.12.1.3.2  Note: In case of eddy current brake switch off the deceleration of the service brake or emergency brake might be affected if the effect of these brakes was included in the calculation of the deceleration value . [¶1400]

- 3.12.1.3.3  Note: in case of powerless section the deceleration of the service brake or emergency brake might be affected if the effect of a regenerative brake not independent from the presence of voltage in the catenary was included in the calculation of the deceleration value. [¶1401]

- 3.12.1.4 Intentionally deleted. [¶1402]

- 3.12.1.5 The following actions shall be performed once a track condition has been received: [¶1403]

- Indicate on DMI (see chapter 5, procedure 'Indication of track conditions'), except 'Station  platform',  'Change  of  allowed  current  consumption'  and  'Big  metal masses'. [¶1404]

- Send information with the remaining distance to an ERTMS/ETCS external function (see chapter 5, procedure 'Generation of track conditions related information to an ERTMS/ETCS  external  function'),  with  the  exception  of  big  metal  mass  track condition, sound horn track condition, non stopping area, tunnel stopping area and supervision of  radio transmission which are handled inside the ERTMS/ETCS onboard equipment. [¶1405]

- 3.12.1.5.1  Note: Whether some information shall be filtered (not shown to the driver or not sent to an ERTMS/ETCS external function) is outside the scope of ERTMS/ETCS. [¶1406]

- 3.12.1.5.2  Note: The ERTMS/ETCS external function must be able to handle new track condition of the same type as previously received and covering the same distance. [¶1407]

- 3.12.1.6 The  train  is  permitted  to  run  without  any  track  condition  information  given  from  the trackside. The initial state shall then be used by the on-board equipment. [¶1408]

# 3.12.2 Route Suitability [¶1409]

- 3.12.2.1 Route suitability data defines which values concerning loading gauge, traction system and axle load category a train must meet to be allowed to enter the route. [¶1410]

- 3.12.2.2 It  shall  be  possible  for  trackside  to  send  route  suitability  data  as  location  data  when needed. [¶1411]

- 3.12.2.3 On  reception  of  route  suitability  data,  the  ERTMS/ETCS  on-board  equipment  shall compare it with the corresponding Train Data stored on-board. Unsuitability exists if: [¶1412]

- The loading gauge profile of the train is not included in the list of loading gauges accepted by trackside [¶1413]

- The  list  of  traction  systems  accepted  by  the  engine  does  not  include  the  one received from trackside [¶1414]


---
<!-- pagina 116 -->

-  The axle load category of the train is higher than the permitted one received from trackside [¶1415]

- 3.12.2.4 If at least one unsuitability exists, the closest location corresponding to the unsuitability(ies)  shall  be  considered  as  both  the  EOA  and  SvL  (instead  of  the EOA/LOA and the  SvL  (if  any)  derived  from  the  MA),  with  no  Release  Speed.  The driver shall be informed about all unsuitabilities. [¶1416]

- 3.12.2.5 Intentionally deleted. [¶1417]

- 3.12.2.5.1  Intentionally deleted. [¶1418]

- 3.12.2.6 Intentionally deleted. [¶1419]

- 3.12.2.7 Intentionally deleted. [¶1420]

- 3.12.2.8 If, for any reasons, the train overpasses the location of the first route suitability where incompatibility occurs, it shall be tripped. [¶1421]

- 3.12.2.9 The Train Data concerning route suitability is part of the Train Data sent to the RBC. [¶1422]

- 3.12.2.9.1  Note: This allows for route suitability supervision to be used in systems external to the ERTMS/ETCS system. [¶1423]

- 3.12.2.10 The train is permitted to run without any route suitability data given from the track. No default values shall be used or supervised by the on-board equipment, i.e. the initial state is that no restrictions related to route suitability exists. [¶1424]

# 3.12.3 Text Transmission [¶1425]

# 3.12.3.1 General Rules [¶1426]

- 3.12.3.1.1  It  shall  be  possible  to  transmit  information  to  be  displayed  to  the  driver  from  the trackside to the on-board equipment in the form of text messages. [¶1427]

- 3.12.3.1.2  Text messages shall always be supplemented by conditions on when and where they are to be displayed, and whether any acknowledgement is requested from the driver. These parameters shall be transmitted individually for each message. [¶1428]

- 3.12.3.1.3  Text messages and the supplementary information shall always be transmitted in one message. [¶1429]

- 3.12.3.1.4  It shall be possible to send the text to be displayed in plain text or to send a number selecting a fixed message. [¶1430]

- 3.12.3.1.4.1 Note: In case of plain text messages the trackside selects the language in which the message is displayed. [¶1431]

- 3.12.3.1.5  Intentionally deleted. [¶1432]

- 3.12.3.1.6  Intentionally deleted. [¶1433]


---
<!-- pagina 117 -->

- 3.12.3.1.7  Intentionally deleted. [¶1434]

- 3.12.3.1.8  Intentionally deleted. [¶1435]

- 3.12.3.1.9  The following data shall be included in a text message: [¶1436]

-  Class of message (auxiliary or important information) [¶1437]

-  Plain text message or fixed message number [¶1438]

-  Conditions for start of indication [¶1439]

-  Conditions for end of indication [¶1440]

-  If driver acknowledgement is requested or not [¶1441]

- 3.12.3.1.10  The  appearance  of  a  message  shall  depend  on  the  class  and  on  whether  a  driver acknowledgement is requested. [¶1442]

- 3.12.3.1.11  It shall be possible for trackside to send a text message with a request to report driver acknowledgement, if any, to an RBC. [¶1443]

# 3.12.3.2 Intentionally deleted

- 3.12.3.2.1  Intentionally deleted

# 3.12.3.3 Fixed text messages [¶1444]

- 3.12.3.3.1  Fixed text messages shall be stored on-board in all languages that can be selected by the driver. [¶1445]

- 3.12.3.3.2  Intentionally deleted. [¶1446]

- 3.12.3.3.3  Intentionally deleted. [¶1447]

- 3.12.3.3.4  Intentionally deleted. [¶1448]

- 3.12.3.3.5  Intentionally deleted. [¶1449]

# 3.12.3.4 Conditions for Start/End of Indication [¶1450]

- 3.12.3.4.1  It shall be possible to specify individual events for start/end condition of indication. [¶1451]

- 3.12.3.4.2  The following events can be used to define the start condition: [¶1452]

-  Location [¶1453]

-  Mode (start display as soon as in mode) [¶1454]

-  Level (start display as soon as in level) [¶1455]

- 3.12.3.4.3  The following events can be used to define the end condition: [¶1456]

-  Location [¶1457]

-  Time [¶1458]

-  Mode (stop display when leaving mode) [¶1459]


---
<!-- pagina 118 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1460]

-  Level (stop display when leaving level) [¶1461]

- 3.12.3.4.3.1 It  shall be possible to define whether one or all of the events used from the list in 3.12.3.4.2/3.12.3.4.3 have  to  be  fulfilled to define  the start/end condition.  This definition shall apply to both start and end conditions checked by the on-board. [¶1462]

- 3.12.3.4.3.2 In  case  a  confirmation  of  the  text  message  is  requested,  it  shall  be  possible  to define whether the driver acknowledgement is considered: [¶1463]

- As  always  ending  the  text  display,  regardless  of  the  end  condition  defined  in 3.12.3.4.3.1 [¶1464]

- As  a  necessary  condition  to  end  the  text  display,  in  addition  to  the  end  condition defined in 3.12.3.4.3.1. [¶1465]

- 3.12.3.4.4  The  end  condition  shall  be  evaluated  as  soon  as  the  start  condition  is  fulfilled.  No display shall take place if the end condition is immediately fulfilled. [¶1466]

- 3.12.3.4.5  Once the text message is displayed and the end condition is fulfilled, the start condition shall not be re-evaluated. [¶1467]

- 3.12.3.4.6  When the end event "location" is used, the length on which the text is displayed shall refer to the location used for the start condition, independently from other start events. [¶1468]

- 3.12.3.4.7  In case a confirmation of the text message is requested, it shall be possible to define whether the service brake or emergency brake application shall be commanded if the driver does not acknowledge before the end condition is fulfilled. [¶1469]

- 3.12.3.4.7.1 If  the  driver  does  not  acknowledge  before  the  end  condition  is  fulfilled,  the  text message shall remain displayed until acknowledged by driver. [¶1470]

- 3.12.3.4.7.2 If  the  driver  acknowledges  before  the  end  condition  is  fulfilled,  the  on-board equipment shall consider the driver acknowledgement as requested by trackside (see 3.12.3.4.3.2). [¶1471]

- 3.12.3.4.8  Intentionally deleted. [¶1472]

# 3.12.3.5 Report of driver acknowledgement to RBC [¶1473]

- 3.12.3.5.1  If trackside requests a report of driver acknowledgement, then it shall include: [¶1474]

-  a text message identifier [¶1475]

-  the identity of the RBC to which the driver acknowledgement report is to be sent. [¶1476]

- 3.12.3.5.2  When  the  driver  has  acknowledged  a  text  message  with  a  request  to  report  driver acknowledgement,  the  driver  acknowledgement  report,  including  the  text  message identifier, shall be sent to the RBC referenced in the request. [¶1477]

- 3.12.3.5.3  A  new  text  message  with  request  for  report  of  driver  acknowledgement  shall  be rejected  by  the  ERTMS/ETCS  on-board  equipment  if  it  has  the  same  text  message [¶1478]


---
<!-- pagina 119 -->

identifier  as  a  previously  received  text  message,  which  the  driver  has  not  yet acknowledged. [¶1479]

# 3.12.4 Mode profile [¶1480]

- 3.12.4.1 It shall be possible for trackside to send a Mode Profile. The Mode Profile can request On Sight mode, Limited Supervision mode and Shunting mode. [¶1481]

- 3.12.4.2 For  OS  and  LS  mode  the  mode  profile  defines  the  entry  and  the  length  of  the  On Sight/Limited Supervision area. For SH mode the mode profile only defines the entry location to SH mode, any length given shall be ignored by the on-board. [¶1482]

- 3.12.4.3 On reception of a new MA (with or without Mode Profile) the on-board equipment shall delete the currently supervised Mode Profile. [¶1483]

- 3.12.4.3.1  Exception: When receiving a new MA by infill, any currently supervised Mode Profile shall be deleted only beyond the reference location of the infill information. [¶1484]

- 3.12.4.4 In  case  the  mode  profile  information  for  shunting  is  overwritten  by  a  new  shunting profile, before the on-board equipment switches to SH mode, a previous list of balise groups for SH area shall be deleted or replaced by a new list of balise groups for SH area. [¶1485]

- 3.12.4.5 The beginning of the Mode Profile relates to the max safe front end of the train. [¶1486]

- 3.12.4.6 The end of the mode profile relates to the min safe front end of the train. [¶1487]

# 3.12.5 Level Crossings [¶1488]

- 3.12.5.1 It  shall  be  possible  for  trackside  to  inform  the  ERTMS/ETCS  on-board  equipment about the conditions under which a Level Crossing (LX) must be passed. [¶1489]

- 3.12.5.2 Each Level Crossing shall have an identity, so that all LX information is independent of each other. This means that an individual LX information cannot affect, nor be affected by, any other individual LX information. [¶1490]

- 3.12.5.3 If the ERTMS/ETCS on-board equipment receives a new LX information with the same identity  as  an  already  received  LX  information,  the  new  LX  information shall  replace the previous one. [¶1491]

- 3.12.5.4 Level Crossing information shall be given as profile data, corresponding to the LX start location and the length of the LX area. [¶1492]

- 3.12.5.5 Level Crossing information shall indicate whether the LX is protected or not. [¶1493]

- 3.12.5.6 In case the LX is not protected, ERTMS/ETCS on-board equipment shall be informed: [¶1494]

- at which speed the LX is allowed to be passed [¶1495]

- whether the stopping of the train in rear of the LX start location is required or not [¶1496]


---
<!-- pagina 120 -->

- 3.12.5.7 In case stopping in rear of the non protected LX is required, a stopping area in rear of the LX start location shall be defined. [¶1497]

# 3.13 Speed and distance monitoring [¶1498]

# 3.13.1 Introduction [¶1499]

- 3.13.1.1 The speed and distance monitoring is the supervision of the speed of the train versus its  position,  in  order  to  assure  that  the  train  remains  within  the  given  speed  and distance limits. [¶1500]

- 3.13.1.1.1  Note: The speed and distance monitoring of the on-board can only assure this when the following necessary conditions are fulfilled: [¶1501]

-  Brake system of the train functions as specified [¶1502]

-  wheel/rail adhesion is sufficient for the required safe deceleration [¶1503]

-  Brake characteristics (and other Train related inputs) are correctly entered into the on-board [¶1504]

- 3.13.1.2 Note: The ERTMS/ETCS on-board equipment triggers brake commands and revokes them,  it  may  also  receive  status  information  if  the  brakes  are  applied  or  released. However, it cannot be made responsible if brake control circuits outside the equipment fail.  Also the way the brakes are released by the driver after a revocation of a brake command is an implementation issue. [¶1505]

- 3.13.1.3 Figure  28  gives  an  overview  of  the  main  elements  contributing  to  the  speed  and distance monitoring. These elements (inputs, functions and outputs) are detailed in the following chapters. [¶1506]


---
<!-- pagina 121 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1507]

![](images/image_0043.png)

Figure 28: Speed and distance monitoring overview [¶1508]

- 3.13.1.4 Throughout  the  following  sections,  all  the  distances  marked  with  'd'  (lower  case), which are referred in parameters, formulas and figures, are counted from the current reference location of the on-board equipment (e.g. the LRBG). [¶1509]

# 3.13.2 Inputs for speed and distance monitoring [¶1510]

# 3.13.2.1 Introduction [¶1511]

- 3.13.2.1.1  The traction / braking models, the brake position / brake percentage are used for the definition of the kinematic behaviour of the train after a service brake command or an emergency brake command has been initiated. [¶1512]


---
<!-- pagina 122 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1513]

- 3.13.2.1.2  However, railway brakes have a statistical behaviour and braking distances vary within the typical distribution for a given condition. Correction factors are therefore incorporated for the speed and distance monitoring. [¶1514]

- 3.13.2.1.3  The  correction  factors  will  allow  obtaining,  from  the  nominal  emergency  braking performance  of  the  train,  the  minimum  emergency  braking  performances  that  are required for reference conditions set by trackside. [¶1515]

# 3.13.2.2 Train related inputs [¶1516]

# 3.13.2.2.1  Introduction [¶1517]

- 3.13.2.2.1.1 The train related inputs to be considered for the speed and distance monitoring are: [¶1518]

- Traction model [¶1519]

- Braking models (brake build up time and speed dependent deceleration) or brake percentage [¶1520]

-  Brake position [¶1521]

- Special brakes (interface configuration and status) [¶1522]

- Service brake (interface configuration and application) [¶1523]

-  Traction cut-off interface [¶1524]

- On-board correction factors [¶1525]

- Nominal rotating mass [¶1526]

- Train length [¶1527]

-  Fixed values related to speed and distance monitoring [¶1528]

-   Train related speed restriction (i.e. the maximum train speed) [¶1529]

- 3.13.2.2.1.2 These train related inputs are acquired as Train Data (see 3.18.3.2 items b) c) and d)), except: [¶1530]

-  the configuration of the special brakes, service brake and traction cut-off interfaces which are not affected by the Train Data acquisition, [¶1531]

-  the service brake application and the special brakes statuses which are continuously acquired on the Train Interface, [¶1532]

-  the fixed values. [¶1533]

- 3.13.2.2.1.3 The  speed  and  distance  monitoring  shall  use  braking  models  acquired  as  Train Data, unless the brake percentage is acquired as Train Data and the conversion model is applicable (see 3.13.3.2 for its validity limits). [¶1534]

# 3.13.2.2.2  Traction model [¶1535]

- 3.13.2.2.2.1 The traction model shall be given as a step function as indicated in  Figure 29. It shall describe the time delay T_traction_cut_off from the traction cut-off command by [¶1536]


---
<!-- pagina 123 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1537]

the  on-board  (t0)  to  the  moment  the  acceleration  due  to  traction  (A_traction)  is guaranteed  to  be  zero  (t1).  The  estimated  acceleration  value  of  the  train  shall  be considered during this time delay. [¶1538]

![](images/image_0044.png)

Figure 29: Traction Model [¶1539]

- 3.13.2.2.2.2 Note:  The  current  value  of  A_traction  is  not  known  directly  by  the  on-board.  It  is implicitly  known  as  a  contribution  to  the  estimated  acceleration,  together  with  the acceleration due to gradient. [¶1540]

- 3.13.2.2.3  Braking Models [¶1541]

# 3.13.2.2.3.1 Speed Dependent Deceleration [¶1542]

- 3.13.2.2.3.1.1 The deceleration due to braking shall be given as a step function of the speed. [¶1543]

- 3.13.2.2.3.1.2 It  shall  be  possible  to  define  up  to  seven  steps  for  each  speed  dependent deceleration model. [¶1544]

- 3.13.2.2.3.1.3 Note: An example with 4 steps is given in  Figure 30. A_brake(V) is calculated as follows: [¶1545]

-  A_brake = AD_0  when 0 ≤ speed ≤ V1 [¶1546]

-  A_brake = AD_1  when V1 < speed ≤ V2 [¶1547]

-  A_brake = AD_2  when V2 < speed ≤ V3 [¶1548]

-  A_brake = AD_3  when V3 < speed [¶1549]

![](images/image_0045.png)


---
<!-- pagina 124 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1550]

# Figure 30: Speed Dependent Deceleration Model [¶1551]

- 3.13.2.2.3.1.4 The last step of A_brake(V) shall by definition be considered as open ended, i.e. it has no upper speed limit. [¶1552]

- 3.13.2.2.3.1.5 The model shall be applicable only after full build up of the braking effort (see a_full in Figure 31) [¶1553]

- 3.13.2.2.3.1.6 The model shall be used for the emergency brake nominal deceleration (A_brake_emergency(V)), for the full service brake deceleration (A_brake_service(V)) and for the normal service brake deceleration (A_brake_normal_service(V)). [¶1554]

- 3.13.2.2.3.1.7 It  shall  be  possible  to  define  individual  speed  dependent  deceleration  models  of A_brake_emergency(V)  and  A_brake_service(V)  for  each  combination  of  use  of regenerative brake, eddy current brake and magnetic shoe brake. [¶1555]

- 3.13.2.2.3.1.8 Note: Individual deceleration models may be equal, thereby avoiding the influence of  a  specific  brake  on  A_brake_emergency(V)  or  A_brake_service(V).  However,  the choice to take into account or not the contribution of a specific brake for A_brake_emergency(V) or A_brake_service(V) is only rolling stock dependent, not an ETCS implementation issue. [¶1556]

- 3.13.2.2.3.1.9 It shall be possible to define up to two sets of three models of A_brake_normal_service(V): [¶1557]

- one set applicable when the brake position is in 'Freight train in G' [¶1558]

- one set applicable when the brake position is in 'Passenger train in P' or 'Freight train in P' [¶1559]

- 3.13.2.2.3.1.10 A  set  of  A_brake_normal_service(V)  shall  be  defined  as  a  function  of  the  full service brake deceleration at zero speed, A_brake_service(V=0): [¶1560]

- If A_brake_service(V = 0)  A_SB01 [¶1561]

A_brake_normal_service(V) = A_brake_normal_service_0(V) [¶1562]

- if A_SB01 < A_brake_service(V = 0)  A_SB12 [¶1563]

A_brake_normal_service(V) = A_brake_normal_service_1(V) [¶1564]

- if A_SB12 < A_brake_service (V = 0) [¶1565]

A_brake_normal_service(V) = A_brake_normal_service_2(V) [¶1566]

- 3.13.2.2.3.1.11 Note: the two pivot values A_SB01 and A_SB12 are part of the A_brake_normal_service model, i.e. they are train related input data for the speed and distance monitoring function. [¶1567]

# 3.13.2.2.3.2 Brake build up time [¶1568]


---
<!-- pagina 125 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1569]

- 3.13.2.2.3.2.1 The deceleration A_brake is not available immediately after the on-board commands the brake. There is a time lag between brake command and the start of the brake force build-up. There is also time needed to build up the full brake force. [¶1570]

- 3.13.2.2.3.2.2 The model for the brake build up time shall be given as a step function as explained in Figure 31. [¶1571]

- 3.13.2.2.3.2.3 In Figure 31, the following time intervals are defined: [¶1572]

- T_brake_react (t0…t1) is the interval between the command of the brake by the onboard and the moment the brake force starts to build up. [¶1573]

- T_brake_increase (t1...t2) is the interval in which the brake force increases from the zero to the moment when 95% of full brake power is reached. [¶1574]

-  T_brake_build_up (t0...t3) is the equivalent brake build up time. [¶1575]

- 3.13.2.2.3.2.4 The equivalent brake build up time (T_brake_build_up) is defined as T_brake_build_up = T_brake_react + 0.5*T_brake_increase. [¶1576]

- 3.13.2.2.3.2.5 This model for T_brake_build_up shall be used for the emergency brake (T_brake_emergency) and for the full service brake (T_brake_service). [¶1577]

- 3.13.2.2.3.2.6 Note: The equivalent brake build up time is a safe approximation. In the beginning of the build-up time the model assumes a smaller deceleration, in the later part this is compensated by a higher deceleration. [¶1578]

- 3.13.2.2.3.2.7 Note: T_brake_react and T_brake_increase are indicated in Figure 31 for completeness reasons; only T_brake_build_up is to be considered as an input for the speed and distance monitoring function. [¶1579]

- 3.13.2.2.3.2.8 It shall be possible to define individual  values  of  T_brake_emergency  and T_brake_service  for  each  combination  of  use  of  regenerative  brake,  eddy  current brake, magnetic shoe brake and Ep brake. [¶1580]

![](images/image_0046.png)

Figure 31: Brake Build Up Time Model [¶1581]


---
<!-- pagina 126 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1582]

- 3.13.2.2.3.2.9 Note: Individual values of T_brake_emergency and T_brake_service may be equal, thereby  avoiding  the  influence  of  a  specific  brake.  However,  the  choice  to  take  into account  or  not  the  contribution  of  a  specific  brake  for  T_brake_emergency  and T_brake_service is only rolling stock dependent, not an ETCS implementation issue. [¶1583]

- 3.13.2.2.3.2.10 Note: In general, T_brake_emergency and T_brake_service are determined by the  pneumatic  brake  therefore  avoiding  to  take  into  account  of  the  influence  of  the regenerative  brake,  eddy  current  brake  or  magnetic  shoe  brake.  However,  if  the Electro-pneumatic brake system is used, it is possible that T_brake_emergency and T_brake_service are determined by another special brake. [¶1584]

# 3.13.2.2.4  Brake Position [¶1585]

- 3.13.2.2.4.1 The brake position shall be set to one of the following three values: [¶1586]

- Passenger train in P [¶1587]

- Freight train in P [¶1588]

-  Freight train in G [¶1589]

- 3.13.2.2.4.2 Note: The brake position defines the behaviour of the brake for specific train types. [¶1590]

# 3.13.2.2.5  Brake Percentage [¶1591]

- 3.13.2.2.5.1 If  the  brake  percentage  is  captured  as  Train  Data  and  the  conversion  model  is applicable (see 3.13.3.2), they are used to derive A_brake_emergency(V), A_brake_service(V), T_brake_emergency and T_brake_service. [¶1592]

- 3.13.2.2.5.2 Note: the conversion model has been designed assuming that all the provisions laid down in the UIC leaflet 544-1 6 th  edition, with the exception of sections 9.1.2, 9.2.2 and 9.3.3, apply for the acquired brake percentage. [¶1593]


---
<!-- pagina 127 -->

# 3.13.2.2.6  Special Brakes [¶1594]

- 3.13.2.2.6.1 For  each  special  brake  (regenerative  brake,  eddy  current  brake,  magnetic  shoe brake and electro-pneumatic brake), the on-board shall be configured to define one of the following possibilities marked with an 'X' in Table 3 [¶1595]

- 3.13.2.2.6.2 When an interface exists with the regenerative brake, eddy current brake, magnetic shoe brake system and/or the Ep brake on-board system and depending whether their status affects the concerned brake parameter(s), the speed and distance monitoring shall  take  into  account  their  status  'active'  or  'not  active'  to  select  the  appropriate brake parameter(s) captured as Train Data, according to Table 4: [¶1596]

[¶1597]
|               |                     | configuration possibilities   | configuration possibilities                                        | configuration possibilities                                      | configuration possibilities                                                 |
|---------------|---------------------|-------------------------------|--------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|
|               |                     | No interface exists           | Interface exists and status affects the emergency brake model only | Interface exists and status affects the service brake model only | Interface exists and status affects both emergency and service brake models |
| Special brake | regenerative brake  | x                             | x                                                                  | x                                                                | x                                                                           |
| Special brake | eddy current brake  | x                             | x                                                                  | x                                                                | x                                                                           |
| Special brake | magnetic shoe brake | x                             | x                                                                  |                                                                  |                                                                             |
| Special brake | Ep brake            | x                             |                                                                    | x                                                                | x                                                                           |

Table 3: On-board Configuration in relation to special brakes [¶1598]

[¶1599]
|                 |                      | When interface exists and if status affects the brake parameter, selection of brake parameter according to status of:   | When interface exists and if status affects the brake parameter, selection of brake parameter according to status of:   | When interface exists and if status affects the brake parameter, selection of brake parameter according to status of:   | When interface exists and if status affects the brake parameter, selection of brake parameter according to status of:   |
|-----------------|----------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
|                 |                      | regenerative brake                                                                                                      | eddy current brake                                                                                                      | magnetic shoe brake                                                                                                     | Ep brake                                                                                                                |
| Brake parameter | A_brake_emergency(V) | x                                                                                                                       | x                                                                                                                       | x                                                                                                                       |                                                                                                                         |
| Brake parameter | T_brake_emergency    | x                                                                                                                       | x                                                                                                                       | x                                                                                                                       | x                                                                                                                       |
| Brake parameter | A_brake_service(V)   | x                                                                                                                       | x                                                                                                                       |                                                                                                                         |                                                                                                                         |
| Brake parameter | T_brake_service      | x                                                                                                                       | x                                                                                                                       |                                                                                                                         | x                                                                                                                       |

Table 4: Selection of brake parameters according to status of special brakes [¶1600]


---
<!-- pagina 128 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1601]

- 3.13.2.2.6.3 When the brake percentage is captured as Train Data and the conversion model is applicable, A_brake_emergency(V), T_brake_emergency and A_brake_service(V) shall  not  be  influenced  by  the  status  of  a  special  brake.  However,  the  conversion model offers the possibility that T_brake_service can be affected by the status of the regenerative brake, eddy current brake or Ep brake (see A.3.9). [¶1602]

- 3.13.2.2.6.4 The on-board equipment shall be configured to define whether it is allowed to take into account the contribution of a special/additional brake, which is independent from wheel/rail adhesion, for the selection of the maximum emergency brake deceleration under reduced adhesion conditions (see 3.13.6.2.1.6). [¶1603]

- 3.13.2.2.6.5 Note: the choice to set to 'allowed' the contribution of such special/additional brake in the selection of the maximum emergency braking effort, is rolling stock dependent. [¶1604]

- 3.13.2.2.6.6 If  it  is  allowed  to  take  into  account  the  contribution  of  a  special/additional  brake, which  is  independent  from  wheel/rail  adhesion,  the  speed  and  distance  monitoring function shall take into account the status 'active' or 'not active' of the special/additional  brake  to  select  the  appropriate  National  Value  under  reduced adhesion conditions (see 3.13.2.3.7.7). [¶1605]

# 3.13.2.2.7  Service brake [¶1606]

- 3.13.2.2.7.1 The on-board shall be configured to define whether the service brake command is implemented or not, i.e. whether a service brake interface is implemented to command a full service brake effort. [¶1607]

- 3.13.2.2.7.2 The on-board shall be configured to define whether the service brake feedback is implemented or not, i.e. whether it is able to acquire from the service brake interface the information that the service brake is currently applied. [¶1608]

- 3.13.2.2.7.3 If the service brake feedback is implemented and if not inhibited by National Value, the  speed  and  distance  monitoring  function  shall  take  into  account  either  the  main brake pipe pressure or the brake cylinder pressure to adjust in real time the expected brake build up time (see 3.13.9.3.3.4 and Appendix A.3.10). [¶1609]

# 3.13.2.2.8  Traction cut-off interface [¶1610]

- 3.13.2.2.8.1 The on-board shall be configured to define whether the traction cut-off command is implemented, i.e. whether the interface to the traction system is implemented or not. [¶1611]

# 3.13.2.2.9  On-board Correction Factors [¶1612]

# 3.13.2.2.9.1 Correction factors for the emergency deceleration [¶1613]

- 3.13.2.2.9.1.1 If  the  braking  models  are  captured  as  Train  Data,  rolling  stock  correction  factors shall be defined in the ETCS on-board equipment. If the brake percentage is captured as Train Data and the conversion model is used (see 3.13.3.2 for its validity limits), no rolling stock correction factor shall apply. [¶1614]


---
<!-- pagina 129 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1615]

- 3.13.2.2.9.1.2 For each defined individual speed dependent deceleration model of A_brake_emergency(V) (i.e. corresponding to each combination of use of regenerative brake,  eddy  current  brake  and  magnetic  shoe  brake),  one  set  of  rolling  stock correction factors Kdry_rst(V, EBCL) and Kwet_rst(V) shall be defined in the on-board equipment. [¶1616]

- 3.13.2.2.9.1.3 For  a  given  confidence  level  on  emergency  brake  safe  deceleration  (EBCL),  the rolling  stock correction factor Kdry_rst(V) shall be given as a step function of speed, with the same steps as the ones of A_brake_emergency(V). [¶1617]

- 3.13.2.2.9.1.4 The confidence  level  on  emergency  brake  safe  deceleration  represents  the probability of the following individual  event:  the  rolling  stock  emergency  brake subsystem of the train does ensure a deceleration at least equal to A_brake_emergency(V) * Kdry_rst(V), when the emergency brake is commanded on dry rails. [¶1618]

- 3.13.2.2.9.1.5 The rolling stock correction factor Kwet_rst(V) shall be given as a step function of speed, with the same steps as the ones of A_brake_emergency(V). It represents the loss  of  deceleration  with  regards  to  emergency  braking  on  dry  rails,  when  the emergency  brake  is  commanded  on  wet  rails,  according  to  wheel/rail  adhesion reference conditions. [¶1619]

# 3.13.2.2.9.2 Correction factor for gradient on normal service deceleration [¶1620]

- 3.13.2.2.9.2.1 The speed dependent correction factors for gradient on the normal service brake, Kn+(V) and Kn-(V), shall be given as step functions in the range from 0 to 10 m/s2. [¶1621]

- 3.13.2.2.9.2.2 It shall be possible to define up to five steps for Kn+(V) and for Kn-(V), respectively. [¶1622]

- 3.13.2.2.9.2.3 Note: An example with 4 steps is given in Figure 32. Kn is calculated as follows: [¶1623]

-  Kn = Kn_0 when 0 ≤ speed ≤ V1 [¶1624]

-  Kn = Kn_1 when V1 < speed ≤ V2 [¶1625]

-  Kn = Kn_2 when V2 < speed ≤ V3 [¶1626]

-  Kn = Kn_3 when V3 < speed [¶1627]


---
<!-- pagina 130 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1628]

![](images/image_0047.png)

Figure 32  Speed dependent correction factor for normal service brake (Kn) [¶1629]

- 3.13.2.2.9.2.4 Kn+(V) shall be applicable for positive gradients. [¶1630]

- 3.13.2.2.9.2.5 Kn-(V) shall be applicable for negative gradients. [¶1631]

- 3.13.2.2.9.2.6 The  last  step  of  the  Kn+(V)  or  Kn-(V)  shall  by  definition  be  considered  as  open ended, i.e. it has no upper speed limit. [¶1632]

# 3.13.2.2.10  Nominal Rotating mass [¶1633]

- 3.13.2.2.10.1  It shall be possible to define the nominal rotating mass to be used for compensating the gradient, instead of the two related fixed values defined in A.3.1. [¶1634]

# 3.13.2.2.11  Train length [¶1635]

- 3.13.2.2.11.1  The speed and distance monitoring shall take into account the train length acquired as part of Train Data (see section 3.18.3). [¶1636]

# 3.13.2.2.12  Fixed values [¶1637]

- 3.13.2.2.12.1  The speed and distance monitoring shall take into account the fixed values defined in A.3.1 that are related to speed and distance monitoring. [¶1638]

# 3.13.2.2.13  Maximum train speed [¶1639]

- 3.13.2.2.13.1  The  speed  and  distance  monitoring  shall  take  into  account  the  maximum  train speed defined as part of Train Data (see section 3.18.3). [¶1640]

# 3.13.2.3 Trackside related inputs [¶1641]

# 3.13.2.3.1  Introduction [¶1642]

- 3.13.2.3.1.1 The trackside related inputs to be considered for the speed and distance monitoring are: [¶1643]

- Trackside related speed restrictions [¶1644]

- Gradients [¶1645]


---
<!-- pagina 131 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1646]

-  Track conditions related to brake inhibition [¶1647]

- Track conditions related to powerless section [¶1648]

- Reduced adhesion conditions [¶1649]

-  Specific speed and distance limits (e.g. EOA/SvL) [¶1650]

- National Values [¶1651]

# 3.13.2.3.2  Trackside related speed restrictions [¶1652]

- 3.13.2.3.2.1 The  speed  and  distance  monitoring  shall  take  into  account  the  trackside  related speed restrictions composed of all speed restrictions mentioned in 3.11.2 except the maximum train speed. [¶1653]

# 3.13.2.3.3  Gradients [¶1654]

- 3.13.2.3.3.1 The speed and distance monitoring shall take into account the gradient profile and the default gradient for TSR (see section 3.11.12). [¶1655]

# 3.13.2.3.4  Track conditions [¶1656]

- 3.13.2.3.4.1 The speed and distance monitoring shall take into  account the  following types of track  condition  received  from  trackside  (see  section  3.12.1):  powerless  section, inhibition of regenerative brake, eddy current brake and magnetic shoe brake. [¶1657]

# 3.13.2.3.5  Reduced adhesion conditions [¶1658]

- 3.13.2.3.5.1 The  speed  and  distance  monitoring  shall  take  into  account  the  track  reduced adhesion received from trackside or selected by the driver (see section 3.18.4.6). [¶1659]

# 3.13.2.3.6  Specific speed / distance limits [¶1660]

- 3.13.2.3.6.1 The speed and distance monitoring shall take into account the following limits: [¶1661]

- the Limit of Authority (LOA), the End of Authority (EOA), the Supervised Location (SvL) and its associated release speed, if any. [¶1662]

- the maximum permitted distance to run in Staff Responsible [¶1663]

# 3.13.2.3.7  National Values for speed and distance monitoring [¶1664]

- 3.13.2.3.7.1 It  shall  be  possible  by  means of a National Value to inhibit the use of the service brake command in target speed monitoring. [¶1665]

- 3.13.2.3.7.2 It  shall  be  possible  to  state  by  means of a National Value whether an emergency brake command has to be revoked, both in ceiling speed and target speed monitoring, when: [¶1666]

- the Permitted Speed supervision limit is no longer exceeded, or [¶1667]

- the train is at standstill. [¶1668]


---
<!-- pagina 132 -->

- 3.13.2.3.7.3 It  shall  be  possible  by  means  of  a  National  Value  to  inhibit  the  guidance  curve (GUI). [¶1669]

- 3.13.2.3.7.4 It  shall  be  possible  by  means  of  a  National  Value  to  inhibit  the  service  brake feedback function. [¶1670]

- 3.13.2.3.7.5 It  shall  be  possible  by  means  of  National  Values  to  indicate  to  the  on-board equipment the required confidence level  on  the  emergency  brake safe deceleration, when the emergency brake is commanded on dry rails (see 3.13.2.2.9.1.4). [¶1671]

- 3.13.2.3.7.6 It  shall  be  possible  by  means  of  a  National  Value  to  indicate  to  the  on-board equipment the available wheel/rail adhesion, weighted between the wheel/rail adhesion for dry rails and the wheel/rail adhesion for wet rails according to reference conditions. [¶1672]

- 3.13.2.3.7.7 In order to adapt to the train behaviour under reduced adhesion conditions, it shall be possible by means of National Values either to limit to a maximum value the speed dependent  deceleration for the emergency  brake  when  the  reduced  adhesion conditions  are  known  to  ETCS  (see  3.13.2.3.5)  or  to  request  supplementary  DMI information assisting further the driver in ceiling speed monitoring. Three values shall be applicable for a given combination of the brake position and of the type of brakes: [¶1673]

- the first value shall be used for 'Passenger train in P' with special/additional brakes independent from wheel/rail adhesion; [¶1674]

- the second value shall be used for 'Passenger train in P' without special/additional brakes independent from wheel/rail adhesion; [¶1675]

-  the third value shall be used for 'Freight train in P' or 'Freight train in G'. [¶1676]

- 3.13.2.3.7.8 It shall be possible by means of a National Value to specify a release speed. [¶1677]

- 3.13.2.3.7.9 It shall be possible by means of a National Value to inhibit the compensation of the speed measurement inaccuracy. [¶1678]

- 3.13.2.3.7.10  It  shall  be  possible  by  means  of  National  Values  to  define  integrated  correction factors,  namely  Kv_int(V),  Kr_int(l)  and  Kt_int.  The  integrated  correction  factors  only apply to the on-board equipment when the conversion model is used. [¶1679]

- 3.13.2.3.7.11  The speed dependent correction factor, Kv_int(V), shall be given as a step function. [¶1680]

- 3.13.2.3.7.11.1 It shall be possible to define up to five steps for Kv_int(V). [¶1681]

- 3.13.2.3.7.11.2 Note:  An  example  with  4  steps  is  given  in  Figure  33.  Kv_int  is  calculated  as follows: [¶1682]

-  Kv_int = Kv_int_0 when 0 ≤ speed ≤ V1 [¶1683]

-  Kv_int = Kv_int_1 when V1 < speed ≤ V2 [¶1684]

-  Kv_int = Kv_int_2 when V2 < speed ≤ V3 [¶1685]

-  Kv_int = Kv_int_3 when V3 < speed [¶1686]


---
<!-- pagina 133 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1687]

![](images/image_0048.png)

Figure 33  Speed dependent correction factor Kv_int [¶1688]

- 3.13.2.3.7.11.3 It shall be possible to define up to 2 sets of Kv_int with separate speed limits V1, V2, .. for each set. The sets of Kv_int relate to the following train types: [¶1689]

-  Freight trains [¶1690]

-  Conventional passenger trains [¶1691]

- 3.13.2.3.7.11.3.1 Note: Different sets of Kv_int are needed for different types of trains in order to compensate  the  absence  of  the  rolling  stock  related  correction  factors  when  the conversion model is used. [¶1692]

- 3.13.2.3.7.11.4 The set of Kv_int for conventional passenger trains shall be divided into two sub sets Kv_int_x_a and Kv_int_x_b, with identical speed limits V1, V2, .... [¶1693]

- 3.13.2.3.7.11.5 Subset Kv_int_x_a shall be applicable for maximum emergency brake deceleration lower or equal to a deceleration limit, defined as a National Value. [¶1694]

- 3.13.2.3.7.11.6 Subset Kv_int_x_b shall be applicable for maximum emergency brake deceleration greater or equal to a deceleration limit, defined as a National Value. [¶1695]

- 3.13.2.3.7.12  The  train  length  dependent  correction  factor,  Kr_int(l),  shall  be  given  as  a  step function. [¶1696]

- 3.13.2.3.7.12.1 It shall be possible to define up to five steps for Kr_int(l). [¶1697]

- 3.13.2.3.7.12.2 Note:  An  example  with  4  steps  is  given  in  Figure  34.  Kr_int  is  calculated  as follows: [¶1698]

-  Kr_int = Kr_int_0 when 0 ≤ train length ≤ L1 [¶1699]

-  Kr_int = Kr_int_1 when L1 < train length ≤ L2 [¶1700]

-  Kr_int = Kr_int_2 when L2 < train length ≤ L3 [¶1701]

-  Kr_int = Kr_int_3 when L3 < train length [¶1702]


---
<!-- pagina 134 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1703]

![](images/image_0049.png)

Figure 34  Train length dependent correction factor Kr_int [¶1704]

- 3.13.2.3.7.13  The last step of the Kv_int(V) and Kr_int(l) shall by definition be considered as open ended, i.e. it has no upper speed and train length limit, respectively. [¶1705]

- 3.13.2.3.7.14  The correction factor for brake build up time (Kt_int) shall be a single parameter. [¶1706]

# 3.13.3 Conversion Models [¶1707]

# 3.13.3.1 Introduction [¶1708]

- 3.13.3.1.1  For trains with variable composition (loco hauled trains), the brake characteristics can vary together with the composition of the train. In this case, it is not convenient to preprogram  the  brake  parameters  necessary  to  calculate  the  braking  curves.  The  only practical way to obtain the correct values for the current train composition is to include them into the data entry process by the driver. However, it cannot be expected from the driver to know deceleration values and brake build up times. Conversion models are therefore defined to convert the parameters  entered  by  the  driver (brake percentage and brake position) into the parameters of the corresponding brake model. [¶1709]

- 3.13.3.1.2  Note: The process for defining the input parameters for the conversion model (brake percentage and brake position) is outside the scope of the  ERTMS/ETCS specifications. [¶1710]

# 3.13.3.2 Applicability of the conversion models [¶1711]

- 3.13.3.2.1  The  conversion  models  shall  be  used  by  the  on-board  equipment  if  the  brake percentage  is  acquired  as  part  of  Train  Data,  and  if  the  maximum  train  speed,  the brake percentage and the train length are all within the following validity limits of the conversion models: [¶1712]

- 0 ≤ V ≤ 200, where V is the maximum train speed in km/h [¶1713]

- 30 ≤ λ ≤ 250, where λ is the brake percentage in % [¶1714]

-  0 ≤ L ≤ Lmax, where L is the train length in m and where Lmax = 900 m if the brake position is 'Passenger train in P' or Lmax = 1500 m if the brake position is 'Freight train in P' or 'Freight train in G' [¶1715]


---
<!-- pagina 135 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1716]

- 3.13.3.2.1.1 Note: The overspeed above the maximum train speed which may occur due to the ceiling speed margins is taken into account in the definition of the conversion model. [¶1717]

- 3.13.3.2.2  For trains not fitting into at least one of those validity limits, it is still possible to acquire the  brake  percentage  as  Train  Data,  but  the  conversion  models  are  not  applicable, which  means  that  braking  models  (i.e.  pre-programmed  deceleration  profiles  and brake build up times) shall be used by the speed and distance monitoring function. [¶1718]

# 3.13.3.3 Brake percentage conversion model [¶1719]

# 3.13.3.3.1  Input parameters [¶1720]

- 3.13.3.3.1.1 The  input  for  the  model  shall  be  the  brake  percentage  of  the  train  as  defined  in 3.13.2.2.5. [¶1721]

# 3.13.3.3.2  Calculation of the basic deceleration [¶1722]

- 3.13.3.3.2.1 The basic deceleration A_basic(V) shall be given as a step function of the speed using the algorithm defined in Appendix A.3.7. [¶1723]

# 3.13.3.3.3  Output parameters [¶1724]

- 3.13.3.3.3.1 The output of  the  brake  percentage  conversion  model shall  consist  of  two  speed dependent  deceleration  brake  models,  A_brake_emergency(V)  for  the  emergency brake and A_brake_service(V) for the service brake. [¶1725]

# 3.13.3.4 Brake position conversion model [¶1726]

# 3.13.3.4.1  Input parameters [¶1727]

- 3.13.3.4.1.1 The input for the model shall consist of the brake position of the train as defined in 3.13.2.2.4, the train length and the target speed. [¶1728]

# 3.13.3.4.2  Calculation of the emergency brake equivalent time [¶1729]

- 3.13.3.4.2.1 The equivalent brake build up time for the emergency brake shall be determined as specified in Appendix A.3.8. [¶1730]

# 3.13.3.4.3  Calculation of the full service brake equivalent time [¶1731]

- 3.13.3.4.3.1 The equivalent brake build up time for the full service brake shall be determined as specified in Appendix A.3.9. [¶1732]

# 3.13.3.4.4  Output parameters [¶1733]

- 3.13.3.4.4.1 The outputs of the brake position conversion model shall consist of: [¶1734]

- two values of the equivalent brake build up time to be used when the target speed (V_target) is equal to zero, one value for the emergency brake and one for the full service brake: [¶1735]

T_brake_emergency_cm0 as defined for emergency brake in A.3.8 [¶1736]


---
<!-- pagina 136 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1737]

T_brake_service_cm0 as defined for service brake in A.3.9 [¶1738]

- two values of the equivalent brake build up time to be used when the target speed (V_target) is different from zero, one value for the emergency brake and one for the full service brake: [¶1739]

T_brake_emergency_cmt as defined for emergency brake in A.3.8 [¶1740]

T_brake_service_cmt as defined for service brake in A.3.9 [¶1741]

# 3.13.4 Acceleration / Deceleration due to gradient [¶1742]

# 3.13.4.1 Introduction [¶1743]

- 3.13.4.1.1  The elements of the gradient profile given from trackside shall be compensated: [¶1744]

- in location according to the train length as defined in 3.13.4.2 [¶1745]

- in value according to the rotating mass as defined in 3.13.4.3 in order to derive the corresponding acceleration/deceleration. [¶1746]

Black: defined by trackside [¶1747]

![](images/image_0050.png)

Figure 35: Compensation on the gradient profile [¶1748]


---
<!-- pagina 137 -->

- 3.13.4.1.2  The default gradient for TSR shall be compensated in value according to the rotating mass as defined in 3.13.4.3. [¶1749]

- 3.13.4.1.3  For  all  locations  not  covered  by  the  gradient  profile,  the  on-board  shall  consider  the gradient value as: [¶1750]

- the default gradient for TSR, if available and if the concerned target is due to a TSR [¶1751]

- zero, for other cases. [¶1752]

# 3.13.4.2 Train length compensation [¶1753]

- 3.13.4.2.1  Assuming that a fictive train front  end  would  be at any location between the current (actual) train front end location and the SvL, the acceleration due to the gradient shall be determined using the lowest (taking the sign into account) gradient value given by the gradient profile between the location of the fictive train front end and the location of the fictive train rear end (see Figure 35). [¶1754]

# 3.13.4.3 Rotating mass [¶1755]

- 3.13.4.3.1  The influence of gradients shall be compensated for the rotating mass of the train (see Figure 35). [¶1756]

- 3.13.4.3.1.1 Note: Since the rotating mass works like a flywheel (rotating inertia), the effect of the gradient is reduced. Assume for instance a (theoretical) train without any rotating mass,  not  braking,  on  a  downhill  gradient  from  height  1  to  height  2.  All  the  energy added to the train when it goes from H1 to H2 is converted into linear forward motion. This can be observed as an acceleration due to the gradient. Now assume the same train with part of the weight rotating. If this train travels the same distance from H1 to H2, the same amount of energy is added to the train. But now a part of that energy is converted  into  rotational  motion  and  only  the  remaining  part  is  converted  into  linear forward motion. The latter can be observed as an acceleration which is less than for the train without rotating mass. [¶1757]

- 3.13.4.3.1.2 Note: For the influence of the rotating mass on the deceleration due to the brake, it is already taken into account in the values for the brake parameters. [¶1758]

- 3.13.4.3.2  The following formulas shall be used: [¶1759]

- If M_rotating_nom is unknown: [¶1760]

-  Uphill: A_gradient = g * grad / (1000+10*M_rotating_max) [¶1761]

-  Downhill: A_gradient = g * grad / (1000+10*M_rotating_min) [¶1762]

- If M_rotating_nom is known: [¶1763]

-  Uphill: A_gradient = g * grad / (1000+10*M_rotating_nom) [¶1764]

-  Downhill: A_gradient = g * grad / (1000+10*M_rotating_nom) [¶1765]

Legend: [¶1766]

- A_gradient = acceleration/deceleration due to gradient [¶1767]


---
<!-- pagina 138 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1768]

g = 9.81 m/s 2  - acceleration of gravity in m/s 2 [¶1769]

grad = gradient values in ‰ (positive = uphill) [¶1770]

M_rotating_nom = nominal rotating mass (part of train data)  as a percentage of the total train weight [¶1771]

M_rotating_max = maximum possible rotating mass (see A.3.1) as a percentage of the total train weight [¶1772]

M_rotating_min = minimum possible rotating mass (see A.3.1) as a percentage of the total train weight [¶1773]

# 3.13.5 Determination of locations without special brake contribution and with reduced adhesion conditions [¶1774]

- 3.13.5.1 As  long  as  it  uses  a  track  condition  profile  given  by  trackside,  the  on-board  shall consider  locations  without  special  brake  contribution  over  a  distance  going  from  the start location of the profile to the foot of the deceleration curve (EBD, SBD or GUI, see sections 3.13.8.3, 3.13.8.4 and 3.13.8.5). [¶1775]

- 3.13.5.2 If the status of a special brake is 'not active', all locations shall be considered without the contribution of this special brake. [¶1776]

- 3.13.5.2.1  Note: in such case, a track condition profile implying the inhibition of this special brake will have no effect. [¶1777]

- 3.13.5.3 From the adhesion profile given by trackside, the on-board shall consider locations with reduced adhesion conditions over a distance going from the start location of the profile to the location derived by adding the train length to the end location of the profile. [¶1778]

- 3.13.5.4 When  slippery  rail  is  selected  by  the  driver,  all  locations  shall  be  considered  with reduced adhesion conditions. [¶1779]

- 3.13.5.5 The  speed  and  distance monitoring shall use, as resulting  reduced  adhesion conditions, the most restrictive value of the adhesion conditions selected by the driver and the adhesion conditions calculated from the trackside profile. [¶1780]

# 3.13.6 Calculation of the deceleration and brake build up time [¶1781]

# 3.13.6.1 Introduction [¶1782]

- 3.13.6.1.1  This chapter describes how the safe emergency brake, the expected and the normal service  brake  decelerations  and  the  time  intervals  due  to  brake  build  up  time  are calculated. [¶1783]

# 3.13.6.2 Emergency brake [¶1784]

# 3.13.6.2.1  Safe deceleration [¶1785]


---
<!-- pagina 139 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1786]

- 3.13.6.2.1.1 The  safe  deceleration,  A_safe(V,d),  is  safety  relevant.  This  means  that  for  the calculation of the safe deceleration, all necessary track and train characteristics shall be taken into account. [¶1787]

- 3.13.6.2.1.2 The train and track related characteristics to be considered are: [¶1788]

- The  speed  dependent  deceleration  model(s)  for  the  emergency  brake  either acquired  as  part  of  Train  Data  (see  3.13.2.2.3.1)  or  derived  from  the  brake percentage using the conversion model (see 3.13.3.3) [¶1789]

- The acceleration/deceleration due to gradient i.e. A_gradient(d) (see 3.13.4) [¶1790]

-  The locations with reduced adhesion conditions (see 3.13.5) [¶1791]

- The National Values for reduced adhesion condition (see 3.13.2.3.7.7) [¶1792]

- The  locations  without  special  brake  contribution  (see  3.13.5),  only  if  the  speed dependent deceleration model(s) for the emergency brake are acquired as part of Train Data [¶1793]

-  The  rolling  stock  correction  factors  Kdry_rst(V,  EBCL)  and  Kwet_rst(V)  (see 3.13.2.2.9.1), only if the speed dependent deceleration model(s) for the emergency brake are acquired as part of Train Data [¶1794]

- The National Values for confidence level on emergency brake safe deceleration and for  the  available  wheel/rail  adhesion  (see  3.13.2.3.7.5  &  3.13.2.3.7.6),  only  if  the speed dependent deceleration model(s) for the emergency brake are acquired as part of Train Data [¶1795]

- The integrated correction factors Kv_int(V) (with the two pivot deceleration values for passenger trains) and Kr_int(l) (see 3.13.2.3.7), only if the conversion model is used [¶1796]

- The brake position (see 3.13.2.2.4) [¶1797]

-  The acquired train length L_TRAIN (see 3.13.2.2.11), only if the conversion model is used [¶1798]

- 3.13.6.2.1.3 A_safe(V,d) shall be equal to: [¶1799]

For  locations  with  normal  adhesion  conditions  and  for  locations  with  reduced adhesion conditions when A_MAXREDADH does not limit to a maximum value the speed dependent deceleration for the emergency brake: [¶1800]

A_safe(V,d) = A_brake_safe(V,d) + A_gradient(d) [¶1801]

For locations with reduced adhesion conditions when A_MAXREDADH limits to a maximum value the speed dependent deceleration for the emergency brake: [¶1802]

A_safe(V,d) = MIN(A_brake_safe(V,d) , A_MAXREDADH) + A_gradient(d) [¶1803]

- 3.13.6.2.1.4 A_brake_safe(V,d) shall be the safe emergency brake deceleration. A_brake_safe(V,d) shall be equal to: [¶1804]


---
<!-- pagina 140 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1805]

If  the  speed  dependent  deceleration  model(s)  for  the  emergency  brake  are acquired as part of Train Data: [¶1806]

A_brake_safe(V,d) = Kdry_rst(V, M_NVEBCL) * (Kwet_rst(V) + M_NVAVADH *(1- Kwet_rst(V))) * A_brake_emergency(V,d) [¶1807]

If the conversion model is used: [¶1808]

A_brake_safe(V) = Kv_int(V) * Kr_int(L_TRAIN) * A_brake_emergency(V) [¶1809]

3.13.6.2.1.5 A_brake_emergency(V,d) shall be the emergency brake deceleration as a function of the speed, of the locations with change of special brake(s) contribution encountered between the train front and the foot of the EBD curve. A_brake_emergency(V,d) shall be equal to: [¶1810]

A_brake_emergency1(V) when destfront ≤ d ≤ d1 [¶1811]

A_brake_emergency2(V) when d1 < d ≤ d2 [¶1812]

A_brake_emergency3(V) when d2 < d ≤ d3 [¶1813]

.... [¶1814]

# Where [¶1815]

d1, d2, d3,... are the locations with change of special brake(s) contribution [¶1816]

A_brake_emergencyx(V) is equal to the emergency brake model, A_brake_emergency, applicable for the concerned combination of brake. [¶1817]

![](images/image_0051.png)

Figure 36: Influence of track conditions on A_brake_emergency(V,d) [¶1818]

- 3.13.6.2.1.6 A_MAXREDADH  shall  be  the  value,  out  of  the  three  related  National  Values, applicable for this train according to: [¶1819]

- its brake position [¶1820]

- whether special/additional brakes independent from wheel/rail adhesion are active and it  is  allowed  to  take  into  account  their  contribution  to  the  emergency  braking effort. [¶1821]


---
<!-- pagina 141 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1822]

- 3.13.6.2.1.7 Kdry_rst(V, M_NVEBCL) shall be the rolling stock correction factor, as a function of speed (with speed steps identical with the ones of A_brake_emergency(V)), corresponding to the confidence level on emergency brake safe deceleration required by trackside (National Value). [¶1823]

- 3.13.6.2.1.8 Kv_int(V) shall be the integrated correction factor applicable for the train, selected according to the brake position. [¶1824]

- 3.13.6.2.1.8.1 If the brake position is 'Passenger train in P', the set of Kv_int shall be calculated as  a  function  of  the  maximum  emergency  brake  deceleration  (A_ebmax)  in  the following way (see also figure 10): [¶1825]

- 3.13.6.2.1.8.2 The maximum EB deceleration A_ebmax shall be the maximum of A_brake_emergency between 0 km/h and the maximum speed of the train. [¶1826]

- 3.13.6.2.1.9 Note:  Figure  38  gives  an  example  of  the  influence  of  the  various  track/train characteristics on A_safe(V,d) and consequently on the EBD curve (see 3.13.8.3). [¶1827]

Kv_int_x = Kv_int_x_a [¶1828]

when A_ebmax ≤ A_P12. [¶1829]

Kv_int_x = Kv_int_x_b [¶1830]

when A_ebmax ≥ A_P23. [¶1831]

Kv_int_x  =  Kv_int_x_a  +  (A_ebmax  -  A_P12)/(A_P23  -  A_P12)  *  (Kv_int_x_b  - [¶1832]

Kv_int_x_a) [¶1833]

when A_P12 < A_ebmax < A_P23.' [¶1834]

![](images/image_0052.png)

Figure 37: Kv_int structure for conventional passenger trains [¶1835]


---
<!-- pagina 142 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1836]

![](images/image_0053.png)

Figure 38: Influence of track/train characteristics on A_safe [¶1837]

# 3.13.6.2.2  Safe brake build up time [¶1838]

- 3.13.6.2.2.1 The  safe  brake  build  up  time,  T_be,  is  safety  relevant.  This  means  that  for  the calculation of the safe brake build up time, all necessary track and train characteristics shall be taken into account. [¶1839]

- 3.13.6.2.2.2 The train and track related characteristics to be considered are: [¶1840]

- The values of T_brake_emergency acquired as part of Train Data (see 3.13.2.2.3.2.8)  or  the  value  of  T_brake_emergency  derived  from  the  conversion model  (see  3.13.3.4)  using  the  brake  position  and  train  length  acquired  as  Train Data. [¶1841]

- The integrated correction factor Kt_int, only if the conversion model is used  (see 3.13.2.3.7) [¶1842]

-  The status of the regenerative brake, eddy current brake, magnetic shoe brake and Ep  brake  system  (see  3.13.2.2.6),  only  if  the  values  of  T_brake_emergency  are acquired as part of Train Data [¶1843]

- 3.13.6.2.2.3 The safe brake build up time T_be shall be equal to: [¶1844]

If values of T_brake_emergency are acquired as part of Train Data: [¶1845]

T_be  =  T_brake_emergency,  with  T_brake_emergency  corresponding  to  the combination of special brakes currently in use [¶1846]

If the conversion model is used: [¶1847]

T_be = Kt_int * T_brake_emergency [¶1848]

# 3.13.6.3 Service brake [¶1849]

# 3.13.6.3.1  Expected deceleration [¶1850]


---
<!-- pagina 143 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1851]

- 3.13.6.3.1.1 Since  the  expected  deceleration  is  not  safety  relevant,  no  worst  case  conditions (e.g.  correction  factors,  adhesion  conditions)  need  to  be  taken  into  account  for  its calculation. [¶1852]

- 3.13.6.3.1.2 The train and track related characteristics to be considered are: [¶1853]

- The  speed  dependent  deceleration  model(s)  for  the  full  service  brake  either acquired  as  part  of  Train  Data  (see  3.13.2.2.3.1)  or  derived  from  the  brake percentage using the conversion model (see 3.13.3.3) [¶1854]

- The acceleration/deceleration due to gradient i.e. A_gradient(d) (see 3.13.4) [¶1855]

-  The locations without special brake contribution (see 3.13.5) [¶1856]

- 3.13.6.3.1.3 A_expected(V,d) shall be equal to: [¶1857]

A_expected(V,d) = A_brake_service(V,d) +A_gradient(d) [¶1858]

- 3.13.6.3.1.4 A_brake_service(V,d)  shall  be  the  full  deceleration  of  the  service  brake  as  a function  of  the  speed,  of  the  locations  with  change  of  special  brake(s)  contribution encountered between the train front and the foot of the SBD curve. A_brake_service(V,d) shall be equal to: [¶1859]

A_brake_service1(V) when destfront ≤ d ≤ d1 [¶1860]

A_brake_service2(V) when d1 < d ≤ d2 [¶1861]

A_brake_service3(V) when d2 < d ≤ d3 [¶1862]

.... [¶1863]

# Where [¶1864]

d1, d2, d3,... are the locations with change of special brake(s) contribution [¶1865]

A_brake_servicex(V) is equal  to  the  full  service  brake  model,  A_brake_service, applicable for the concerned combination of brake. [¶1866]

# 3.13.6.3.2  Expected brake build up time [¶1867]

- 3.13.6.3.2.1 [¶1868]

- Since  the  expected  brake  build  up  time  is  not  safety  relevant,  no  worst  case conditions (e.g. correction factors, adhesion conditions) need to be taken into account for its calculation. [¶1869]

- 3.13.6.3.2.2 No track related characteristics are to be considered for the expected brake build up time. [¶1870]

- 3.13.6.3.2.3 The train related characteristics to be considered are: [¶1871]

- The values of T_brake_service acquired as part of Train Data (see 3.13.2.2.3.2.8) or  the  value(s)  of  T_brake_service  derived  from  the  conversion  model  (see 3.13.3.4) using the brake position and train length acquired as Train Data) [¶1872]

- The status of the regenerative brake, eddy current brake and Ep brake system (see 3.13.2.2.6) [¶1873]


---
<!-- pagina 144 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1874]

- 3.13.6.3.2.4 The expected brake build up time T_bs shall be equal to the brake build up time of the full service brake: [¶1875]

T_bs  =  T_brake_service,  with  T_brake_service  corresponding  to  the  combination  of special brakes currently in use [¶1876]

# 3.13.6.4 Normal service brake deceleration [¶1877]

- 3.13.6.4.1  Since  the  normal  service  brake  deceleration  is  not  safety  relevant,  no  worst  case conditions (e.g. correction factors, adhesion conditions) need to be taken into account for its calculation. [¶1878]

- 3.13.6.4.2  The train and track related characteristics to be considered are: [¶1879]

- The  speed  dependent  deceleration  model(s)  for  the  full  service  brake  either acquired  as  part  of  Train  Data  (see  3.13.2.2.3.1)  or  derived  from  the  brake percentage using the conversion model (see 3.13.3.3) [¶1880]

- The speed dependent deceleration model(s) for the normal service brake acquired as part of Train Data (see 3.13.2.2.3.1) [¶1881]

-  The acceleration/deceleration due to gradient i.e. A_gradient(d) (see 3.13.4) [¶1882]

- The brake position (see 3.13.2.2.4) [¶1883]

- The on-board correction factors Kn+(V) and Kn-(V) (see 3.13.2.2.9.2) [¶1884]

-  The locations without special brake contribution (see 3.13.5) [¶1885]

- 3.13.6.4.3  The normal service brake deceleration shall be equal to: [¶1886]

For positive gradient values (uphill): [¶1887]

A_normal_service(V,d) = A_brake_normal_service(V,d) + A_gradient(d) - [¶1888]

Kn+(V)*grad/1000 [¶1889]

For negative gradient values (downhill): [¶1890]

A_normal_service(V,d) = A_brake_normal_service(V,d) + A_gradient(d) Kn-(V)*grad/1000 [¶1891]

Where [¶1892]

grad = gradient values in ‰ (positive = uphill) [¶1893]

- 3.13.6.4.4  A_brake_normal_service(V,d) shall be the normal deceleration of the service brake as a function of the speed, of the locations with change of special brake(s) contribution encountered between the train front and the foot of the GUI curve. A_brake_normal_service(V,d) shall be equal to: [¶1894]

A_brake_normal_service1(V) when destfront ≤ d ≤ d1 [¶1895]

A_brake_normal_service2(V) when d1 < d ≤ d2 [¶1896]

A_brake_normal_service3(V) when d2 < d ≤ d3 [¶1897]

.... [¶1898]

Where [¶1899]


---
<!-- pagina 145 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1900]

d1, d2, d3,... are the locations with change of special brake(s) contribution [¶1901]

A_brake_normal_servicex(V) is equal to the normal service brake model applicable for the concerned combination of brake position and of the value of A_brake_service(V=0) between dx-1 and dx (see 3.13.2.2.3.1.9 and 3.13.2.2.3.1.10). [¶1902]

# 3.13.7 Determination of Most Restrictive Speed Profile (MRSP) [¶1903]

- 3.13.7.1 The  Most  Restrictive  Speed  Profile  (MRSP)  is  a  description  of  the  most  restrictive speed restrictions the train shall obey on a given piece of track. [¶1904]

- 3.13.7.2 The Most Restrictive Speed Profile shall be computed from all speed restrictions (see 3.13.2.2.13 & 3.13.2.3.2) by selecting the most restrictive parts of each element, some elements  being  compensated  by  the  train  length  if  requested  by  trackside  (see 3.11.3.1.3 for SSP, 3.11.4.6 for ASP and 3.11.5.3 for TSR). [¶1905]

- 3.13.7.3 The Most Restrictive Speed Profile shall be recalculated when any of the elements it is built of is changed. [¶1906]

![](images/image_0054.png)

Figure 39: Most Restrictive Speed Profile selection [¶1907]

# 3.13.8 Determination of targets and brake deceleration curves [¶1908]

# 3.13.8.1 Introduction [¶1909]

- 3.13.8.1.1  A  target  is  defined  by  a  target  location  and  a  target  speed,  to  which  the  train  must decelerate before reaching the target location. [¶1910]

- 3.13.8.1.2  For that purpose, the on-board equipment shall use brake deceleration curves related to  the  supervised  targets,  from  the  deceleration  values  as  specified  in  sections 3.13.6.2.1, 3.13.6.3.1and 3.13.6.4. [¶1911]

- 3.13.8.1.3  These deceleration values being speed and distance dependent, a brake deceleration curve shall be calculated piecewise, i.e. it shall be composed of interconnected arcs of [¶1912]


---
<!-- pagina 146 -->

parabola, each one being based on one of the speed/distance dependent deceleration values (see Figure 38). [¶1913]

# 3.13.8.2 Determination of the supervised targets [¶1914]

- 3.13.8.2.1  The  on-board  shall  continuously  supervise  a  list  of  targets,  which  may  include  the following types of target: [¶1915]

- the locations corresponding to a speed decrease of the MRSP (if any), which are in advance of the max safe front end of the train [¶1916]

- the Limit of Authority (LOA) [¶1917]

-  the End of Authority (EOA) and the Supervised Location (SvL) [¶1918]

- the  location  deduced  from  the  maximum  permitted  distance  to  run  in  Staff Responsible, with a target speed zero [¶1919]

- 3.13.8.2.1.1 Note: depending on the information received from trackside and the position of the train, the list of supervised targets may be empty. [¶1920]

- 3.13.8.2.2  The list of supervised targets shall be re-evaluated when any of the elements it is built of is changed (e.g. new MA and/or track description accepted on-board, EOA and/or SvL  temporarily  supervised  at  the  start  location  of  a  mode  profile,  update  of  stored information in specific situations (see sections A.3.4 and 4.10)). [¶1921]

- 3.13.8.2.3  A target corresponding to a speed decrease of the MRSP shall be removed from the list  of  supervised  targets  when  the  max  safe  front  end  of  the  train  has  passed  the target location. [¶1922]

# 3.13.8.3 Emergency Brake Deceleration curves (EBD) [¶1923]

- 3.13.8.3.1  If  a  target  belongs  to  the  MRSP  or  is  an  LOA,  the  on-board  shall  calculate  an  EBD curve based on the safe deceleration A_safe(V,d), that crosses the ceiling speed EBI supervision  limit  (see  3.13.9.2)  at  the  target  location,  and  that  extends  up  to  the location where the target speed is reached (EBD foot). [¶1924]


---
<!-- pagina 147 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1925]

![](images/image_0055.png)

Figure 40: Calculation of the EBD curve with regards to MRSP or LOA target [¶1926]

- 3.13.8.3.2  If  a target is an  SvL, the on-board shall calculate an Emergency Brake Deceleration (EBD) curve based on the safe deceleration A_safe(V,d) and that reaches zero speed at the SvL. [¶1927]

- 3.13.8.3.3  If a target is the location at the end of the maximum permitted distance to run in Staff Responsible,  the  on-board  shall  calculate  an  Emergency  Brake  Deceleration  (EBD) curve based on the safe deceleration A_safe(V,d) and that reaches zero speed at this staff responsible end location. [¶1928]

![](images/image_0056.png)

Figure 41: Calculation of the EBD curve with regards to SvL or SR distance [¶1929]

# 3.13.8.4 Service Brake Deceleration curves (SBD) [¶1930]


---
<!-- pagina 148 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1931]

- 3.13.8.4.1  If  a  target  is  an  EOA,  the  on-board  shall  calculate  an  Service  Brake  Deceleration (SBD) curve based on the expected deceleration A_expected(V,d) and that reaches zero speed at this EOA location. [¶1932]

![](images/image_0057.png)

Figure 42: Calculation of the SBD curve with regards to EOA [¶1933]

# 3.13.8.5 Guidance curves (GUI) [¶1934]

- 3.13.8.5.1  The purpose of the guidance curve (GUI) is to provide a comfortable way of braking for the driver, to avoid excessive wear of the brakes and to save traction energy. [¶1935]

- 3.13.8.5.2  If  the  National  Value  does  not  inhibit  them,  the  on-board  shall  calculate  a  guidance curve (GUI) for each supervised target, based on the normal service brake deceleration A_normal_service(V,d). The foot of a GUI curve (i.e. the location where the GUI speed is equal to the target speed) shall be: [¶1936]

- the target location, in case of EOA/SvL [¶1937]

- the location defined in 3.13.9.3.5.9, for others targets [¶1938]

# 3.13.9 Supervision limits [¶1939]

# 3.13.9.1 Overview [¶1940]

- 3.13.9.1.1  In this chapter the following supervision limits are defined: [¶1941]

-  Emergency brake intervention (EBI) [¶1942]

-  Service brake intervention (SBI) [¶1943]

-  Warning (W) [¶1944]

-  Permitted speed (P) [¶1945]

-  Indication (I) [¶1946]


---
<!-- pagina 149 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1947]

-  Release speed monitoring start location [¶1948]

- 3.13.9.1.2  The purpose of the emergency brake intervention supervision limit is to assure that the train will remain within the various limits (in distance/speed) imposed by the trackside. [¶1949]

- 3.13.9.1.3  The  purpose  of  all  other  supervision  limits  is  to  assist  the  driver  in  preventing  an emergency  brake  intervention  by  maintaining  the  speed  of  the  train  within  the appropriate limits. [¶1950]

# 3.13.9.2 Ceiling supervision limits [¶1951]

- 3.13.9.2.1  The ceiling supervision limits are derived from the MRSP elements, where the speed is constant (refer to 3.13.7) or from the LOA. [¶1952]

- 3.13.9.2.2  From  an  MRSP  element  or  from  the  LOA,  the  Permitted  speed,  Warning,  Service brake  intervention  and  Emergency  brake  intervention  supervision  limits  are  defined (see Figure 43). [¶1953]

- 3.13.9.2.3  For dv_ebi, the following formula shall be applied: [¶1954]

![](images/image_0058.png)

Figure 43: Ceiling supervision limits [¶1955]

$$
3 . 1 3 . 9 . 2 . 3 & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
$$ [¶1956]


---
<!-- pagina 150 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1957]

![](images/image_0059.png)

Figure 44: Definition of dV_ebi [¶1958]

- 3.13.9.2.4  dV_ebi_min, dV_ebi_max, V_ebi_min and V_ebi_max are defined as fixed values (See Appendix A.3.1) [¶1959]

- 3.13.9.2.5  For  dV_sbi,  the  same  formula  as  for  dV_ebi  shall  apply,  dV_sbi_min,  dV_sbi_max, V_sbi_min and V_sbi_max being also defined as fixed values (See Appendix A.3.1) [¶1960]

- 3.13.9.2.6  For  dV_warning,  the  same  formula  as  for  dV_ebi  shall  apply,  dV_warning_min, dV_warning_max,  V_warning_min  and  V_warning_max  being  also  defined  as  fixed values (See Appendix A.3.1) [¶1961]

- 3.13.9.2.7  For LOA, the same formulas shall apply, by substituting V_MRSP with the LOA speed. [¶1962]

- 3.13.9.2.8  Intentionally deleted. [¶1963]

# 3.13.9.3 Braking to target supervision limits [¶1964]

# 3.13.9.3.1  Overview [¶1965]

- 3.13.9.3.1.1 The braking to target  supervision limits  are  derived  from  the  EBD,  SBD  and  GUI curves. [¶1966]

- 3.13.9.3.1.2 From  an  EBD  curve,  the  Emergency  brake  intervention  (EBI),  Service  brake intervention  (SBI2),  Warning  (W),  Permitted  speed  (P)  and  Indication  (I)  supervision limits, valid for the estimated speed, are defined as follows(see Figure 45): [¶1967]


---
<!-- pagina 151 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1968]

![](images/image_0060.png)

Figure 45: Braking to target supervision limits from EBD curve [¶1969]

- 3.13.9.3.1.3 From  the  SBD  curve,  Service  brake  intervention  (SBI1),  Warning  (W),  Permitted speed  (P)  and  Indication  (I)  supervision  limits,  valid  for  the  estimated  speed,  are defined as follows (see Figure 46): [¶1970]

- 3.13.9.3.1.4 No  specific  supervision  limit  is  calculated  from  the  GUI  curve:  it  is  only  used  to adjust the Permitted speed (P) supervision limit, which is obtained either from the EBD or the SBD curve. [¶1971]

![](images/image_0061.png)

Figure 46: Braking to target supervision limits from SBD curve [¶1972]

# 3.13.9.3.2  EBI supervision limit [¶1973]

- 3.13.9.3.2.1 If  not  inhibited  by  National  Value,  the  ERTMS/ETCS  on-board  equipment  shall compensate  the  inaccuracy  of  the  speed  measurement  by  taking  into  account  the [¶1974]


---
<!-- pagina 152 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1975]

speed  under  reading  amount  (V_ura)  at  the  moment  when  the  calculation  is  made: V_delta0 = V_ura (see Figure 45). [¶1976]

- 3.13.9.3.2.2 The time elapsed between the Emergency brake intervention and the full application of the braking effort is reached (EBD) shall be split into two parts: [¶1977]

- Time during which the traction effort is still present: T_traction [¶1978]

- Remaining time during which the traction effort is not present: T_berem [¶1979]

- 3.13.9.3.2.3 The traction time (T_Traction) shall be defined as follows: [¶1980]

- when the traction cut-off is implemented: [¶1981]

T_traction = MAX((T_traction_cut_off - (T_warning + T_bs2)) ; 0). [¶1982]

- when the traction cut-off is not implemented: T_traction = T_traction_cut_off [¶1983]

- 3.13.9.3.2.4 Note:  When  the  traction  cut-off  is  implemented,  the  traction  cut-off  command  is triggered  when  passing  the  warning  limit.  The  term  (T_warning  +  T_bs2)  in  the equation above takes this into account, assuming that the warning limit is derived from the EBD. [¶1984]

- 3.13.9.3.2.5 T_bs2 and T_warning are defined in sections 3.13.9.3.3 and 3.13.9.3.4. [¶1985]

- 3.13.9.3.2.6 The  remaining  time  with  no  traction  (T_berem)  shall  be  equal  to  MAX(T_be  -T_traction ; 0). [¶1986]

- 3.13.9.3.2.7 Note: T_Traction exceeding T_be is rather a theoretical case, but is nevertheless included to make the specifications complete. [¶1987]

- 3.13.9.3.2.8 During T_traction, the estimated acceleration (A_est1) shall be the one measured at the moment when the calculation is made, but limited to positive or null values. [¶1988]

- 3.13.9.3.2.9 If  T_be > T_traction, the estimated acceleration during T_berem (A_est2) shall be the one measured at the moment when the calculation is made, but limited to values between 0 and +0.4m/s 2 . [¶1989]

- 3.13.9.3.2.10  The  compensated  speed  and  the  distance  travelled  during  the  time  elapsed between the Emergency brake intervention and the full application of the braking effort is reached shall be derived as follows (see Figure 45): [¶1990]

$$
V _ { b e c } = \max \left \{ ( V _ { e s t } + V _ { d e l t a 0 } + V _ { d e l t a 1 } ) , V _ { t \arg e t } \right \} + V _ { d e l t a 2 }
$$ [¶1991]

$$
V _ { b e c } = & \max \left \{ ( V _ { e s t } + V _ { d e l t a 0 } + V _ { d e l t a 1 } ) , V _ { t \arg e t } \right \} + V _ { d e l t a 2 } \\ & D _ { b e c } = \max \left \{ ( V _ { e s t } + V _ { d e l t a 0 } + \frac { V _ { d e l t a 1 } } { 2 } ) , V _ { t \arg e t } \right \} . T _ { \text {traction} } \\ + & \left ( \max \left \{ ( V _ { e s t } + V _ { d e l t a 0 } + V _ { d e l t a 1 } ) , V _ { t \arg e t } \right \} + \frac { V _ { d e l t a 2 } } { 2 } \right ) . T _ { b e r e m }
$$ [¶1992]


---
<!-- pagina 153 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶1993]

with ura delta V V  0 or 0 0  delta V (if  compensation  of  speed  inaccuracy  is  inhibited  by National Value) [¶1994]

$$
\text {with } V _ { d e l t a 1 } = A _ { e s t 1 } \cdot T _ { t r a c t i o n } \text { and } V _ { d e l t a 2 } = A _ { e s t 2 } \cdot T _ { b e r e m }
$$ [¶1995]

3.13.9.3.2.11  Note: The formula avoids that V_bec is lower than V_target. [¶1996]

3.13.9.3.2.12  For the estimated speed V_est, the location of the EBI supervision limit shall be: [¶1997]

$$
d _ { E B I } \left ( V _ { e s t } \right ) = d _ { E B D } \left ( V _ { b e c } \right ) - D _ { b e c }
$$ [¶1998]

# 3.13.9.3.3  SBI supervision limit [¶1999]

- 3.13.9.3.3.1 For the EOA, the on-board shall calculate the location of the SBI supervision limit (SBI1) valid for the estimated speed, assuming that this latter remains constant during the interval T_bs1, until the SBD curve is reached. [¶2000]

$$
d _ { S B I 1 } ( V _ { e s t } ) = d _ { S B D } ( V _ { e s t } ) - V _ { e s t } \cdot T _ { b s 1 }
$$ [¶2001]

- 3.13.9.3.3.2 For  an  EBD  based  target,  the  on-board  shall  calculate  the  location  of  the  SBI supervision limit (SBI2) valid for the estimated speed, assuming that this latter remains constant  during  the  interval  T_bs2,  until  the  location  of  the  EBI  supervision  limit  is reached. [¶2002]

$$
d _ { S B I 2 } ( V _ { e s t } ) = d _ { E B I } \left ( V _ { e s t } \right ) - V _ { e s t } \cdot T _ { b s 2 }
$$ [¶2003]

- 3.13.9.3.3.3 If the service brake command is available for use and the service brake feedback is not available for use, T_bs1 and T_bs2 shall be equal to T_bs. [¶2004]

- 3.13.9.3.3.4 If both the service brake command and the service brake feedback are available for use, T_bs1 and T_bs2 shall by default be set to T_bs. When the service brake is used by  the  driver  in  target  speed  monitoring  or  release  speed  monitoring,  they  shall  be reduced and possibly locked to the respective fixed values of 0s and T_bs2_locked, until  the  ceiling  speed  monitoring  is  entered;  they  are  then  reset  to  T_bs  (refer  to detailed algorithm in Appendix A.3.10). [¶2005]

- 3.13.9.3.3.4.1 In case T_bs < T_bs2_locked then T_bs2 shall be equal to T_bs2_locked. [¶2006]

- 3.13.9.3.3.5 If the service brake command is not available for use, T_bs1 and T_bs2 shall be set to zero. [¶2007]

- 3.13.9.3.3.6 Note:  The  values  T_bs1  and  T_bs2  =  0s  are  defined  to  achieve  the  maximum performance when service brake command is not used. [¶2008]

- 3.13.9.3.3.7 For display purpose only, the SBI1 speed for the estimated train front end, shall be calculated as follows (see Figure 47): [¶2009]

$$
V _ { S B I 1 } ( d _ { e s t f r o n t } ) = V _ { S B D } \left ( d _ { e s t f r o n t } + V _ { e s t } \cdot T _ { b s 1 } \right )
$$ [¶2010]


---
<!-- pagina 154 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2011]

$$
V _ { S B I 1 } ( d _ { e s t f r o n t } ) = 0 \text { if } d _ { e s t f r o n t } + V _ { e s t } \cdot T _ { b s 1 } \geq d _ { E o A }
$$ [¶2012]

![](images/image_0062.png)

Figure 47: Calculation of SBI1 speed displayed to the driver [¶2013]

3.13.9.3.3.8 For  display  purpose  only,  the  SBI2  speed  for  the  max  safe  front  end  of  the  train shall be calculated as follows (see Figure 48): [¶2014]

$$
) \}
$$ [¶2015]

$$
\text {shall be calculated as follows (see Figure 48):} \\ V _ { S B 2 } ( d _ { \max. safefrofront } ) = \\ \max \left \{ \left ( V _ { E B D } \left ( d _ { \max. safefrofront } + V _ { \ e s t } \cdot T _ { b s 2 } + D _ { b e _ { \displaystyle b s y } } \right ) - \left ( V _ { d e l t a 0 } + V _ { d e l t a 1 } + V _ { d e l t a 2 } \right ) \right ) \left ( V _ { \arg e t } + d V _ { S b i } \right ) \left ( V _ { \arg e t } \right ) \right \} \\ \\ V _ { S B 2 } ( d _ { \max. safefrofront } ) = V _ { t \arg e t } + d V _ { s b i } \left ( V _ { \arg e t } \right ) \text { if} \\ d _ { \max. safefrofront } + V _ { e s t } \cdot T _ { b s 2 } + D _ { b e _ { \displaystyle b s y } } \geq d _ { E B D } \left ( V _ { \arg e t } \right ) \\ \text {With } V _ { \ } d e l t a 0 , \, V _ { \ } d e l t a 1 \text { and } V _ { \ } d e l t a 2 \text { calculated according to } 3 . 1 3 . 9 . 3 . 2 . 1 0 \\ \\ \text {With } D _ { b e _ { \displaystyle b s y } } = \left ( V _ { \ e s t } + V _ { d e l t a 0 } + \frac { V _ { d e l t a 1 } } { 2 } \right ) \cdot T _ { t r a c i n } + \left ( V _ { \ e s t } + V _ { d e l t a 0 } + V _ { d e l t a 1 } + \frac { V _ { d e l t a 2 } } { 2 } \right ) \cdot T _ { b e r e m }
$$ [¶2016]

$$
\text {With } D _ { b e _ { d i s p l a y } } = ( V _ { e s t } + V _ { d e l t a 0 } + \frac { V _ { d e l t a 1 } } { 2 } ) \cdot T _ { t r a c t i o n } + \left ( V _ { e s t } + V _ { d e l t a 0 } + V _ { d e l t a 1 } + \frac { V _ { d e l t a 2 } } { 2 } \right ) \cdot T _ { b e r e m }
$$ [¶2017]


---
<!-- pagina 155 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2018]

![](images/image_0063.png)

Figure 48: Calculation of SBI2 speed displayed to the driver [¶2019]

- 3.13.9.3.3.8.1 Note:  the  re-use  of  the  same  distance  travelled  and  speed  increase  between  the SBI2 supervision limit and the EBD, as for the estimated speed (see Figure 48), leads to an overestimation/underestimation of the SBI2 speed to be displayed to the driver. This  simplification,  which  avoids  the  need  of  an  iterated  calculation,  is  however acceptable and necessary since the error made tends to zero when the train reaches the SBI2 supervision limit. [¶2020]

- 3.13.9.3.3.9 Intentionally deleted. [¶2021]

# 3.13.9.3.4  Warning supervision limit (W) [¶2022]

- 3.13.9.3.4.1 The on-board shall calculate the location of the Warning supervision limit valid for the  estimated  speed,  assuming  that  this  latter  remains  constant  during  the  interval T_warning until the location of the SBI1 (for the EOA) or the SBI2 (for an EBD based target) supervision limit is reached. [¶2023]

$$
d _ { W } ( V _ { e s t } ) = d _ { S B I 1 } ( V _ { e s t } ) - V _ { e s t } \cdot T _ { w a r n i n g }
$$ [¶2024]

$$
d _ { W } ( V _ { e s t } ) = d _ { S B I 1 } ( V _ { e s t } ) - V _ { e s t } \cdot T _ { w a r m i n g } \text { for the  } E O A
$$ [¶2025]

$$
d _ { _ { W } } ( V _ { _ { e s t } } ) = d _ { _ { S B I 2 } } ( V _ { _ { e s t } } ) - V _ { _ { e s t } } \cdot T _ { _ { w a r n i n g } } \text { for an EBD based target}
$$ [¶2026]

3.13.9.3.4.2 T_warning is defined as a fixed value (refer to A.3.1). [¶2027]

# 3.13.9.3.5  Permitted speed supervision limit (P) [¶2028]


---
<!-- pagina 156 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2029]

- 3.13.9.3.5.1 In case the calculation of the GUI curve is inhibited, the on-board shall calculate the location  of  the  Permitted  speed  supervision  limit  valid  for  the  estimated  speed, assuming that this latter remains constant during the interval T_driver until the location of  the  SBI1  (for  the  EOA) or the SBI2 (for an EBD based target) supervision limit is reached. [¶2030]

$$
d _ { P } ( V _ { e s t } ) = d _ { S B I 1 } ( V _ { e s t } ) - V _ { e s t } \cdot T _ { d r i v e r }
$$ [¶2031]

$$
d _ { P } ( V _ { e s t } ) = d _ { S B I 2 } ( V _ { e s t } ) - V _ { e s t } \cdot T _ { d r i v e r } \text { for an EBD based target}
$$ [¶2032]

$$
d _ { P } ( V _ { e s t } ) & = d _ { S B I 1 } ( V _ { e s t } ) - V _ { e s t } \cdot T _ { d r i v e r } \text { for the EOA} \\ d _ { P } ( V _ { e s t } ) & = d _ { S B I 2 } ( V _ { e s t } ) - V _ { e s t } \cdot T _ { d r i v e r } \text { for an EBD based target}
$$ [¶2033]

3.13.9.3.5.2 T_driver is defined as a fixed value (refer to A.3.1). [¶2034]

- 3.13.9.3.5.3 Note: The reference for the Permitted speed supervision limit is the SBI supervision limit  and  not  the  Warning  supervision  limit.  As  a  result  the  permitted  and  warning supervision limits are clearly separated and do not affect each other. In this way it is clear that the warning is not part of the critical performance interval. [¶2035]

- 3.13.9.3.5.4 In  case  the  calculation  of  the  Guidance  curve  is  enabled,  the  on-board  shall calculate the location of the Permitted speed supervision limit valid for the estimated speed, as follows: [¶2036]

$$
d _ { P } ( V _ { e s t } ) = \min \left \{ \left ( d _ { S B I 1 } ( V _ { e s t } ) - V _ { e s t } \cdot T _ { d r i v e r } \right ) , d _ { G U I } ( V _ { e s t } ) \right \} \text { for the EOA}
$$ [¶2037]

$$
d _ { P } ( V _ { e s t } ) = \min \left \{ \left ( d _ { S B I 2 } ( V _ { e s t } ) - V _ { e s t } \cdot T _ { d r i v e r } \right ) , d _ { G U I } ( V _ { e s t } ) \right \} \text { for an EBD based target}
$$ [¶2038]

- 3.13.9.3.5.5 In case the calculation of the GUI curve is inhibited, for display purpose only, the P speed related to SBD shall be calculated for the estimated train front end as follows: [¶2039]

$$
5 \text { speed related to SBD shall be calculated for the estimated traffic} \\ V _ { P } ( d _ { \text {estfront} } ) = V _ { S B D } ( d _ { \text {estfront} } + V _ { \text {est} } \cdot ( T _ { d r i v e } + T _ { b s 1 } ) ) \\ E O A \\ V _ { P } ( d _ { \text {estfront} } ) = 0 \text { if } d _ { \text {estfront} } + V _ { \text {est} } \cdot ( T _ { d r i v e } + T _ { b s 1 } ) \geq d _ { E O A } \\ E O A
$$ [¶2040]

- 3.13.9.3.5.6 In case the calculation of the GUI curve is enabled, for display purpose only, the P speed related to SBD shall be calculated for the estimated train front end as follows: [¶2041]

$$
V _ { P } ( d _ { e s t r o f n } ) = \min \left \{ V _ { S B D } ( d _ { e s t r o f n } + V _ { e s t } \cdot ( T _ { d r i v e } + T _ { b s 1 } ) ) , V _ { G U I } ( d _ { e s t r o f n } ) \right \} \\ V _ { P } ( d _ { e s t r o f n } ) = 0 \text { if } d _ { e s t r o f n } + V _ { e s t } \cdot ( T _ { d r i v e } + T _ { b s 1 } ) \geq d _ { E o A } \\
$$ [¶2042]

- 3.13.9.3.5.7 In case the calculation of the GUI curve is inhibited, for display purpose only, the P speed related to EBD, shall be calculated for the max safe front end of the train as follows (see Figure 49): [¶2043]


---
<!-- pagina 157 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2044]

$$
V _ { p } \left ( d _ { \max s a f e r o f n } \right ) & = \\ E B _ { \ } T \arg e t \\ \max \left \{ V _ { E B D } \left ( d _ { \max s a f e r o f n } + V _ { e s t } \cdot ( T _ { d r i v e } + T _ { b s 2 } ) + D _ { b e _ { \max p i l y } } \right ) - ( V _ { d e l t a 0 } + V _ { d e l t a 1 } + V _ { d e l t a 2 } ) \right \} V _ { t \arg e t } \right \} \\ V _ { p } \left ( d _ { \max s a f e r o f n } \right ) - V _ { t \arg e t } & \quad \cdot d _ { \max s a f e r o f n } + V _ { e s t } \cdot ( T _ { d r i v e } + T _ { b s 2 } ) + D _ { b e _ { \max p i l y } } \right \} d _ { E B D } \left ( V _ { t \arg e t } \right ) \\ \text {With } V _ { \ } d e l t a 0 , V _ { \ } d e l t a 1 \text { and } V _ { \ } d e l t a 2 \text { calculated according to } 3 . 1 3 . 9 . 3 . 2 . 1 0 \\ \text {With } D _ { b e _ { \max p i l y } } = ( V _ { e s t } + V _ { e d l t a 0 } + \frac { V _ { d e l t a 1 } } { 2 } ) \cdot T _ { t r a c t i n } + \left ( V _ { e s t } + V _ { d e l t a 0 } + V _ { d e l t a 1 } + \frac { V _ { d e l t a 2 } } { 2 } \right ) \cdot T _ { b e r e m }
$$ [¶2045]

![](images/image_0064.png)

Figure 49: Calculation of Permitted speed displayed to the driver [¶2046]

3.13.9.3.5.7.1 Note:  the  re-use  of  the  same  distance  travelled  and  speed  increase  between  the Permitted speed supervision limit and the EBD, as for the estimated speed (see Figure 49), leads to an overestimation/underestimation of the Permitted speed to be displayed to  the  driver.  This  simplification,  which  avoids  the  need  of  an  iterated  calculation,  is however acceptable and necessary since the error made tends to zero when the train reaches the Permitted speed supervision limit. [¶2047]


---
<!-- pagina 158 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2048]

- 3.13.9.3.5.8 In case the calculation of the GUI curve is enabled, for display purpose only, the P speed related to EBD, shall be calculated for the max safe front end of the train as follows: [¶2049]

$$
V _ { P } \left ( d _ { \max s a f e r f o n } \right ) & = \\ & E B D \, \arg e t \\ \max \left \{ \min \left \{ V _ { E B D } \left ( d _ { \max s a f e r f o n } + V _ { e s t } \cdot ( T _ { d r i v e } + T _ { b s 2 } ) + D _ { b e d l a p s y } \right ) - ( V _ { d e l a 0 } + V _ { d e l a 1 } + V _ { d e l a 2 } ) \right \} \right \} , V _ { t r a g e t } \right \} \\ & \left \{ V _ { G U } \left ( d _ { \max s a f e r f o n } \right ) \\ E B D \, \arg e t
$$ [¶2050]

$$
V _ { P } \left ( d _ { \max s a f e f r o n t } \right ) = V _ { t \arg e t } \text { if } d _ { \max s a f e f r o n t } + V _ { e s t } \cdot ( T _ { d r i v e r } + T _ { b s 2 } ) + D _ { b e _ { d i p l a y } } \geq d _ { E B D } \left ( V _ { t \arg e t } \right ) \\ \ E B D _ { - t \arg e t }
$$ [¶2051]

$$
\text { or if } d _ { \max s a f e f r o n t } \geq d _ { G U I } ( V _ { t \arg e t } )
$$ [¶2052]

With V_delta0, V_delta1 and V_delta2 calculated according to 3.13.9.3.2.10 [¶2053]

$$
W \left ( D _ { b e _ { d i s p a l y } } = ( V _ { e s t } + V _ { d e l t a 0 } + \frac { V _ { d e l t a 1 } } { 2 } ) \cdot T _ { t r a c t i o n } + \left ( V _ { e s t } + V _ { d e l t a 0 } + V _ { d e l t a 1 } + \frac { V _ { d e l t a 2 } } { 2 } \right ) \cdot T _ { b e r e m }
$$ [¶2054]

- 3.13.9.3.5.9 In order to determine the reference location of the target distance displayed to the driver,  in  order  to  check  whether  the  target  is  masking  another  one,  and  in  order  to determine the foot of the GUI curve (only if it is enabled) in case of target different from EOA/SvL,  the  location  of  the  Permitted  speed  supervision  limit,  valid  for  the  target speed, shall be calculated from the EBD, taking into account the following assumptions: [¶2055]

- the estimated acceleration shall be set to 'zero' [¶2056]

- if not inhibited by National Value, the compensation of the inaccuracy of the speed measurement shall be set to a value calculated from the target speed, as defined in SUBSET-041 § 5.3.1.2: V_delta0t = f41(V_target) [¶2057]

3.13.9.3.5.10  To  do  so,  the  same  formulas  defined  above  with  V_est  and  V_delta0  shall  be applied, by substituting V_est with V_target and V_delta0 with V_delta0t. [¶2058]

$$
\Delta \rho \text {pinned} , & \text {by $Substitution} \, V _ { - \Delta } \text {st} \, \text {with} \, V _ { - \Delta } \text {get} \, \text {and} \, V _ { - \Delta } \text {delete} \, \text {with} \, V _ { - \Delta } \text {delta} \, \text {.} \\ d _ { E B I } \left ( V _ { \text {targ} \, e t } \right ) & = d _ { E B D } \left ( V _ { \text {targ} \, e t } + V _ { d \text {delta} \, 0 \, t } \right ) - \left ( V _ { \text {targ} \, e t } + V _ { d \text {delta} \, 0 \, t } \right ) \cdot \left ( T _ { \text {berrem} } + T _ { \text {traction} } \right ) \\ d _ { P } \left ( V _ { \text {targ} \, e t } \right ) & = d _ { E B I } \left ( V _ { \text {targ} \, e t } \right ) - V _ { \text {targ} \, e t } \cdot \left ( T _ { d r i v e r } + T _ { b s \, 2 } \right )
$$ [¶2059]

- 3.13.9.3.5.10.1 Justification:  these assumptions are intended to avoid fluctuations of the target distance displayed to the driver. Moreover the foot of the GUI curve may influence the perturbation location, which  must  be  fully predictable for trackside  engineering reasons. [¶2060]

- 3.13.9.3.5.11  In case a non protected LX start location is supervised as both the EOA and SvL and  the  stopping  in  rear  of  LX  is  not  required,  the  location  of  the  most  restrictive [¶2061]


---
<!-- pagina 159 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2062]

Permitted  speed  supervision  limit,  valid  for  the  LX  speed  shall  be  used  in  order  to determine the location where the supervision of the LX start location is substituted by the supervision of the LX speed (see section 5.16.3). [¶2063]

3.13.9.3.5.12  To  calculate  this  location,  the  same  formulas  defined  above  with  V_est  shall  be applied by substituting V_est with V_LX. [¶2064]

$$
a p p i m e b y \, & \text {substituting } v _ { - } e s t \text { with } v _ { - } L \\ d _ { S B I 1 } ( V _ { L X } ) = d _ { S B D } ( V _ { L X } ) - V _ { L X } \cdot T _ { b s 1 } \\ d _ { S B I 2 } ( V _ { L X } ) = d _ { E B I } ( V _ { L X } ) - V _ { L X } \cdot T _ { b s 2 } \\ \text {With}
$$ [¶2065]

$$
d _ { E B } \left ( V _ { L X } \right ) & = d _ { E B D } \left ( V _ { L X } + V _ { d e l t a } + V _ { d e l t a } + V _ { d e l t a } \right ) - \left ( V _ { L X } + V _ { d e l t a } \right ) + \frac { V _ { d e l t a } } { 2 } \right ) \cdot T _ { \text {traction} } \\ & - \left ( V _ { L X } + V _ { d e l t a } + V _ { d e l t a } + \frac { V _ { d e l t a } } { 2 } \right ) \cdot T _ { \text {berem} } \\ & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
$$ [¶2066]

And with V_delta0, V_delta1 and V_delta2 calculated according to 3.13.9.3.2.10 [¶2067]

In case the GUI curve is inhibited: [¶2068]

$$
d _ { _ { P } } ( V _ { _ { L X } } ) = d _ { _ { S B 1 } } ( V _ { _ { L X } } ) - V _ { _ { L X } } \cdot T _ { _ { d i r v e r } } \text { if } d _ { _ { S B 1 } } ( V _ { _ { L X } } ) - d _ { _ { S B 1 } } ( V _ { _ { L X } } ) \geq d _ { _ { \max s a f e f o r t } } - d _ { _ { e s f r o n t } }
$$ [¶2069]

$$
O r \ d _ { P } ( V _ { L X } ) = d _ { S B I 2 } ( V _ { L X } ) - V _ { L X } \cdot T _ { d r i v e r } \text { if } d _ { S B I 2 } ( V _ { L X } ) - d _ { S B I 1 } ( V _ { L X } ) < d _ { \max s a f e f o r t } - d _ { e s f o r t }
$$ [¶2070]

In case the GUI curve is enabled: [¶2071]

$$
d _ { P } ( V _ { L X } ) = \min \left \{ \left ( d _ { S B I 1 } ( V _ { L X } ) - V _ { L X } \cdot T _ { d r i v e r } \right ) , d _ { G U I } ( V _ { L X } ) \right \} _ { \text {if} }
$$ [¶2072]

$$
d _ { P } ( V _ { L X } ) = \min \left \{ \left ( d _ { S B I 1 } ( V _ { L X } ) - V _ { L X } \cdot T _ { d r i v e r } \right ) , d _ { G U I } ( V _ { L X } ) \right \} _ { \text {if} } \\ d _ { S B I 2 } ( V _ { L X } ) - d _ { S B I 1 } ( V _ { L X } ) \geq d _ { \max s a f e f r o n t } - d _ { e s t f r o n t } \\ \\ \text {or} \quad d _ { P } ( V _ { L X } ) = \min \left \{ \left ( d _ { S B I 2 } ( V _ { L X } ) - V _ { L X } \cdot T _ { d r i v e r } \right ) , d _ { G U } ( V _ { L X } ) \right \} _ { \text {if} } \\ d _ { S B I 2 } ( V _ { L X } ) - d _ { S B I 1 } ( V _ { L X } ) < d _ { \max s a f e f r o n t } - d _ { e s t f r o n t }
$$ [¶2073]

3.13.9.3.5.12.1 Note: the use of the instantaneous speed under reading amount and acceleration in the calculation of this location avoids a jump of display when the substitution takes place. [¶2074]

# 3.13.9.3.6  Indication supervision limit (I) [¶2075]

- 3.13.9.3.6.1 The on-board shall calculate the location of the Indication supervision limit valid for the  estimated  speed,  assuming  that  this  latter  remains  constant  during  the  interval T_indication until the location of the Permitted speed supervision limit is reached. [¶2076]

$$
d _ { I } ( V _ { e s t } ) = d _ { P } ( V _ { e s t } ) - V _ { e s t } \cdot T _ { i n d i c a t i o n }
$$ [¶2077]


---
<!-- pagina 160 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2078]

- 3.13.9.3.6.2 If  the  service  brake  feedback  interface  is  not  available  for  use,  then  T_indication shall be calculated as follows: [¶2079]

$$
T _ { i n d i c a t i o n } = \max \left \{ ( 0 . 8 \cdot T _ { b s } ) , 5 s \right \} + T _ { d r i v e r }
$$ [¶2080]

- 3.13.9.3.6.3 Note: The reduction of T_indication by a factor is intended to improve performance and the feasibility of this reduction is based on experience with real implementations. To avoid very low values when T_bs is small, a minimum is defined for T_indication, giving the driver always enough time to operate the brake. [¶2081]

- 3.13.9.3.6.4 If the service brake feedback interface is available for use then T_indication shall be equal to 5s + T_driver. [¶2082]

# 3.13.9.4 Release speed supervision limits [¶2083]

- 3.13.9.4.1  The release speed is a special ceiling speed limit, applicable in the vicinity of the EOA. The  EBI  supervision  limit  is  equal  to  the  release  speed.  There  is  no  SBI,  W,  P,  I supervision limit associated to the release speed. [¶2084]

- 3.13.9.4.2  Note: The release speed may be necessary for two reasons. One is that a train has to be able to approach the EOA where the permitted speed reaches zero and might be too restrictive to permit acceptable driving due to inaccuracy of the measured distance. The other reason is that in a level 1 application the train has to be able to overpass the balise  when the signal  clears.  For  these  two  reasons a (low) release speed may be given from trackside or may be calculated on board, based on the distance from the EOA to the Supervised Location. [¶2085]

- 3.13.9.4.3  With each MA, it shall be possible for the trackside to: [¶2086]

- Give the value of the release speed directly to the on-board, OR [¶2087]

- Instruct the on-board to calculate the release speed, OR [¶2088]

-  Instruct the on-board to use the national value. [¶2089]

- 3.13.9.4.4  In case the MA does not identify the variant to be used or in case of LOA, no release speed shall be supervised. [¶2090]

- 3.13.9.4.5  Note:  When  the  release  speed  is  given  as  a  fixed  value  from  trackside,  the ERTMS/ETCS  system  cannot  be  responsible  for  stopping  the  train  in  rear  of  the Supervised  Location.  In  this  case,  it  is  the  full  responsibility  of  the  infrastructure manager to set the appropriate release speed with regard to the risk of passing the Supervised Location. [¶2091]

- 3.13.9.4.6  The start location of the release speed monitoring (i.e. where the EBI supervision limit related  to  EBD  is  replaced  with  an  EBI  supervision  limit  equal  to  the  release  speed value) shall be the location of the most restrictive SBI supervision limit among the SBI1 related to EOA, the SBI2 related to SvL and, when the Release Speed is calculated on-board, the SBI2 supervision limit(s) related to other target(s), if any, between the [¶2092]


---
<!-- pagina 161 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2093]

Trip location related to the EOA and the SvL, calculated for the Release Speed value, taking into account the following assumptions: [¶2094]

- the estimated acceleration shall be set to 'zero' [¶2095]

- if not inhibited by National Value, the compensation of the inaccuracy of the speed measurement shall be set to a value calculated from the release speed, as defined in SUBSET-041 § 5.3.1.2: V_delta0rs = f41(V_release) [¶2096]

3.13.9.4.7  To do so, the same formulas defined above with V_est and V_delta0 shall be applied, by substituting V_est with V_release and V_delta0 with V_delta0rs. [¶2097]

$$
d _ { s B I 1 } ( V _ { r e l e a s e } ) = d _ { s B D } ( V _ { r e l e a s e } ) - V _ { r e l e a s e } \cdot T _ { b s 1 }
$$ [¶2098]

$$
\text {with } \, d _ { E B I } \left ( V _ { r e l e a s e } \right ) = d _ { E B D } \left ( V _ { r e l e a s e } + V _ { d e l a t 0 r s } \right ) - \left ( V _ { r e l e a s e } + V _ { d e l a t 0 r s } \right ) \cdot \left ( T _ { b e r e m } + T _ { t r a c t i o n } \right ) \\ \quad T \arg e t _ { - n } \left ( V _ { \arg e t _ { - n } } \right )
$$ [¶2099]

$$
d _ { S B 1 } ( V _ { \text {release} } ) & = d _ { S B D } ( V _ { \text {release} } ) - V _ { \text {release} } \cdot T _ { b s 1 } \\ d _ { S B 1 2 } ( V _ { \text {release} } ) & = d _ { E B 1 } \left ( V _ { \text {release} } \right ) - V _ { \text {release} } \cdot T _ { b s 2 } \\ T \arg e t _ { n } & = \begin{array} { c c } T \arg e t _ { n } \end{array} \\ \intertext { w i t h d _ { E B 1 } ( V _ { \text {release} } ) = d _ { E B D } \left ( V _ { \text {release} } + V _ { \delta t a r 0 s } \right ) - ( V _ { \text {release} } + V _ { \delta t a r 0 s } ) \cdot ( T _ { b e r e m } + T _ { t r a c i t } ) } \intertext { w i t h d _ { E B 1 } ( V _ { \text {release} } ) = d _ { E B D } \left ( V _ { \text {release} } + V _ { \delta t a r 0 s } \right ) - ( V _ { \text {release} } + V _ { \delta t a r 0 s } ) \cdot ( T _ { b e r e m } + T _ { t r a c i t } ) }
$$ [¶2100]

with Target_n being any EBD based target between the Trip location related to the EOA and the SvL(included) [¶2101]

$$
d _ { S B I 2 } ( V _ { r e l e a s e } ) = \min \left \{ d _ { S B I 2 } \left ( V _ { r e l e a s e } \right ) , \dots , d _ { S B I 2 } \left ( V _ { r e l e a s e } \right ) \right \}
$$ [¶2102]

with MREBDT = Most Restrictive Target amongst the EBD based targets between the Trip location related to the EOA and the SvL (included) [¶2103]

$$
d _ { \underset { \ R S M } { s t a r t } } = d _ { \ S B 1 } ( V _ { r e l a s e } ) \text { if } d _ { \ S B 1 } ( V _ { r e l a s e } ) - d _ { \ S B 1 } ( V _ { r e l a s e } ) \geq d _ { \max s a f e r f o n t } - d _ { \ e s t f r o n t }
$$ [¶2104]

$$
\text {Or} \, d _ { \ s u r t } = d _ { \ S B I 2 } \left ( V _ { r e l a s e } \right ) \text { if } d _ { \ S B I 2 } \left ( V _ { r e l a s e } \right ) - d _ { \ S B I 1 } \left ( V _ { r e l a s e } \right ) < d _ { \max s a f r o n t } - d _ { \ e s t r o n t } \\
$$ [¶2105]

$$
\ s e \Big ( \text {if } d _ { S B I 2 } ( V _ { \text {release} } ) - d _ { S B I 1 } ( V _ { \text {release} } ) \geq d _ { \max s a f e f r o n t } - d _ { \text {estfront} } \\ \intertext { s e } \text {release} \Big ) \text { if } d _ { S B I 2 } ( V _ { \text {release} } ) - d _ { S B I 1 } ( V _ { \text {release} } ) < d _ { \max s a f e f r o n t } - d _ { \text {estfront} } \\ \text {DT}
$$ [¶2106]


---
<!-- pagina 162 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2107]

![](images/image_0065.png)

Figure 50: Start location of Release Speed Monitoring [¶2108]

- 3.13.9.4.8  When the Release Speed is calculated on-board (Figure 51 box 3), its value shall be equal to the most restrictive value, at the Trip location related to the EOA, amongst the EBI  supervision  limit  related  to  the  SvL  (Figure  51  box  1)  and,  if  any,  the  EBI supervision limits(s) related to other target(s) between the Trip location related to the EOA and the SvL (Figure 51 box 2). [¶2109]

![](images/image_0066.png)

Figure 51: Calculated Release Speed based on speed restriction between EOA and SvL [¶2110]


---
<!-- pagina 163 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2111]

- 3.13.9.4.8.1 In order to calculate in advance the EBI supervision limit at the Trip location related to the EOA, the on-board equipment shall take into account an estimated acceleration set to 'zero'. [¶2112]

3.13.9.4.8.2 The on-board equipment shall seek for each target referred to in clause 3.13.9.4.8, a release speed value which satisfies the two following inequalities: [¶2113]

$$
3 . 1 3 . 9 . 4 . 8 . & \quad \text {the on-board equipment shall seek for each target referred to in clause 3.13.9.4 . 8 ,} \\ & \quad a r e l a s e e s p e d v e l u s t i s f a t i s t h e t w o w i n c u l i e q u a l i t i e s . \\ \ A B S \left \{ V _ { r e l a s e } - \left ( V _ { E B D } \left ( d _ { r i p t E o A } + D _ { b e c } \right ) - V _ { d e l a t o r s o b } \right ) \right \} \leq 1 k m / \, h \\ d _ { r i p t E o A } + D _ { b e c } \leq d _ { E B D } \left ( V _ { t a r g e t } \right ) & \\ & \quad w i t h \ V _ { d e l a t o r s o b } = \max \left \{ f _ { 4 1 } ( V _ { r e l a s e } ) , V _ { u r a } \right \} \, or \, V _ { d e l a t o r s o b } = 0 \, \text {if compensation of speed} \\ \text {inaccuracy is inhibited by National Value} \\ & \quad w i t h \ D _ { b e c } = \left ( V _ { r e l a s e } + V _ { d e l a t o r s o b } \right ) \cdot ( T _ { t r a c t i o n } + T _ { b e r e m } ) \\ & \quad w i t h \\ & \quad d _ { r i p t E o A } = d _ { E o A } + \alpha \cdot L _ { a n t e n a - f r o n t } \\ & \quad + \max \left \{ 2 \cdot Q _ { l o c a c _ { - r e f B G } } + 1 0 m + 1 0 \% \cdot d _ { E o A } \right \} \left ( d _ { \max s a f e r o n t } - d _ { \min s a f e r o n t } \right ) \right \} \\ & \quad \text {and with $\alpha=1$ if level=1} \\ & \quad \alpha = 0 \, \text {if level=2 or 3} \\ \text {if no speed value higher than $\ V _ { t } $target fulfills the above inequa l i ties, then} \\ V _ { r e l a s e } = V _ { t a r g e t }
$$ [¶2114]

If no speed value higher than V_target fulfils the above inequalities, then: [¶2115]

$$
V _ { r e l e a s e } = V _ { t \arg e t }
$$ [¶2116]

3.13.9.4.8.2.1 Note:  The  above  formulas  are  intended  to  prevent  the  calculated  release  speed from fluctuating, according to the distance, speed and acceleration measurements. It allows  calculating  the  release  speed  only  once,  for  a  given  on-board  reference location, unless [¶2117]

-  the distance confidence interval exceeds a predicted one, which is based on the  assumption  that  the  whole  distance  between  the  current  on-board reference  location  and  the  EOA  would  be  travelled  with  SUBSET-041 odometer  performance  values  and  without  any  update  of  the  on-board reference location, or [¶2118]

-  the speed under reading amount (V_ura) exceeds the  SUBSET-041 performance value [¶2119]

Whenever the on-board reference location is updated (e.g. new LRBG), the release speed  will  however  be  recalculated  and  will  increase  with  a  step.  This  behaviour  is acceptable from an operational point of view. [¶2120]


---
<!-- pagina 164 -->

- 3.13.9.4.8.2.2 Note: The method chosen (e.g. iterative algorithm) to compute the release speed is an implementation issue. [¶2121]

- 3.13.9.4.9  If the release speed (Figure 52 box 1 gives an example when it is calculated on-board) exceeds the MRSP anywhere in the area (Figure 52 box 2) delimited on one side by the presumed start location of the Release speed monitoring and on the other side by the trip location related to the EOA, the on-board shall use as a fixed release speed (Figure 52 box 4) the most restrictive value of the MRSP (Figure 52 box 3) within this area,  and  shall  re-evaluate  the  start  location  of  the  Release  speed  monitoring accordingly. [¶2122]

![](images/image_0067.png)

Figure 52: Release Speed limited by MRSP [¶2123]

# 3.13.9.5 Intentionally deleted

# 3.13.10 Speed and distance monitoring commands [¶2124]

# 3.13.10.1 Introduction [¶2125]

- 3.13.10.1.1  By comparing the train speed and position to the various supervision limits defined in the previous section, the on-board equipment generates braking commands, traction cut-off commands and relevant information to the driver. The information displayed to the driver is selected according to the following supervision statuses of the speed and distance  monitoring  function:  Normal  status,  Indication  status,  Overspeed  status, Warning status and Intervention status. [¶2126]

- 3.13.10.1.2  The following types of speed and distance monitoring are defined: [¶2127]

-  Ceiling speed monitoring (CSM) [¶2128]

-  Target speed monitoring (TSM) [¶2129]


---
<!-- pagina 165 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2130]

-  Release speed monitoring (RSM) [¶2131]

- 3.13.10.1.3  Ceiling speed monitoring is the speed supervision in the area where the train can run without the need to brake to a target. [¶2132]

- 3.13.10.1.4  Target speed monitoring is the speed and distance supervision in the area where the specific information related to a target is displayed to the driver and within which the train brakes to a target. [¶2133]

- 3.13.10.1.5  Release speed monitoring is the speed and distance supervision in the area close to the EOA where the train is allowed to run with release speed to approach the EOA. [¶2134]

![](images/image_0068.png)

Figure 53: Different types of speed and distance monitoring [¶2135]

# 3.13.10.2 General requirements [¶2136]

- 3.13.10.2.1  The  train  speed  indicated  to  the  driver  shall  be  identical  to  the  speed  used  for  the speed monitoring. This shall be the estimated speed. [¶2137]

- 3.13.10.2.2  Once a Train Interface command (traction cut-off, service brake or emergency brake) is  triggered, the on-board shall apply it until its corresponding revocation condition is met. [¶2138]

- 3.13.10.2.3  If there is no on-board interface with the service brake or if the use of the service brake command  is  not  allowed  by  a  National  Value  (only  in  Target  speed  monitoring), whenever a service brake command is specified, the emergency brake command shall be triggered instead. [¶2139]

- 3.13.10.2.4  The  emergency  brake  command,  which  is  triggered  instead  of  the  service  brake command when an SBI supervision limit is exceeded, shall be revoked according to the  requirements  specified  for  the  revocation  of  service  brake  command,  unless  the [¶2140]


---
<!-- pagina 166 -->

emergency brake command has been also triggered due to an EBI supervision limit. In such  case,  the  condition  for  revoking  the  emergency  brake  command  due  to  EBI supervision limit shall prevail. [¶2141]

- 3.13.10.2.5  The  on-board  shall  revoke  the  Intervention  status  only  when  no  brake  command  is applied by the speed and distance monitoring function. [¶2142]

- 3.13.10.2.6  In  level  2/3:  Train  trip  shall  be  initiated  if  the  on-board  equipment  detects  that  the minimum safe front end has passed the EOA/LOA location. [¶2143]

- 3.13.10.2.7  In  Level  1:  Train  Trip  shall  be  initiated  if  the  on-board  equipment  detects  that  the minimum  safe  antenna  position  (calculated  by  subtracting  distance  between  active Eurobalise antenna and the front end of the train from the min safe front end position) has passed the EOA/LOA location. [¶2144]

- 3.13.10.2.8  In  the  following  sections,  the  term  V_MRSP  (together  with  the  derived  ceiling supervision limits) refers to the lowest MRSP element encountered between the min safe front end and the max safe front end of the train. [¶2145]

# 3.13.10.3 Requirements for Ceiling speed monitoring [¶2146]

- 3.13.10.3.1  The on-board equipment shall display the Permitted speed ceiling supervision limit. [¶2147]

- 3.13.10.3.2  When  the  supervision  status  is  Overspeed,  Warning  or  Intervention,  the  on-board equipment shall display the SBI speed ceiling supervision limit. [¶2148]

- 3.13.10.3.3  The  on-board  shall  compare  the  estimated  speed  with  the  ceiling  supervision  limits defined  in  section  3.13.9.2  and  shall  trigger/revoke  commands  to  the  train  interface (service  brake  if  implemented  or  emergency  brake)  and  supervision  statuses  as described in Table 5 and Table 6. [¶2149]

[¶2150]
| Triggering condition #   | Estimated speed                        | Location   | TI Command triggered   | Supervision status triggered   |
|--------------------------|----------------------------------------|------------|------------------------|--------------------------------|
| t1                       | MRSP est V V                          | Any        | -                      | Normal Status                  |
| t2                       | MRSP est V V                          | Any        | -                      | Overspeed Status               |
| t3                       | ) ( MRSP warning MRSP est V dV V V   | Any        | -                      | Warning Status                 |
| t4                       | ) ( MRSP sbi MRSP est V dV V V       | Any        | SB                     | Intervention Status            |
| t5                       | ) ( MRSP ebi MRSP est V dV V V       | Any        | EB                     | Intervention Status            |

Table 5: triggering of Train Interface commands and supervision statuses in ceiling speed monitoring [¶2151]


---
<!-- pagina 167 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2152]

[¶2153]
| Revocation condition #   | Estimated speed   | Location   | TI Command revoked                        | Supervision status revoked                                                                                                       |
|--------------------------|-------------------|------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| r0                       | Standstill        |            | EB                                        | Intervention Status                                                                                                              |
| r1                       | MRSP est V V     | Any        | SB EB (only if allowed by National Value) | Indication Status Overspeed Status Warning Status Intervention Status (in case of EB command, only if allowed by National Value) |

Table 6: Revocation of Train Interface commands and supervision statuses in ceiling speed monitoring [¶2154]

3.13.10.3.4  The on-board equipment shall execute the transitions between the different supervision statuses as described in Table 7 (see section 4.6.1 for details about the symbols).  This  table  takes  into  account  the  order  of  precedence  between  the supervision  statuses  and  the  possible  updates  of  the  MRSP  while  in  ceiling  speed monitoring (e.g. when a TSR is revoked). [¶2155]

[¶2156]
| Normal status   | < r1 -p1-         | < r1 -p1-        | < r1 -p1-      | < r0, r1 -p1-       |
|-----------------|-------------------|------------------|----------------|---------------------|
|                 | Indication status |                  |                |                     |
| t2 > -p3-       | t2 > -p3-         | Overspeed status |                |                     |
| t3 > -p2-       | t3 > -p2-         | t3 > -p2         | Warning status |                     |
| t4, t5 > -p1-   | t4, t5 > -p1-     | t4, t5 > -p1-    | t4, t5 > -p1-  | Intervention status |

Table 7: Transitions between supervision statuses in ceiling speed monitoring [¶2157]

- 3.13.10.3.5  When  the  speed  and  distance  monitoring  function  becomes  active  and  the  ceiling speed monitoring is the first one entered, the triggering condition t1 defined in Table 5 shall be checked in order to determine whether the Normal status applies. If it is not [¶2158]


---
<!-- pagina 168 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2159]

- the  case,  the  on-board  shall  immediately  set  the  supervision  status  to  the  relevant value, applying a transition from the Normal status according to Table 7. [¶2160]

- 3.13.10.3.6  The  Indication  status  is  not  used  in  ceiling  speed  monitoring.  However,  in  case  the ceiling  speed  monitoring  is  entered  and  the  supervision status was previously set to Indication,  the  on-board  equipment  shall  immediately  execute  one  of  the  transitions from the Indication status, as described in Table 7. [¶2161]

- 3.13.10.3.7  In  ceiling  speed  monitoring,  only  the  ceiling  supervision  limits  (described  in  section 3.13.9.2)  are  used  to  determine  the  commands  to  the  Train  Interface  and  the supervision statuses displayed to the driver. However the braking to target supervision limits  and  the  release  speed  supervision  limits  (described  in  sections  3.13.9.3  and 3.13.9.4) are also used to determine the locations where the transition to target speed monitoring and to release speed monitoring occur respectively. [¶2162]

- 3.13.10.3.8  The on-board equipment shall display to the driver the first Indication location that will be reached by either the max safe or by the estimated train front end. To that effect, the  on-board  shall  compute  the  remaining  distance  to  the  first  Indication  location  as follows: [¶2163]

$$
\| V _ { e s t } \| < V _ { r e l e a s e }
$$ [¶2164]

$$
\text {Ind distance} = d _ { \underset { R S M } { \text {start} } } - d _ { \underset { \text {effort} } { \text {est} } \text {front} } \text { in case } d _ { \underset { R S M } { \text {start} } } = d _ { S B 1 } ( V _ { r e l a s e } )
$$ [¶2165]

$$
\text {Ind distance} = \, d _ { \underset { R S M } { s t a r t } } - d _ { \max s a f e f r o n t } \text { in case } \, d _ { \underset { R S M } { s t a r t } } = d _ { S B 1 } ( V _ { r e l a s e } )
$$ [¶2166]

$$
\text {with} \, d _ { \stackrel { s t a r t } { R S M } } \text {and} \, d _ { \stackrel { S B I 2 } { M R E B D T } } ( V _ { r e l e a s e } ) \, \text {as defined in } 3 . 1 3 . 9 . 4 . 7
$$ [¶2167]

$$
\| f \| V _ { e s t } \geq V _ { r e l e a s e }
$$ [¶2168]

Ind distance = [¶2169]

$$
\min \text {distance} \equiv & \\ \min \begin{cases} ( d _ { 1 } ( V _ { e s t } ) - d _ { e s t f r o n t } ) , ( d _ { 1 } ( V _ { e s t } ) - d _ { \max s a f e r f o n } ) , ( d _ { 1 } ( V _ { e s t } ) - d _ { \max s a f e r f o n } ) \\ \ E O A & \text {SvL} \\ & \text {Targ et al.} \end{cases} \\ \min \begin{cases} ( , \dots , ( d _ { 1 } ( V _ { e s t } ) - d _ { \max s a f e r f o n } ) \\ T \arg e t _ { n } \end{cases}
$$ [¶2170]

With Target_1, ..., Target_n being EBD based targets whose speed value is below or equal to the estimated speed [¶2171]

- 3.13.10.3.8.1  In  case  no  release  speed  is  supervised,  the  same  formulas  shall  be  applied,  by substituting V_release with the value 0. [¶2172]

- 3.13.10.3.8.2  Exception: In case the list of supervised targets is empty or in case of LOA with no EBD based target whose speed value is below or equal to the estimated speed, the [¶2173]


---
<!-- pagina 169 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2174]

ERTMS/ETCS  on-board  equipment  shall  not  display  any  first  Indication  location information. [¶2175]

- 3.13.10.3.9  If A_MAXREDADH (see 3.13.6.2.1.6) requests the target information as supplementary DMI information, the on-board equipment shall display to the driver the target information (target speed and distance to target) related to one target at a time: the  Most  Relevant  Displayed  Target  (MRDT).  The  MRDT shall be selected amongst the supervised  targets  as  the  one  whose  remaining  distance  to its Indication supervision  limit  (as  specified  in  3.13.10.3.8  and  3.13.10.3.8.1)  is  the  shortest.  The indicated distance to the target shall be computed in the same way as for target speed monitoring, i.e. clauses 3.13.10.4.7, 3.13.10.4.8 and 3.13.10.4.8.1 shall apply. [¶2176]

- 3.13.10.3.9.1  Exception: In case the list of supervised targets is empty or in case of LOA with no EBD based target whose speed value is below or equal to the estimated speed, the ERTMS/ETCS on-board equipment shall not display any target information. [¶2177]

- 3.13.10.3.10 If A_MAXREDADH  (see  3.13.6.2.1.6) requests a time to Indication as supplementary  DMI  information,  the  on-board  equipment  shall  compute  the  Time  to Indication (TTI) as the time to travel at the estimated speed the remaining distance to the  first  Indication  location  (as  specified  in  3.13.10.3.8  and  3.13.10.3.8.1).  The  onboard  equipment  shall  inform  the  driver  as  long  as  this  time  is  shorter  than  a  fixed value (refer to A.3.1). [¶2178]

- 3.13.10.3.10.1  Exception: In case the list of supervised targets is empty or in case of LOA with no EBD based target whose speed value is below or equal to the estimated speed, the ERTMS/ETCS on-board equipment shall not compute any time to Indication. [¶2179]

# 3.13.10.4 Requirements for Target speed monitoring [¶2180]

- 3.13.10.4.1  In target speed monitoring, both the ceiling supervision limits and the braking to target supervision limits, described in sections 3.13.9.2 and 3.13.9.3, are used to determine the  commands  to  the  Train  Interface  and  the  supervision  statuses  displayed  to  the driver. [¶2181]

- 3.13.10.4.2  The on-board equipment shall display to the driver the target information (target speed and distance to target)  related  to  one  target  at  a  time:  the  Most  Relevant  Displayed Target (MRDT). The MRDT shall be selected amongst the supervised targets whose Indication supervision limit is exceeded (i.e. a condition to trigger a supervision status with respect to these targets is met, see table 8 and table 9) and shall be determined according to the following steps: [¶2182]

-  Step  0:  MRDT0  =  the  target  of  which  the  braking  to  target  Permitted  speed supervision limit (refer to section 3.13.9.3.5), calculated for the current position of the train, is the lowest one amongst the concerned targets: [¶2183]

$$
V _ { P } = \min \left \{ V _ { P } ( d _ { e s t f o r n } ) , V _ { P } ( d _ { \max s a f e f o r n } ) , V _ { P } ( d _ { \max s a f e f o r n } ) , \dots , V _ { P } ( d _ { \max s a f e f o r n } ) \right \} \\ M R D T _ { 0 }
$$ [¶2184]


---
<!-- pagina 170 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2185]

$$
with V _ { p } ( d _ { \ e s t r o f } ) \tan k e t { \intertext { with $V_{p} (d_{\ e s t r o f})$ taken into account only if $d_{\ e s t r o f} > d_{1}(V_{\ e s t r o f})$} \\ E O A \\ \intertext { with $V_{p} (d_{\max safeffront})$ taken into account only if $d_{\max safeffront} > d_{1}(V_{\ e s t r o f})$} \\ S v _ { L } \\ \intertext { with $V_{p} (d_{\max safeffront})$ taken into account only if $d_{\max safeffront} > d_{1}(V_{\ e s t r o f})$ and $V_{\ e s t } \geq V _ { T \arg e _ { 1 } } $ } \\ T \arg e _ { 1 }
$$ [¶2186]

$$
\text {with } V _ { P } ( d _ { \max s a f f o r n } ) \text { taken into account only if } d _ { \max s a f f o r n } > d _ { \max s a f f o r n } ( V _ { _ { e s t } } ) \text { and } V _ { e s t } \geq V _ { T \arg e _ { - 1 } }
$$ [¶2187]

... [¶2188]

$$
\text {with } V _ { P } ( d _ { \max s a f f o r f } ) \text { taken into account only if } d _ { \max s a f f o r f } > \sup _ { T \arg e t _ { n } } ( V _ { e s t } ) \text { and } V _ { e s t } \geq V _ { T \arg e t _ { n } }
$$ [¶2189]

-  Step 1: the on-board equipment shall check whether the MRDT obtained from the previous step (MRDT0) masks any other target(s) remaining in the list of concerned targets, whose target speed is lower than MRDT0. A target is masked by MRDT0 if its  Indication  supervision  limit  is  located  in  rear  of  the  location  of  the  MRDT0 Permitted  speed  supervision  limit,  both  at  the  target  speed  of  MRDT0.  It  shall  be identified using one of the following formulas, where both the Indication supervision limit  and  the  Permitted  speed  supervision  limit  are  calculated  using  the  same formulas defined above and by substituting V_est with V_target_MRDT0: [¶2190]

$$
\begin{smallmatrix} d _ { I } \left ( V _ { \ t \arg e t } \right ) < d _ { P } \left ( V _ { \ t \arg e t } \right ) & d _ { I } \left ( V _ { \ t \arg e t } \right ) < d _ { P } \left ( V _ { \ t \arg e t } \right ) \\ E O A \quad _ { M R D T _ { 0 } } & \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { }
$$ [¶2191]

$$
\begin{smallmatrix} d _ { I } & ( V _ { t \arg e t } ) < d _ { P } \left ( V _ { t \arg e t } \right ) \\ T \arg e t _ { - 1 } & M R D T _ { 0 } ^ { \dag } \left ( M R D T _ { 0 } \right ) ^ { \dag } M R D T _ { 0 } \right ) \text { or } \dots \text { or } T \arg e t _ { - n } \left ( M R D T _ { 0 } \right ) ^ { \dag } M R D T _ { 0 } \right )
$$ [¶2192]

If at least one target is masked by MRDT0, then the MRDT obtained from this step (MRDT1) shall be the masked target with its Indication supervision limit the furthest in rear of the location of the MRDT0 Permitted speed supervision limit and the onboard equipment shall go to the next step. [¶2193]

If  none  of  the  remaining  targets  from  the  list  of  concerned  targets  is  masked  by MRDT0 or  if  there  is  no  other  remaining  target  to  check  in  the  list  of  concerned targets,  then  the  MRDT  shall  be  the  target  obtained  from  the  previous  step  (i.e. MRDT0). [¶2194]

... [¶2195]

-  Step n: the on-board shall apply step n-1, substituting MRDTn-2 with MRDTn-1 and checking  the  list  of  concerned  targets  excluding  the  targets  which  have  been preselected  as  MRDT  in  all  the  previous  steps  (i.e.  from  MRDT0  to  MRDTn-1 inclusive). [¶2196]

- 3.13.10.4.2.1  Note  1:  the  above  process  for  the  determination  of  the  MRDT  ensures  that  in  all circumstances (especially when several targets are close to each other) it is avoided that a target is displayed after its Indication supervision limit has been reached. [¶2197]


---
<!-- pagina 171 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2198]

- 3.13.10.4.2.2  Note  2:  when entering target speed monitoring,  there is by definition at least one target  that  satisfies  the  conditions  to  be  selected  as  MRDT.  Afterwards  (e.g.  due  to train  braking)  it  is  possible  that  no  target  satisfies  any  more  the  conditions  to  be selected  as  MRDT,  which  however  only  means  that  the  target  previously  selected remains the MRDT (see clause 3.13.10.4.5). [¶2199]

- 3.13.10.4.2.3  Note  3:  if  MRDTn-1  is  a  target  at  zero  speed  (e.g.  EOA  or  SvL),  then  it  is  always selected as MRDT, i.e. no other target can be selected as MRDT as per step n. [¶2200]

- 3.13.10.4.3  The  on-board  equipment  shall  display  the  Permitted  speed,  according  to  following formula: [¶2201]

$$
V _ { P } = \min \left \{ V _ { P } ( d _ { \ e s f r o n t } ) , V _ { P } ( d _ { \max s a f e r o n t } ) , V _ { P } ( d _ { \max s a f e r o n t } ) , \dots , V _ { P } ( d _ { \max s a f e r o n t } ) , V _ { M R S P } \right \} \\ D M = \left \{ V _ { P } ( \ e O A ) \, \substack { S v L } \\ \, T \arg e t _ { - 1 } \right \}
$$ [¶2202]

With Target_1, ..., Target_n being all the targets from the list of supervised targets [¶2203]

- 3.13.10.4.4  When  the  supervision  status  is  Overspeed,  Warning  or  Intervention,  the  on-board equipment shall display the SBI speed, according to the following formula: [¶2204]

$$
V _ { S B I } = \min \left \{ \max \left \{ V _ { S B I } ( d _ { e s t f r o n } ) , V _ { r e a l e s e } \right \} , \max \left \{ V _ { S B I } ( d _ { \max s a f e r f o n } ) , V _ { r e a l e s e } \right \} , \right \} , \\ D M I \quad \left \{ V _ { S B I D } ( d _ { \max s a f e r f o n } ) , \dots , V _ { S B I D } ( d _ { \max s a f e r f o n } ) , V _ { M R S P } + d V _ { s b i } ( V _ { M R S P } ) \right \} \\
$$ [¶2205]

- 3.13.10.4.5  Once a target is the MRDT, it shall remain the MRDT until it is removed from the list of supervised targets or until it is replaced as MRDT with another target which is selected for the first time according to clause 3.13.10.4.2. The driver shall be informed upon any change of MRDT. [¶2206]

- 3.13.10.4.6  If  the  MRDT is either the EOA or the SvL, the on-board equipment shall display the release speed, if given by the trackside or calculated on-board. [¶2207]

- 3.13.10.4.7  If the MRDT is neither the EOA nor the SvL, the indicated distance to the target shall be the distance between the maximum safe front end and the location of the Permitted speed supervision limit calculated for the target speed (see section 3.13.9.3.5 for the calculation of this location), but limited to zero after this location is passed. [¶2208]

$$
\Target \, \text {distance} = \max \left \{ ( d _ { P } ( V _ { t \arg e t } ) - d _ { \max \, s a f f o r n t } ) , 0 \right \}
$$ [¶2209]

3.13.10.4.7.1  Intentionally deleted. [¶2210]

- 3.13.10.4.8  If the MRDT is either the EOA or the SvL, the indicated distance to the target shall be calculated as follows: [¶2211]

$$
\Target \, \text {distance} = \max \left \{ \min \left \{ \left ( d _ { E O A } - d _ { e s t f r o n t } \right ) \left ( d _ { S v L } - d _ { \max s a f e f r o n t } \right ) \right \} , 0 \right \}
$$ [¶2212]


---
<!-- pagina 172 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2213]

- 3.13.10.4.8.1  As  long  as  the  displayed  values  are  locked  due  to  SB  feedback  (see  Appendix A.3.10 for details), the on-board equipment shall ensure that the displayed Permitted speed, the displayed SBI speed (if any) and the distance to target never increase (e.g. due to the reduction of T_bs1 and T_bs2 or e.g. due to relocation). In other terms if a concerned  displayed  value  (VP_DMI,  VSBI_DMI  or  target  distance)  calculated  as above has a higher value than the previously displayed value, then the previous value shall remain displayed until a further calculated value is lower than the displayed one. [¶2214]

- 3.13.10.4.9  The on-board shall consider the service brake command as available for use unless: [¶2215]

- The service brake command is not implemented, OR [¶2216]

- The national value inhibits its use. [¶2217]

- 3.13.10.4.10 The on-board equipment shall compare the estimated speed and train position with  the  ceiling  and  braking  to  target  supervision  limits  and  shall  trigger/revoke commands  to  the  train  interface  (traction  cut-off  if  implemented,  service  brake  if available  for  use  or  emergency  brake)  and  supervision  statuses,  by  evaluating  and taking into account the conditions as specified in clause 3.13.10.4.10.1. [¶2218]

- 3.13.10.4.10.1  The conditions in Table 8 and Table 10 shall be evaluated for each target related to an  MRSP speed decrease or LOA, the conditions in Table 9 and Table 11 shall be evaluated  for  the  targets  EOA  and  SvL  and  for  the  end  of  the  maximum  permitted distance to run in Staff Responsible. [¶2219]


---
<!-- pagina 173 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2220]

[¶2221]
| Triggering condition #   | Estimated speed                                                                 | Train front end position (max safe)                 | TI Command triggered   | Supervisi on status triggered   |
|--------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------|------------------------|---------------------------------|
| t3                       | MRSP est et t V V V   arg                                                     |     est P safefront est I V d d V d   max     | -                      | Indication Status               |
| t4                       | MRSP est et t V V V   arg                                                     |   est P safefront V d d  max                     | -                      | Overspeed Status                |
| t6                       | ) ( MRSP warning MRSP est MRSP V dV V V V                                    |     est W safefront est I V d d V d   max     | -                      | Overspeed Status                |
| t7                       | ) ( ) ( arg arg MRSP warning MRSP est et t warning et t V dV V V V dV V     |   est W safefront V d d  max                     | TCO                    | Warning Status                  |
| t9                       | ) ( ) ( MRSP sbi MRSP est MRSP warning MRSP V dV V V V dV V                 |     est SBI safefront est I V d d V d 2 max   | TCO                    | Warning Status                  |
| t10                      | ) ( ) ( arg arg MRSP sbi MRSP est et t sbi et t V dV V V V dV V             |   est SBI safefront V d d 2 max                  | SB                     | Intervention Status             |
| t12                      | ) ( ) ( MRSP ebi MRSP est MRSP sbi MRSP V dV V V V dV V                     |     est EBI safefront est I V d d V d   max   | SB                     | Intervention Status             |
| t13                      | ) ( ) ( arg arg MRSP ebi MRSP est et t ebi et t V dV V V V dV V             |   est EBI safefront V d d  max                   | EB                     | Intervention Status             |
| t15                      | ) ( MRSP ebi MRSP est V dV V V                                                |   est I safefront V d d  max                     | EB                     | Intervention Status             |

Table 8: Triggering of Train Interface commands and supervision statuses in target speed monitoring, MRSP target or LOA [¶2222]


---
<!-- pagina 174 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2223]

![](images/image_0069.png)

Figure 54: Triggering of Train Interface commands and supervision statuses in target speed monitoring, MRSP target or LOA (number in circle corresponds with the equivalent triggering condition in Table 8) [¶2224]


---
<!-- pagina 175 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2225]

[¶2226]
| Triggering condition #   | Estimated speed                                    | Train front end position (estimated and max safe)                                                                                                                        | TI Command triggered   | Supervisi on status triggered   |
|--------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|---------------------------------|
| t3                       | MRSP est release V V V                           | (   est I safefront V d d  max for SvL OR   est I estfront V d d  for EOA ) AND (   est P safefront V d d  max for SvL AND   est P estfront V d d  for EOA ) |                        | Indication Status               |
| t4                       | MRSP est release V V V                           |   est P safefront V d d  max for SvL OR   est P estfront V d d  for EOA                                                                                            |                        | Overspeed Status                |
| t6                       | ) ( MRSP warning MRSP est MRSP V dV V V V       | (   est I safefront V d d  max for SvL OR   est I estfront V d d  for EOA ) AND (   est W safefront V d d  max for SvL AND   est W estfront V d d  for EOA ) | -                      | Overspeed Status                |
| t7                       | ) ( MRSP warning MRSP est release V dV V V V    |   est W safefront V d d  max for SvL OR   est W estfront V d d  for EOA                                                                                            | TCO                    | Warning Status                  |

Chapter 3 [¶2227]


---
<!-- pagina 176 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2228]

[¶2229]
| Triggering condition #   | Estimated speed                                                     | Train front end position (estimated and max safe)                                                                                                                                | TI Command triggered   | Supervisi on status triggered   |
|--------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|---------------------------------|
| t9                       | ) ( ) ( MRSP sbi MRSP est MRSP warning MRSP V dV V V V dV V     | (   est I safefront V d d  max for SvL OR   est I estfront V d d  for EOA ) AND (   est SBI safefront V d d 2 max  for SvL AND   est SBI estfront V d d 1  for EOA ) | TCO                    | Warning Status                  |
| t10                      | ) ( MRSP sbi MRSP est release V dV V V V                         |   est SBI safefront V d d 2 max  for SvL OR   est SBI estfront V d d 1  for EOA                                                                                            | SB                     | Intervention Status             |
| t12                      | ) ( ) ( MRSP ebi MRSP est MRSP sbi MRSP V dV V V V dV V         | (   est I safefront V d d  max for SvL OR   est I estfront V d d  for EOA ) AND   est EBI safefront V d d  max                                                          | SB                     | Intervention Status             |
| t13                      | ) ( MRSP ebi MRSP est release V dV V V V                         |   est EBI safefront V d d  max                                                                                                                                                | EB                     | Intervention Status             |
| t15                      | ) ( MRSP ebi MRSP est V dV V V                                    |   est I safefront V d d  max for SvL OR   est I estfront V d d  for EOA                                                                                                    | EB                     | Intervention Status             |

Table 9: Triggering of Train Interface commands and supervision statuses in target speed monitoring, EOA/SvL with release speed [¶2230]


---
<!-- pagina 177 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2231]

![](images/image_0070.png)

RSM [¶2232]

Figure 55: Triggering of Train Interface commands and supervision statuses in target speed monitoring, EOA/SvL with release speed (number in circle corresponds with equivalent triggering condition in Table 9) [¶2233]


---
<!-- pagina 178 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2234]

[¶2235]
| Revoc ation conditi on #   | Estimated speed             | Train front end position (estimated and max safe)   | TI Command revoked                                                  | Supervision status revoked                                                                                                      |
|----------------------------|-----------------------------|-----------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| r0                         | Standstill                  | Standstill                                          | EB                                                                  | Intervention status                                                                                                             |
| r1                         | et t est V V arg           | Not relevant                                        | TCO SB EB (in case V_target ≠ 0, only if allowed by National Value) | Overspeed status Warning status Intervention status (in case of EB command and V_target ≠ 0, only if allowed by National Value) |
| r3                         | MRSP est et t V V V   arg |   est P safefront V d d  max                     | TCO SB EB (only if allowed by National Value)                       | Overspeed status Warning status Intervention status (in case of EB command, only if allowed by National Value)                  |

Table 10: Revocation of Train Interface commands and supervision statuses in target speed monitoring, MRSP target or LOA [¶2236]

[¶2237]
| Revoc ation conditi on #   | Estimated speed            | Train front end position (estimated and max safe)                              | TI Command revoked                                                   | Supervision status revoked                                                                                                       |
|----------------------------|----------------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| r0                         | Standstill                 | Standstill                                                                     | EB                                                                   | Intervention status                                                                                                              |
| r1                         | release est V V           | Not relevant                                                                   | TCO SB EB (in case V_release ≠ 0, only if allowed by National Value) | Overspeed status Warning status Intervention status (in case of EB command and V_release ≠ 0, only if allowed by National Value) |
| r3                         | MRSP est release V V V   |   est P safefront V d d  max for SvL AND   est P estfront V d d  for EOA | TCO SB EB (only if allowed by National Value)                        | Overspeed status Warning status Intervention status (in case of EB command, only if allowed by National Value)                   |

Table 11: Revocation of Train Interface commands and supervision statuses in target speed monitoring, EOA/SvL with release speed [¶2238]

3.13.10.4.11 Note: For clarity reasons, the Figures 54 and 55 show the train speed/position in a region where the target speed monitoring may not have been entered yet, further to the crossing of an Indication supervision limit. [¶2239]


---
<!-- pagina 179 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2240]

- 3.13.10.4.12 Note:  Figure  55  shows  the  parts  of  the  ceiling  speed  and  braking  to  target supervision  limits,  which  are  used  in  target  speed  monitoring  to  trigger  the  brake commands and the transitions between supervision statuses. It does not show what is displayed to the driver: in particular, the braking to target Permitted supervision limit is displayed (even if not supervised) for values lower than the release speed. [¶2241]

- 3.13.10.4.13 In  case  of  target  EOA/SvL  without  any  supervised  release  speed,  the  Table  9 and Table 11 shall be applied, by substituting V_release with the value 0. [¶2242]

- 3.13.10.4.13.1  In case the target is the location at the end of the maximum permitted distance to run  in  Staff  Responsible,  the  Table  9  and  Table  11  shall  be  applied,  by  substituting V_release with the value 0, SvL with staff responsible end location and by ignoring any formula related to EOA. [¶2243]

- 3.13.10.4.14 A TI command shall be triggered if a corresponding triggering condition is met for at  least  one  target.  On  the  other  hand  it  shall  be  revoked  only  if  a  corresponding revocation condition is met for each supervised target. [¶2244]

- 3.13.10.4.15 The  on-board  equipment  shall  execute  the  transitions  between  the  different supervision statuses as described in Table 12 (see section 4.6.1 for details about the symbols). A triggering condition shall be taken into account as soon as it is satisfied for any  target.  On  the  other  hand  a  transition  from  Overspeed,  Warning  or  Intervention status to the Indication status shall be made only if a revocation condition specified for the concerned transition is met for each supervised target. [¶2245]

[¶2246]
| Normal status             |                           |                           |                           |                     |
|---------------------------|---------------------------|---------------------------|---------------------------|---------------------|
| t3 > -p4-                 | Indication status         | < r1, r3 -p1-             | < r1, r3 -p1-             | < r0, r1, r3 -p1-   |
| t4, t6 > -p3-             | t4, t6 > -p3-             | Overspeed status          |                           |                     |
| t7, t9 > -p2-             | t7, t9 > -p2-             | t7, t9 > -p2-             | Warning status            |                     |
| t10, t12, t13, t15 > -p1- | t10, t12, t13, t15 > -p1- | t10, t12, t13, t15 > -p1- | t10, t12, t13, t15 > -p1- | Intervention status |

Table 12: Transitions between supervision statuses in target speed monitoring [¶2247]


---
<!-- pagina 180 -->

- 3.13.10.4.16 When the speed and distance monitoring function becomes active and the target speed monitoring is the first one entered, the triggering condition t3 defined in Table 8 or  Table  9  shall  be  checked  for  each  target  in  order  to  determine  whether  the Indication status applies. If it  is not the case, the on-board shall immediately set the supervision status to the relevant value, applying a transition from the Indication status according to clause 3.13.10.4.15. [¶2248]

- 3.13.10.4.17 The Normal status is not used in target speed monitoring. However, in case the target  speed  monitoring  is  entered  and  the  supervision  status  was  previously  set  to Normal, the on-board equipment shall immediately execute one of the transitions from the Normal status, as specified in clause 3.13.10.4.15. [¶2249]

- 3.13.10.4.18 Note: Depending upon train speed/position it is possible that for some target(s) none  of  the  triggering  conditions  specified  in  table  8  and  9  is  met.  However  the conditions to enter the target speed monitoring are such (see condition [1] in table 16) that the clauses 3.13.10.4.16 and 3.13.10.4.17 always allow determining a supervision status. [¶2250]

# 3.13.10.5 Requirements for release speed monitoring [¶2251]

3.13.10.5.1  The on-board equipment shall display the Release speed. [¶2252]

- 3.13.10.5.2  The on-board equipment shall display the target distance in the same way as for target speed monitoring, i.e. clauses 3.13.10.4.8 and 3.13.10.4.8.1 shall apply. [¶2253]

- 3.13.10.5.3  The braking to target Permitted speed supervision limit related to the MRDT (i.e. EOA or SvL), as calculated in target speed monitoring from the EBD or SBD, shall also be displayed in the same way as for target speed monitoring, i.e. clauses 3.13.10.4.3 and 3.13.10.4.8.1 shall apply. [¶2254]

- 3.13.10.5.4  The  on-board  equipment  shall  compare the estimated speed with the release speed and  shall  trigger/revoke  commands  to  the  train  interface  (emergency  brake)  and supervision statuses as described in Table 13 and Table 14. [¶2255]

[¶2256]
| Triggering condition #   | Estimated speed   | Location   | TI Command triggered   | Supervision status triggered   |
|--------------------------|-------------------|------------|------------------------|--------------------------------|
| t1                       | release est V V  | Any        | -                      | Indication Status              |
| t2                       | release est V V  | Any        | EB                     | Intervention Status            |

Table 13: Triggering of Train Interface commands and supervision statuses in release speed monitoring [¶2257]


---
<!-- pagina 181 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2258]

[¶2259]
| Triggering condition #   | Estimated speed   | Location   | TI Command revoked   | Supervision status revoked      |
|--------------------------|-------------------|------------|----------------------|---------------------------------|
| r0                       | Standstill        | Standstill | EB                   | Intervention Status             |
| r1                       | release est V V  | Any        | -                    | Overspeed Status Warning Status |

Table 14: Revocation of Train Interface commands and supervision statuses in release speed monitoring [¶2260]

- 3.13.10.5.5  The on-board equipment shall execute the transitions between the different supervision statuses as described in Table 15 (see section 4.6.1 for details about the symbols).  This  table  takes  into  account  the  order  of  precedence  between  the supervision statuses and the possible updates of the release speed while in release speed monitoring. [¶2261]

- 3.13.10.5.6  When  the  speed  and  distance  monitoring  function  becomes  active  and  the  release speed monitoring is the first one entered, the triggering condition t1 defined in Table 13 shall be checked in order to determine whether the Indication status applies. If it is not the case, the on-board shall immediately set the supervision status to the Intervention status, applying a transition from the Indication status according to Table 15. [¶2262]

- 3.13.10.5.7  The  Normal,  Warning  and  Overspeed  statuses  are  not  used  in  release  speed monitoring.  However,  in  case  the  release  speed  monitoring  is  entered  and  the [¶2263]

![](images/image_0071.png)

Table 15: Transitions between supervision statuses in release speed monitoring [¶2264]

[¶2265]
| Normal status   |                   |                  |                |              |
|-----------------|-------------------|------------------|----------------|--------------|
| t1 > -p1-       | Indication status | < r1 -p1-        | < r1 -p1-      | < r0 -p1-    |
|                 |                   | Overspeed status |                |              |
|                 |                   |                  | Warning status |              |
| t2 >            | t2 >              | t2 >             | t2 >           | Intervention |
| -p1-            | -p1-              | -p1-             | -p1-           | status       |


---
<!-- pagina 182 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2266]

supervision status was previously set to Normal, Warning or Overspeed, the on-board equipment  shall  immediately  execute  one  of  the  transitions  from  respectively  the Normal, Warning or Overspeed status, as described in Table 15. [¶2267]

# 3.13.10.6 Transitions between types of Speed and distance monitoring [¶2268]

- 3.13.10.6.1  The  transitions  between  the  Ceiling  speed  monitoring,  the  Target  speed  monitoring and the Release speed monitoring shall be achieved as described in the Table 16: [¶2269]

[¶2270]
| Condi tion id   | Transition condition                                                                                                                                                                                                                                                                                                                                                   | CSM   | TSM   | RSM   |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------|-------|
| [1]             | ((The train has passed with its max safe front end the Indication location calculated from an EBD whose target speed is below or equal to the train speed) OR (The train has passed with its estimated front end the Indication location calculated from the SBD)) AND (In case a release speed is supervised, the train speed is above or equal to the release speed) |      |       |       |
| [2]             | (The train has passed with its max safe front end the RSM start location if it is calculated from an EBD) OR (The train has passed with its estimated front end the RSM start location if it is calculated from the SBD)                                                                                                                                               |      |      |       |
| [3]             | (The MRDT is removed from the list of supervised targets) AND (condition [1] is not fulfilled) AND (condition [2] is not fulfilled)                                                                                                                                                                                                                                    |       |      |      |
| [4]             | (The list of supervised targets is updated) AND (condition [1] is fulfilled) AND (condition [2] is not fulfilled)                                                                                                                                                                                                                                                      |      |       |      |
| [5]             | (The list of supervised targets is updated) AND (condition [2] is fulfilled)                                                                                                                                                                                                                                                                                           |      |      |       |

# Table 16: Transitions between types of Speed and distance monitoring [¶2271]

- 3.13.10.6.2  If  a  transition  of  speed  and  distance  monitoring  occurs  while  a  brake  command  is already  applied,  the  concerned  command  shall  be  maintained  until  the  revocation condition, if specified for the newly entered speed and distance monitoring, is fulfilled. [¶2272]

- 3.13.10.6.2.1  Note:  This  means  that  when  the  service  brake  is  commanded  in  ceiling  speed monitoring  while  it  is  not  available  in  target  speed  monitoring,  the  service  brake remains commanded when the on-board switches to target speed monitoring and is only revoked when the Permitted speed supervision limit is no longer exceeded. [¶2273]

- 3.13.10.6.3  If  a  transition  from  target  speed  monitoring  to  ceiling  speed  or  release  speed monitoring occurs while a traction cut-off command is already applied, the traction cutoff command shall be immediately revoked. [¶2274]

- 3.13.10.6.4  If a transition from target speed monitoring to release speed monitoring occurs while a service  brake  command  is  already  applied,  the  service  brake  command  shall  be immediately revoked. [¶2275]


---
<!-- pagina 183 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2276]

- 3.13.10.6.5  On  executing  a  transition  between  types  of  speed  and  distance  monitoring,  the supervision status shall be determined according to the requirements specified for the newly entered speed and distance monitoring. [¶2277]

# 3.13.11 Perturbation location [¶2278]

- 3.13.11.1 The purpose of the perturbation  location  is  to  trigger  the  MA  request  to  the  RBC  in order  to  renew  the  Movement  Authority  in  due  time  before  the  train  would  have  to brake to an EOA/SvL or LOA target. [¶2279]

- 3.13.11.2 For  the  SvL  or  the  LOA,  the  on-board  shall  calculate  the  perturbation  location  as follows. [¶2280]

- 3.13.11.3 Starting from the first element of the MRSP (i.e. from the start location of the on-board stored  track  description),  the  on-board  shall  calculate  the  location  of  the  Indication supervision  limit,  valid  for  the  speed  of  the  MRSP  element,  taking  into  account  the following assumptions: [¶2281]

- the estimated acceleration shall be set to 'zero' [¶2282]

- if not inhibited by National Value, the compensation of the inaccuracy of the speed measurement  shall  be  set  to  a  value,  calculated  from  the  speed  of  the  MRSP element, as defined in SUBSET-041 § 5.3.1.2: V_delta0ind = f41(V_MRSP-n) [¶2283]

-  If available for use, the service brake feedback shall not have any effect: T_bs1ind and T_bs2ind shall be set to T_bs if the service brake command is available for use, otherwise they shall be set to 'zero'. T_tractionind and T_beremind shall be defined as in 3.13.9.3.2 for T_traction and T_berem by substituting T_bs2 with T_bs2ind [¶2284]

- 3.13.11.4 To calculate the EBI supervision limit, the same formulas defined above with V_est, T_traction,  T_berem  and  V_delta0  shall  be  applied,  by  substituting  V_est  with V_MRSP-n,  T_traction  with  T_tractionind,  T_berem  with  T_beremind  and  V_delta0 with V_delta0ind. [¶2285]

$$
d _ { _ { E B I } } \left ( V _ { _ { M R S P - n } } \right ) = d _ { _ { E B D } } \left ( V _ { _ { M R S P - n } } + V _ { _ { d e l t a 0 i n d } } \right ) - \left ( V _ { _ { M R S P - n } } + V _ { _ { d e l t a 0 i n d } } \right ) \cdot \left ( T _ { _ { b e r e m i n d } } + T _ { _ { t r a c t i o n i n d } } \right )
$$ [¶2286]

$$
d _ { S B I 2 } ( V _ { M R S P - n } ) = d _ { E B I } \left ( V _ { M R S P - n } \right ) - V _ { M R S P - n } \cdot T _ { b s 2 i n d }
$$ [¶2287]

$$
d _ { I } ( V _ { _ { M R S P - n } } ) = d _ { P } ( V _ { _ { M R S P - n } } ) - V _ { _ { M R S P - n } } \cdot T _ { i n d i c a t i o n }
$$ [¶2288]

With     driver n MRSP n MRSP SBI n MRSP P T V V d V d       2 if the GUI curve is inhibited [¶2289]

Or           MRSP n GUI driver n MRSP n MRSP SBI n MRSP P V d T V V d V d        , min 2 if  the  GUI curve is enabled [¶2290]

- 3.13.11.5 If the Indication supervision limit, obtained from the speed of the n th  element, is located between the start and end locations of this n th  element, the perturbation location shall be calculated as follows: [¶2291]


---
<!-- pagina 184 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2292]

$$
& \text {if } d _ { M R S P - n } ^ { a } < d _ { I } \left ( V _ { M R S P - n } \right ) \leq d _ { M R S P - n } ^ { b } \\ & \text {Then } d _ { p e r t u r b a t i o n } = d _ { I } \left ( V _ { M R S P - n } \right )
$$ [¶2293]

3.13.11.6 If the Indication supervision limit, obtained from the speed of the n th  element, is located in advance of the end location of this n th element, and if the Indication supervision limit, obtained from the speed of the n+1 th  element is located in rear of the end location of this n th  element (see Figure 56), the perturbation location shall be calculated as follows: [¶2294]

$$
& \text {if } d _ { I } ( V _ { M R S P - n } ) > d _ { M R S P - n } ^ { b } \text { and } d _ { I } ( V _ { M R S P - n + 1 } ) < d _ { M R S P - n } ^ { b } \\ & \text {Then } d _ { p e r t u r b a t i o n } = d _ { M R S P - n } ^ { b }
$$ [¶2295]

![](images/image_0072.png)

Figure 56: Perturbation location derived from MRSP speed increase [¶2296]

3.13.11.7 For the EOA, the on-board shall calculate its perturbation location in the same way as for  an  EBD based target, except that the formulas to calculate the distance between the location of the Indication supervision limit and the SBD shall be: [¶2297]

$$
\text {the location of the Indication supervision limit and the SBD shall be:} \\ d _ { S B 1 } ( V _ { M R S P - n } ) = d _ { S B D } ( V _ { M R S P - n } ) - V _ { M R S P - n } \cdot T _ { b s 1 n d } \\ d _ { I } ( V _ { M R S P - n } ) = d _ { P } ( V _ { M R S P - n } ) - V _ { M R S P - n } \cdot T _ { i d n d i cation } \\ \text {with } d _ { P } ( V _ { M R S P - n } ) = d _ { S B 1 } ( V _ { M R S P - n } ) - V _ { M R S P - n } \cdot T _ { d r i v e r } \text { if the GUI curve is inhibited} \\ \text {Or } \ d _ { P } ( V _ { M R S P - n } ) = \min \left \{ ( d _ { S B 1 } ( V _ { M R S P - n } ) - V _ { M R S P - n } \cdot T _ { d r i v e r } ) , d _ { G U I } ( V _ { M R S P - n } ) \right \} \text { if } \text { the } \ G U I \\ \text {curve is enabled} \\ 3 . 1 3 . 1 8 \text { The on-board shall trigger the MA request to the RBC when the train has passed.}
$$ [¶2298]

$$
G U \|
$$ [¶2299]

- 3.13.11.8 The  on-board  shall  trigger  the  MA  request  to  the  RBC  when  the  train  has  passed, either with its estimated front end for the perturbation location calculated from the EOA [¶2300]


---
<!-- pagina 185 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2301]

or with its max safe front end for the perturbation location calculated from the SvL or the LOA, the following location: [¶2302]

$$
d _ { _ { M A R } } = d _ { _ { p e r t u r b a t i o n } } - ( V _ { _ { M R S P } } + d V _ { _ { w a r n i n g } } ( V _ { _ { M R S P } } ) ) \cdot T _ { _ { M A R } } \, .
$$ [¶2303]

- 3.13.11.9 If, in exceptional situation (e.g. after a shortening of MA), the EBD, SBD or GUI speed at  the  start  location  of  the  MRSP  is  lower  than  the  speed  of  the  first element of the MRSP,  the  location  to  trigger  the  MA  request  to  the  RBC  shall  be  considered  as already passed. [¶2304]

- 3.13.11.10 Note: For trackside engineering reasons, the assumptions for the calculation of the EBI supervision limit  are  necessary to obtain a fully predictable perturbation location, i.e. independent from the measured acceleration and speed confidence interval. [¶2305]

# 3.14 Brake Command Handling and Protection against Undesirable Train Movement [¶2306]

# 3.14.1 Brake Command Handling [¶2307]

- 3.14.1.1 Note: Whenever the type of brake used is not specified explicitly in the text, it shall be interpreted as not being important for technical interoperability and being a property of the specific implementation. [¶2308]

- 3.14.1.2 In case only the application of  (the non-vital) service brake has been commanded and the service brake fails to be applied, the emergency brake command shall be given. [¶2309]

- 3.14.1.3 If the emergency brake command was triggered due to a trip condition (see chapter 4) the  emergency  brake  command  shall  be  released  at  standstill  and  after  driver acknowledgement of the trip condition. [¶2310]

- 3.14.1.4 For  handling  of  brake  commands  resulting  from  the  speed  and  distance  monitoring, refer to section 3.13.10. [¶2311]

- 3.14.1.5 If  the  brake  command  was triggered due to roll  away  protection,  reverse  movement protection or standstill supervision the brake command shall be released at standstill and after driver acknowledgement. [¶2312]

- 3.14.1.6 If  the  brake  command  was  triggered  due  to  linking  error,  balise  group  message inconsistency  or  RAMS  related  supervision  error,  the  brake  command  shall  be released at standstill. [¶2313]

- 3.14.1.7 If  the  brake command was triggered due to supervision of the safe radio connection (T_NVCONTACT)  the  brake  command  shall  be  released  at  standstill  or  if  a  new consistent message has been received from the RBC. [¶2314]

- 3.14.1.7.1  If the brake command was triggered due to an overpassed reversing distance related to a reversing area or due to any further movement in the direction opposite to the train [¶2315]


---
<!-- pagina 186 -->

orientation while the reversing distance is still overpassed, the brake command shall be released if the reversing distance becomes extended so that the reversing distance is no longer overpassed, or at standstill after driver acknowledgement. [¶2316]

- 3.14.1.7.2  If the brake command was triggered due to change of Train Data while running (see section 5.17 procedure "Changing Train Data from sources different from the driver'), the brake command shall be released at standstill and after driver acknowledgement. [¶2317]

- 3.14.1.7.3  If  the  brake  command was triggered due to the detection of a train movement while modifying/revalidating train data or while entering SR speed/distance limits, the brake command shall be released at standstill and after driver acknowledgement.. [¶2318]

- 3.14.1.7.4  If the brake command was triggered due to an overpassed distance allowed for moving backwards in Post Trip mode or due to any further movement in the direction opposite to  the  train  orientation  while  the  distance allowed for moving backwards in Post Trip mode is still overpassed, the brake command shall be released at standstill and after driver acknowledgement. [¶2319]

- 3.14.1.7.5  If the brake command was triggered due to the driver not having acknowledged a text message, the brake command shall be released after the driver has acknowledged the text message. [¶2320]

- 3.14.1.8 An indication shall be given to the driver to indicate when the brakes can be released and when an acknowledgement is requested. [¶2321]

# 3.14.2 Roll Away Protection [¶2322]

- 3.14.2.1 Note: This protection is only applicable if the required information can be obtained from the direction controller. [¶2323]

- 3.14.2.2 The  Roll  Away  Protection  (RAP)  shall  prevent  the  train  from  moving  in  a  direction, which conflicts with the current position of the direction controller in the active desk. [¶2324]

- 3.14.2.3 If  the  controller  is  in  neutral  position,  the  RAP  shall  prevent  forward  and  reverse movements of the train. [¶2325]

- 3.14.2.4 When the system recognises a movement exceeding the national value for the allowed roll away distance the brakes shall be triggered. [¶2326]

- 3.14.2.5 Refer to section 3.14.1. [¶2327]

- 3.14.2.6 An indication shall be given to the driver showing when the RAP is commanding the brakes. [¶2328]

- 3.14.2.7 After revocation of the brake command the RAP shall be re-initialised using the current position of the train as the new reference location. [¶2329]


---
<!-- pagina 187 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2330]

# 3.14.3 Reverse Movement Protection [¶2331]

- 3.14.3.1 The Reverse Movement Protection (RMP) shall prevent the train from moving in the opposite direction to the permitted one. The permitted movement direction of a train shall  be  the  one  of  the  currently  valid  MA,  if  available  on-board.  See  chapter  4 concerning permitted direction for special cases. [¶2332]

- 3.14.3.2 When a reverse movement is detected, the brake command shall be triggered after a distance specified by the national value. [¶2333]

- 3.14.3.3 Refer to section 3.14.1. [¶2334]

- 3.14.3.4 An indication shall be given to the driver showing when the RMP is commanding the brakes. [¶2335]

- 3.14.3.5 After revocation of the brake command the RMP shall be reinitialised using the current position of the train as the new reference location. [¶2336]

- 3.14.3.6 Information received from balises during reverse movement shall be ignored. [¶2337]

# 3.14.4 Standstill supervision [¶2338]

- 3.14.4.1 This function shall prevent the train from moving. [¶2339]

- 3.14.4.2 When a movement is detected, the brake command shall be triggered after a distance specified by the national value. [¶2340]

- 3.14.4.3 Refer to section 3.14.1. [¶2341]

- 3.14.4.4 After revocation of the brake command the standstill supervision shall be re-initialised. [¶2342]

- 3.14.4.5 If a cab is active, an indication shall be given to the driver showing when the Standstill Supervision is commanding the brakes. [¶2343]

# 3.15 Special functions [¶2344]

# 3.15.1 RBC/RBC Handover [¶2345]

# 3.15.1.1 Introduction [¶2346]

- 3.15.1.1.1  The RBC/RBC Handover principles are such that trains are able to pass from one RBC area to another automatically (without driver action). [¶2347]

- 3.15.1.1.2  This  is  also  granted  when,  due  to  a  failure  in  the  on-board  radio  communication system,  the  on-board  is  no  longer  able  to  manage  two  communication  sessions  at once.  Thereby,  the  behaviour  of  the  RBCs  is  independent  from  such  on-board degraded situation. [¶2348]


---
<!-- pagina 188 -->

- 3.15.1.1.3  However, an RBC/RBC handover performed by a train with only one communication session  available  may  result  in  performance  penalties  since  it  will  not  be  able  to 'prepare' (session establishment, version determination, …) the expected supervision by the Accepting RBC until the on-board disconnects from the Handing Over RBC. [¶2349]

- 3.15.1.1.4  In level 3, trains following the one with only one communication session available will always suffer performance penalties since no more position reports will be issued from the  disconnection from the Handing Over RBC until the connection to the Accepting RBC. [¶2350]

# 3.15.1.2 Handing Over RBC [¶2351]

- 3.15.1.2.1  When the Handing Over RBC detects that a route is set for a train to enter another RBC area, it shall send: [¶2352]

- Intentionally deleted. [¶2353]

- To the Accepting RBC the following information: [¶2354]

-  The ETCS identity of the on-board equipment; [¶2355]

-  The border location that will be passed by the train when entering the Accepting RBC area; [¶2356]

-  Current mode of the on-board equipment; [¶2357]

-  For a leading engine, Train Data and Train Running Number; [¶2358]

-  The system versions supported by the on-board equipment; [¶2359]

-  Optionally, for a non-leading engine, the ETCS identity of the leading engine. [¶2360]

- 3.15.1.2.2  The  Handing  Over  RBC  shall  not  send  information  to  an  on-board  equipment concerning  the  route  in  advance  of  the  border  without  receiving  the  corresponding information from the Accepting RBC. [¶2361]

- 3.15.1.2.3  It shall be possible for the Handing Over RBC to request route related information from the Accepting RBC, limited to a maximum amount of data. [¶2362]

- 3.15.1.2.3.1 Route related information is : [¶2363]

- Movement authorities [¶2364]

- Linking [¶2365]

-  International static speed profiles [¶2366]

- Axle Load Speed profiles [¶2367]

- Gradients [¶2368]

-  Temporary speed restrictions [¶2369]

- Mode profiles [¶2370]

- Intentionally deleted

-  Track Conditions [¶2371]


---
<!-- pagina 189 -->

- Level Transition orders [¶2372]

-  Intentionally deleted

- Route Suitability Data [¶2373]

-   National Values [¶2374]

- Adhesion Factor [¶2375]

- Level Crossings [¶2376]

- Permitted Braking Distance Information [¶2377]

- 3.15.1.2.3.2 Note: The amount of information to be sent between the RBCs is depending on the implementation trackside. [¶2378]

- 3.15.1.2.4  Note: Route related information received from the Accepting RBC will be processed by the Handing Over RBC if possible. [¶2379]

- 3.15.1.2.5  Deleted. [¶2380]

- 3.15.1.2.6  When the Handing Over RBC receives a position report and detects that the maximum safe front end of the train has passed the border location, it shall inform the Accepting RBC. [¶2381]

- 3.15.1.2.6.1 Note: This information might be needed to inform the signalman of the Accepting RBC that the train has entered the Accepting RBC area. [¶2382]

- 3.15.1.2.7  When the Handing Over RBC receives a position report and detects that the minimum safe rear end of the train has crossed the border, it shall send a disconnection order to the on-board equipment. [¶2383]

- 3.15.1.2.8  When the Accepting RBC informs the Handing Over RBC that it has taken over the responsibility,  the  latter  shall  stop  sending  route  related  information  to  the  on-board equipment. [¶2384]

- 3.15.1.2.9  When the Handing Over RBC detects that the transition to the Accepting RBC has to be cancelled, it shall send this cancellation information to the Accepting RBC (including the train identification). [¶2385]

- 3.15.1.2.9.1 Note: For instance, the cancellation procedure can be triggered by: [¶2386]

-  Change to a route which does no more include the border; [¶2387]

-  The sending of an 'end of mission' information from the on-board equipment. [¶2388]

# 3.15.1.3 On-board equipment [¶2389]

- 3.15.1.3.1  When receiving an order to switch to another RBC at a given location, the on-board equipment shall: [¶2390]

- Establish the communication session with the Accepting RBC; [¶2391]


---
<!-- pagina 190 -->

- Send a position report to the Handing Over RBC when the maximum safe front end of the train passes the given location; [¶2392]

-  Send a position report to the Handing Over RBC when the minimum safe rear end of the train passes the given location; [¶2393]

- 3.15.1.3.2  Exception to 3.15.1.3.1 a) (degraded situation): If the on-board equipment is able to handle only one communication session at a given time, it shall wait until the session with the Handing over RBC is terminated due to crossing the border and then establish the session with the Accepting RBC. [¶2394]

- 3.15.1.3.3  As  soon as the on-board equipment has established the session with the Accepting RBC, it shall send its Train Data unless it is in sleeping or non leading mode. [¶2395]

- 3.15.1.3.4  When  the  on-board  equipment  is  connected  to  both  RBCs,  it  shall  send  its  position reports  to  both  of  them  with  the  use  of  the  position  report  parameters  valid  for  the Handing Over RBC. [¶2396]

- 3.15.1.3.4.1 If  the  on-board  equipment is connected to both RBCs, and it executes an End of Mission, it shall execute the End of Mission procedure with both RBCs [¶2397]

- 3.15.1.3.5  As soon as the on-board sends a position report directly to the Accepting RBC with its maximum safe front end having passed the border, it shall use information received from  the  Accepting  RBC and only a disconnection order shall be accepted from the Handing Over RBC. [¶2398]

- 3.15.1.3.5.1 Intentionally deleted. [¶2399]

- 3.15.1.3.6  While  both  communication  sessions  are  opened,  if  information  is  received  from  the Accepting  RBC  before  a  position  report  is  sent  to  the  Accepting  RBC  with  the maximum safe front end having passed the border, this information shall be stored onboard. [¶2400]

Exception: The acknowledgement of Train Data shall be immediately accepted by the on-board equipment. [¶2401]

- 3.15.1.3.6.1 Note:  for  the  exhaustive  list  of  accepted/rejected  information,  please  refer  to Chapter 4 Use of received information. [¶2402]

- 3.15.1.3.7  When the train front end passes the announced border or when an order to execute the  RBC transition  immediately  is  received,  the  on-board  shall  substitute  the  current valid RBC ID/phone number with those of the Accepting RBC. [¶2403]

- 3.15.1.3.8  After this substitution, the on-board shall however retain the RBC ID/phone number of the Handing Over RBC until at least one of the following conditions is fulfilled: [¶2404]

- Min  safe  rear  end  of  the  train  has  passed  the  border  and  the  communication session with this Handing Over RBC has been terminated, [¶2405]

- The RBC transition order is deleted according to A.3.4 or 4.10. [¶2406]


---
<!-- pagina 191 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2407]

- 3.15.1.3.8.1 Note: Even after the train front end has passed the border, the on-board may have to maintain the communication session with the Handing Over RBC (see 3.5.4) or reestablish  it  (see  3.5.3.4  f))  and  needs  therefore  to  remember  the  RBC  ID/phone number of this RBC. [¶2408]

- 3.15.1.3.9  In case the ERTMS/ETCS on-board equipment has reported that the train has passed with its min safe rear end the announced border and no order to terminate the session is  received  from  the  Handing  Over  RBC  within  a  fixed  waiting  time  (see  Appendix A.3.1)  from  the  time  the  position  report  was  sent,  it  shall  repeatedly  send  a  position report with the fixed waiting time after each repetition, until the order to terminate the session  is  received,  or  the  defined  number  of  repetitions  (see  Appendix  A.3.1)  has been  reached.  If  no  reply  is  received  within  the  fixed  waiting  time  after  the  last repetition,  the  ERTMS/ETCS on-board equipment shall terminate the communication session with the Handing Over RBC. [¶2409]

# 3.15.1.4 Accepting RBC [¶2410]

- 3.15.1.4.1  The Accepting RBC shall keep route related information sent to the Handing Over RBC updated. In particular, this possibly includes temporary speed restrictions. [¶2411]

- 3.15.1.4.2  As soon as the Accepting RBC receives from the on-board equipment a position report and detects that the maximum safe front end of the train has passed the border, it shall inform the Handing Over RBC that it has taken over the responsibility. [¶2412]

- 3.15.1.4.3  When the Accepting RBC receives Train Data from both the on-board equipment and the  Handing  over  RBC  Train  Data  provided  by  the  on-board  equipment  shall  take precedence. [¶2413]

- 3.15.1.4.4  If the Accepting RBC receives a cancellation information from the Handing Over RBC, it shall send an order to terminate the communication session to the corresponding onboard equipment (if already established). [¶2414]

- 3.15.1.4.5  The Accepting RBC shall comply with the maximum amount of data contained in the last received route related information request from the Handing Over RBC. [¶2415]

# 3.15.1.5 RBC/RBC message acknowledgement [¶2416]

- 3.15.1.5.1  As soon as a consistent RBC/RBC message including the request for acknowledgement is received, the receiving RBC shall send an acknowledgement to the emitting RBC. [¶2417]

- 3.15.1.5.2  The  RBC/RBC  message  is  consistent  when  all  checks  have  been  completed successfully: [¶2418]

- It  has  passed  the  checks  performed  by  the  RBC/RBC  Safe  Communication Interface protocol (see SUBSET-098); [¶2419]

- Variables in the message do not have invalid values. [¶2420]


---
<!-- pagina 192 -->

- 3.15.1.5.3  The acknowledgement message shall refer to the identity of the concerned message sent by the emitting RBC. [¶2421]

# 3.15.2 Handling of Trains with Non Leading Engines [¶2422]

- 3.15.2.1 It is possible to operate a train using more than one engine, each engine being under the control of a driver. [¶2423]

- 3.15.2.2 Only the leading engine is responsible for the train movement supervision functions. [¶2424]

# 3.15.3 Splitting/joining [¶2425]

- 3.15.3.1 ERTMS/ETCS  allows  Splitting  and  Joining  using  the  normal  supervision  functions available (e.g. On-sight, Shunting). [¶2426]

- 3.15.3.2 Splitting  only  refers  to  the  case  that  the  two  resulting  trains  contain  at  least  one ERTMS/ETCS on-board equipment each. [¶2427]

- 3.15.3.2.1  Note: This must be ensured by operational procedures. [¶2428]

- 3.15.3.3 ERTMS/ETCS  is  not  responsible  for  providing  information  that  a  Splitting/Joining operation has been correctly completed (technical aspect and/or operational aspect). [¶2429]

- 3.15.3.4 Justification: ERTMS/ETCS is not able to provide this information. Splitting and Joining requires the fulfilment of operating rules ensuring that a Splitting/Joining operation has been correctly completed (e.g. physical disconnection). [¶2430]

# 3.15.4 Reversing of movement direction [¶2431]

- 3.15.4.1 It  shall  be  possible  to  send  in  advance  to  an  on-board  equipment  information  about areas, where initiation of reversing of movement direction is possible, i.e. change the direction of train movement without changing the train orientation. [¶2432]

- 3.15.4.1.1  A new reversing area given from the trackside shall replace the one already available on-board. [¶2433]

- 3.15.4.2 Together  with  start  and  end  of  reversing  area,  the  following  supervision  information shall be sent: [¶2434]

- Maximum distance to run in the direction opposite to the orientation of the reversing area, the fixed reference location being the end location of the area where reversing of movement is permitted with which the maximum distance information is sent. [¶2435]

- Reversing mode speed limit allowed during reverse movement. [¶2436]


---
<!-- pagina 193 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2437]

![](images/image_0073.png)

Figure 57: Reversing area and maximum distance to run [¶2438]

- 3.15.4.2.1  The  ERTMS/ETCS  on-board  equipment  shall  use  as  fixed  reference  location  for reversing  distance  the  end  location  of  the  reversing  area  with  which  the  maximum distance information is received. This fixed reference location shall remain unchanged until a new reversing area is received. [¶2439]

- 3.15.4.2.1.1 Example  1:  If  a  closer  SvL  is  defined,  see  Appendix  A.3.4  for  a  complete  list  of situations, the reversing area is deleted beyond the new SvL. The reference location for the distance to run in the direction opposite to the reversing area remains fixed at its original position. [¶2440]

- 3.15.4.2.1.2 Example 2: the fixed reference location remains also unchanged in case of update of distance to run in reverse movement without receiving a new reversing area. [¶2441]

- 3.15.4.2.2  Note: All locations refer to the estimated front end of the train (refer to clause 3.6.4.6). [¶2442]

- 3.15.4.3 New distance to run and Reversing mode speed limit given from the trackside shall replace the one already available on-board. [¶2443]

- 3.15.4.3.1  Intentionally deleted. [¶2444]

![](images/image_0074.png)

Figure 58: Influence of a shortened Movement Authority and of a renewal of the maximum distance to run [¶2445]

Figure 59: Intentionally deleted


---
<!-- pagina 194 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2446]

- 3.15.4.4 While at standstill with the front end of the train inside the indicated area, it shall be possible for the driver to reverse the direction of movement. [¶2447]

- 3.15.4.5 The  on-board  equipment  shall  allow  movement  in  the  direction  opposite  to  the  train orientation, supervising it according to distance and speed received. [¶2448]

- 3.15.4.6 Note: level transitions and RBC/RBC handovers are not handled by the ERTMS/ETCS on-board equipment when in Reversing mode. [¶2449]

- 3.15.4.7 When at standstill the on-board equipment shall inform the driver if the reversing of movement is permitted. [¶2450]

- 3.15.4.8 If the end location of the maximum distance to run in the opposite direction is passed by the train front end, the emergency brake command shall be triggered. [¶2451]

# 3.15.5 Track ahead free [¶2452]

- 3.15.5.1 In  a  level  2/3  area,  the  ERTMS/ETCS on-board equipment is able to handle a track ahead free request given by the RBC. [¶2453]

- 3.15.5.2 The track ahead free request from the RBC shall indicate to the on-board [¶2454]

- at which location the ERTMS/ETCS on-board equipment shall begin to display the request to the driver. [¶2455]

- at  which  location  the  ERTMS/ETCS on-board equipment shall stop to display the request to the driver (in case the driver did not acknowledge). [¶2456]

- 3.15.5.3 As long as it is displayed, the driver has the possibility to acknowledge the track ahead free request (meaning the driver confirms that the track between the head of the train and the next signal or board marking signal position is free). [¶2457]

- 3.15.5.4 When  the  driver  acknowledges,  the  ERTMS/ETCS  on-board  equipment  shall  stop displaying the request, and shall inform the RBC that the track ahead is free. [¶2458]

- 3.15.5.5 There  is  no  restrictive  consequence  by  the  on-board  system  if  the  driver  does  not acknowledge. [¶2459]

- 3.15.5.6 A new track ahead free request shall replace the one previously received and stored. [¶2460]

# 3.15.6 Handling of National Systems [¶2461]

- 3.15.6.1 The  ERTMS/ETCS  on-board  supports  driving  on  national  infrastructure  under  the supervision of National Systems. [¶2462]

- 3.15.6.2 In  case  the  ERTMS/ETCS  on-board  equipment  is  interfaced  to  a  National  System through an STM, refer to Subset 035 for detailed requirements. [¶2463]

- 3.15.6.2.1  Intentionally deleted. [¶2464]

- 3.15.6.3 Intentionally deleted. [¶2465]


---
<!-- pagina 195 -->

- 3.15.6.4 Intentionally deleted. [¶2466]

- 3.15.6.5 Amongst  the  data  to  be  used  by  applications  outside  ERTMS/ETCS  that  can  be transmitted  by  trackside  over  the  ERTMS/ETCS  transmission  channels,  it  shall  be possible to send from balises or RBC data to be forwarded to a National System. [¶2467]

- 3.15.6.5.1  Note:  Definition  of  what  qualifies  as  'data  to  be  forwarded  to  a  National  System'  is national dependent and outside the scope of Subset 026. [¶2468]

# 3.15.7 Tolerance of Big Metal Mass [¶2469]

- 3.15.7.1 Big metal object in the track, exceeding the limits for big metal masses as defined in Subset-036, section 6.5.2 'Metal Masses in the Track' may trigger an alarm reporting a malfunction for the onboard balise transmission function. [¶2470]

- 3.15.7.2 In Levels 0/NTC, the alarms which may be triggered by metal masses shall be ignored for  a  defined  distance  (see  A.3.1).  If  the  alarm  persists  for  a  longer  distance  the ERTMS/ETCS on-board equipment shall trigger a safety reaction. [¶2471]

- 3.15.7.3 Justification: Ignoring the alarm for a defined distance eliminates the need to equip all excessive big metal masses with track condition 'Big Metal Mass' outside ETCS fitted areas. [¶2472]

# 3.15.8 Cold Movement Detection [¶2473]

- 3.15.8.1 After  being  switched  off  (i.e.  once  in  No  Power  mode),  the  ERTMS/ETCS  on-board equipment shall be capable, if fitted with, to detect and record whether the engine has been moved or not, during a period of at least 72 hours. [¶2474]

- 3.15.8.2 When  powered  on  again,  the  ERTMS/ETCS  on-board  equipment  shall  use,  if available,  the  memorised  information  about  cold  movement  in  order  to  update  the status  of  information  stored  by  on-board  equipment  (see  chapter  4  section  4.11  for details). [¶2475]

- 3.15.8.3 Note: information memorised by Cold Movement Detection function is considered as not available if: [¶2476]

- no  Cold  Movement  Detection  function  is  implemented  in  the  ERTMS/ETCS  onboard equipment, OR [¶2477]

- the Cold Movement Detection function has encountered a condition, during the No Power period, which prevents the use of the Cold Movement information (e.g. the battery ensuring the Cold Movement Detection function has run down during the No Power period). [¶2478]


---
<!-- pagina 196 -->

# 3.15.9 Virtual Balise Cover [¶2479]

- 3.15.9.1 It shall be possible to set and remove from balise a Virtual Balise Cover (VBC). A VBC is defined by: [¶2480]

- A marker corresponding to balises to be ignored by the on-board together with the area (country or region) in which the VBC is applicable. The VBC marker and the country/region identity form the unique VBC identity. [¶2481]

- Its validity period. [¶2482]

- 3.15.9.2 During a start of mission, the driver shall have the opportunity to set a new VBC, or to remove an existing one. [¶2483]

- 3.15.9.3 As long as a VBC is stored on-board: [¶2484]

- The  ERTMS/ETCS  on-board  equipment  shall  ignore  any  balise  telegram  that includes  a  VBC  marker  and  a  country/region  identity  that  both  match  the  VBC identity. [¶2485]

- No  reaction  shall  be  applied  if  errors  in  the  reading  of  the  rest  of  such  balise telegram occur. [¶2486]

- 3.15.9.4 If  the  ERTMS/ETCS  on-board  equipment  receives  from  balise  or  from  driver  a  new VBC with the same VBC identity as an already stored VBC, the new VBC shall replace the previous one, including its validity period. [¶2487]

- 3.15.9.5 A VBC shall be retained on-board when the on-board equipment is switched off (i.e. enters No Power mode) and shall remain applicable when powered on again. It shall be deleted when: [¶2488]

- it is ordered by trackside, or [¶2489]

- its validity period has elapsed, or [¶2490]

-  it is removed by the driver (during Start of Mission), or [¶2491]

- a mismatch is detected between the country/region identity read from a balise group and the country/region identity of the VBC. Note: this means that the reception of a consistent balise group message is a necessary condition for deleting a VBC due to mismatching country/region identities. [¶2492]

# 3.15.10 Advance display of route related information [¶2493]

- 3.15.10.1 The  ERTMS/ETCS  on-board  equipment  shall  display  an  overview  of  the  gradient profile (as received from trackside), of the MRSP, of the track conditions (except the tunnel  stopping  areas),  of  the  first  Indication  location,  if  any  (only  in  Ceiling  Speed monitoring),  and  of  the  EOA/LOA,  with  the  remaining  distances  referred  to  the  train front end position. [¶2494]


---
<!-- pagina 197 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2495]

- 3.15.10.2 With  regards  to  the  MRSP,  the  track  conditions  and  the  EOA/LOA,  the  remaining distances  shall  be  computed  taking  into  account  the  min  safe,  the  estimated  or  the max safe train front end position depending on their respective supervision. [¶2496]

- 3.15.10.3 With regards to the gradient profile, the remaining distances shall be computed taking into account the estimated train front end position. [¶2497]

- 3.15.10.3.1  With regards to the first Indication location, the remaining distance shall be computed as specified in clauses 3.13.10.3.8 and 3.13.10.3.8.1. [¶2498]

- 3.15.10.4 The overview of route related information shall be restricted to the elements contained within the movement authority and up to the first target at zero speed, if any. [¶2499]

# 3.16 Data Consistency [¶2500]

# 3.16.1 Criteria of consistency [¶2501]

- 3.16.1.1 The on-board shall not consider a message transmitted from the trackside if any of the following criteria is not fulfilled. [¶2502]

- Correctness of the received message: the whole message shall be complete and respect the ETCS language; variables shall not have invalid values [¶2503]

- The message shall be received in due time. [¶2504]

-  The message shall be received at the right expected location. [¶2505]

- 3.16.1.1.1  Regarding a): a value of a variable is invalid when a spare value is used. [¶2506]

# 3.16.2 Balises [¶2507]

# 3.16.2.1 Definitions [¶2508]

- 3.16.2.1.1  The information that is sent from a balise is called a balise telegram. [¶2509]

- 3.16.2.1.2  The  whole  set  of  information  (balise  telegram  or  telegrams)  coming  from  a  balise group is called a balise group message. [¶2510]

- 3.16.2.1.2.1 Note: In case of a balise group containing a single balise, telegram and message coincide. [¶2511]

- 3.16.2.1.3  Intentionally deleted. [¶2512]

# 3.16.2.2 General [¶2513]

- 3.16.2.2.1  If the on-board is not able to recognise whether a balise group is linked or unlinked (if none of the balises in the balise group can be read correctly), it shall consider it as unlinked. [¶2514]

- 3.16.2.2.2  A balise within a balise group shall be regarded as missed if [¶2515]


---
<!-- pagina 198 -->

- No balise is found within the maximum distance between balises from the previous balise in the group. [¶2516]

or [¶2517]

- A following balise within the group has been passed. [¶2518]

# 3.16.2.3 Linking Consistency [¶2519]

- 3.16.2.3.1  If linking information is used the on-board shall react according to the linking reaction information in the following cases: [¶2520]

- If  the  location  reference  of  the  expected  balise  group  is  found  in  rear  of  the expectation window [¶2521]

- If  the  location  reference  of  the  expected  balise  group  is  not  found  inside  the expectation  window  (i.e.  the  end  of  the  expectation  window  has  been  reached without having found the expected balise group) [¶2522]

-  If  inside  the  expectation  window  of  the  expected  balise group another announced balise group, expected later, is found. [¶2523]

- 3.16.2.3.1.1 The  ERTMS/ETCS  on-board  equipment  shall  reject  the  message  from  a  balise group found with its location reference outside its expectation window. [¶2524]

- 3.16.2.3.2  The on-board shall reject the message from the expected group and trip the train if the balise group is passed in the unexpected direction. [¶2525]

- 3.16.2.3.2.1 Exception:  When  the  expected  balise  group  is  referred  in  the  linking  information with a balise group with ID 'unknown', 3.4.4.4.2.1 shall apply. [¶2526]

- 3.16.2.3.3  If the location reference balise of the group is duplicated and the on-board is only able to correctly evaluate the duplicating one, the duplicating one shall be used as location reference instead. [¶2527]

- 3.16.2.3.4  If the balise duplicating the location reference balise is used as location reference for the  group,  and  is  found  within  the  expectation  window,  no  linking  reaction  shall  be applied. [¶2528]

# 3.16.2.4 Balise Group Message Consistency [¶2529]

- 3.16.2.4.1  If  linking  information  is  used,  the  on-board  shall  reject  the  message  from  a  linked balise group found in the expected location and react according to the linking reaction in the following cases: [¶2530]

- A balise is missed inside the group. [¶2531]

- A balise is detected but no telegram is decoded (e.g. wrong CRC,...). [¶2532]

-  Variables in the balise group message have invalid values. [¶2533]

- Message counters do not match (see 3.16.2.4.7) [¶2534]


---
<!-- pagina 199 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2535]

- 3.16.2.4.2  Exception: Concerning a) and b) above, the ERTMS/ETCS on-board equipment shall not reject the message and shall not apply the linking reaction if the balise not found, or  not  decoded,  is  duplicated  within  the  balise  group  and  the  duplicating  one  is correctly read. [¶2536]

- 3.16.2.4.3  If  linking  information  is  used,  the  on-board  shall  reject  the  message  from  a  balise group marked as linked but not included in the linking information. No reaction shall be applied, even if errors in the reading of the balise group occur. [¶2537]

- 3.16.2.4.4  If no linking information is used, the on-board shall reject the message from a balise group marked as linked and command application of the service brake in the following cases: [¶2538]

- A balise is missed inside the group. [¶2539]

- A balise is detected, but no telegram is decoded (e.g. wrong CRC). [¶2540]

-  Variables in the balise group message have invalid values. [¶2541]

- Message counters do not match (see 3.16.2.4.7) [¶2542]

- 3.16.2.4.4.1 Exceptions: Concerning a) and b) of clause 3.16.2.4.4, the ERTMS/ETCS on-board equipment: [¶2543]

- shall not reject the message and shall not command application of the service brake if  the  balise  not  found,  or  not  decoded,  is  duplicated  within  the  balise  group,  the duplicating one is correctly read and contains: [¶2544]

-  directional  information  while  the  orientation  of  the  balise  group  can  still  be evaluated, or [¶2545]

-  only information valid for both directions, or [¶2546]

-  neither directional information nor information valid for both directions, or [¶2547]

-  only data to be used by applications outside ERTMS/ETCS, or [¶2548]

-  only  data  to  be  used  by  applications  outside  ERTMS/ETCS  together  with other information valid for both directions. [¶2549]

- shall  not  command  application  of  the  service  brake  if  the  telegram  correctly  read from another balise of the group contains the information 'Inhibition of balise group message consistency reaction'. [¶2550]

- 3.16.2.4.4.2 Concerning  clause  3.16.2.4.4,  if  the  service  brake  is  applied,  the  location  based information stored on-board shall be shortened to the current position when the train has reached standstill. Refer to appendix A.3.4 for the exhaustive list of information, which shall be shortened. [¶2551]

- 3.16.2.4.4.3 Concerning  clause  3.16.2.4.4,  if  the  service  brake  is  applied,  the  driver  shall  be informed that this is due to a balise group message consistency problem. [¶2552]

- 3.16.2.4.5  A message counter shall be attached to each balise telegram indicating which balise group message the telegram fits to. [¶2553]


---
<!-- pagina 200 -->

- 3.16.2.4.6  Instead of a message counter corresponding to a given balise group message, it shall be possible to identify a telegram as always fitting all possible messages of the group. [¶2554]

- 3.16.2.4.6.1 It  shall also be possible to identify a telegram as never fitting any message of the group. [¶2555]

- 3.16.2.4.7  Comparing message counters of the received telegrams of a balise group message, excluding the ones complying with 3.16.2.4.6 and the ones that are not used by the onboard to compose the message (see 3.16.2.4.8.2), if their values are not all identical, or  at  least  one  of  them  complies  with  3.16.2.4.6.1,  this  shall  be  considered  as  a message consistency error. [¶2556]

- 3.16.2.4.7.1 In  case  of  single  balise  group,  if  the  message  counter  of  the  received  telegram complies  with  3.16.2.4.6.1,  this  shall  also  be  considered  as  a  message  consistency error. [¶2557]

- 3.16.2.4.8  It  shall  be  possible  to  indicate  failures  in  the  system  underlying  the  balise/loop/RIU (e.g. the Lineside Electronic Unit, LEU) by sending a balise telegram, a loop message or a RIU message including the information "default balise/loop/RIU information". [¶2558]

- 3.16.2.4.8.1 If one (and only one) out of a pair of duplicated balise telegrams received by the onboard includes the information 'default balise information', the on-board shall ignore any other information included in this telegram and shall consider information from the telegram not containing 'default balise information". [¶2559]

- 3.16.2.4.8.2 When duplicated balises are both found and decoded correctly, and both, or none of  them,  contain  "default  balise  information",  the  ERTMS/ETCS  on-board  equipment shall compose the message using the telegram from the last received balise out of the pair. [¶2560]

- 3.16.2.4.9  If a message has been received containing the information "default balise information", the driver shall be informed. [¶2561]

# 3.16.2.5 Unlinked Balise Group Message Consistency [¶2562]

- 3.16.2.5.1  An on-board equipment shall reject the message received from a balise group marked as unlinked and command application of the service brake in the following cases: [¶2563]

- A balise is missed inside the unlinked balise group. [¶2564]

- A balise is detected, but no telegram is decoded (e.g. wrong CRC). [¶2565]

-  Variables in the balise group message have invalid values. [¶2566]

- Message counters do not match (see 3.16.2.4.7) [¶2567]

- 3.16.2.5.1.1 Exceptions: Concerning a) and b) of clause 3.16.2.5.1, the ERTMS/ETCS on-board equipment: [¶2568]


---
<!-- pagina 201 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2569]

-  shall  not  reject  the  message  and  shall  not  command  application  of  the  service brake if the balise not found, or not decoded, is duplicated within the balise group, the duplicating one is correctly read and contains: [¶2570]

-  directional  information  while  the  orientation  of  the  balise  group  can  still  be evaluated, or [¶2571]

-  only information valid for both directions, or [¶2572]

-  neither directional information nor information valid for both directions, or [¶2573]

-  only data to be used by applications outside ERTMS/ETCS, or [¶2574]

-  only data to be used by applications outside ERTMS/ETCS together with other information valid for both directions. [¶2575]

- shall  not  command  application  of  the  service  brake  if  the  telegram  correctly  read from another balise of the group contains the information 'Inhibition of balise group message consistency reaction'. [¶2576]

- 3.16.2.5.2  Concerning  clause  3.16.2.5.1,  if  the  service  brake  is  applied,  the  location  based information stored on-board shall be shortened to the current position when the train has reached standstill. Refer to appendix A.3.4 for the exhaustive list of information, which shall be shortened. [¶2577]

- 3.16.2.5.3  Concerning  clause  3.16.2.5.1,  if  the  service  brake  is  applied,  the  driver  shall  be informed that this is due to a balise group message consistency problem. [¶2578]

# 3.16.2.6 Linking Reactions [¶2579]

- 3.16.2.6.1  When the linking reaction leads to train trip or a service brake application, the driver shall  be  informed  that  the  intervention  is  due  to  data  consistency  problem  with  the expected balise group. [¶2580]

- 3.16.2.6.2  If  the  service  brake  is  initiated  due  to  the  linking  reaction,  the  location  based information stored on-board shall be shortened to the current position when the train has reached standstill. Refer to appendix A.3.4 for the exhaustive list of information, which shall be shortened. [¶2581]

# 3.16.2.7 RAMS related supervision functions [¶2582]

- 3.16.2.7.1  Mitigation of balise reception degradation [¶2583]

- 3.16.2.7.1.1 If 2 consecutive linked balise groups announced by linking are not detected and the end  of  the  expectation  window  of  the  second  balise  group  has  been  passed,  the ERTMS/ETCS  on-board  shall  command  the  service  brake  and  the  driver  shall  be informed.  At  standstill,  the  location  based  information  stored  on-board  shall  be shortened  to  the  current  position.  Refer  to  appendix  A.3.4  for  the  exhaustive  list  of information, which shall be shortened. [¶2584]

- 3.16.2.7.2  Mitigation of balise cross-talk while expecting repositioning information [¶2585]


---
<!-- pagina 202 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2586]

- 3.16.2.7.2.1 If repositioning is announced and the expected repositioning balise group has been found,  the  ERTMS/ETCS  on-board  equipment  shall  keep  looking  for  a  balise  group that satisfies  the  same  criteria  as  this  previously  expected  and  already  found repositioning balise group, until one of the following events occurs: [¶2587]

- the  on-board  antenna  leaves  the  expectation  window  of  the  repositioning  balise group that was announced and already found [¶2588]

- a linked balise group that has been announced with known identity is found. [¶2589]

- 3.16.2.7.2.2 If  a  second balise group is found that satisfies the same criteria as the previously expected  and  already  found  repositioning  balise  group,  the  ERTMS/ETCS  on-board equipment  shall  command  the  service  brake  and  the  driver  shall  be  informed.  At standstill,  the  location  based  information  stored  on-board  shall  be  shortened  to  the current position.  Refer to appendix A.3.4 for the exhaustive list of information, which shall be shortened. [¶2590]

- 3.16.2.7.2.3 Note:  this  function  is  independent  from  linking  function,  i.e.  the  rules  related  to linking  always  apply.  This  means  that  once  a  repositioning  balise  group  has  been found and if this  latter  contains  new  linking  information,  the  ERTMS/ETCS on-board equipment  will  start  expecting  the  first  balise  group  announced  in  this  new  linking information in parallel with the monitoring specified in 3.16.2.7.2.1. [¶2591]

# 3.16.3 Radio [¶2592]

# 3.16.3.1 General issues [¶2593]

- 3.16.3.1.1  A radio message is consistent when all checks have been completed successfully: [¶2594]

- Checks performed by Euroradio protocol have been passed (see Subset-037) [¶2595]

- Time stamps checks have been passed (see 3.16.3.3.3) [¶2596]

-  Variables in the messages do not have in-valid values. [¶2597]

- 3.16.3.1.1.1 The on-board shall reject a message transmitted from the trackside if the message is not consistent. [¶2598]

- 3.16.3.1.1.2 The on-board shall inform the trackside if a not consistent message is received. [¶2599]

- 3.16.3.1.2  Emergency  messages  shall  be  transmitted  either  as  high  priority  data  or  as  normal priority data. [¶2600]

- 3.16.3.1.3  Other messages shall be sent as normal priority data. [¶2601]

- 3.16.3.1.3.1 Messages shall only be accepted when received with the data priority for which they are specified. [¶2602]

- 3.16.3.1.4  The chapters 3.16.3.2 to 3.16.3.5 define data consistency principles and corresponding checks for data transmitted as normal priority data. For high priority data, the checks shall not apply. [¶2603]


---
<!-- pagina 203 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2604]

# 3.16.3.2 Time stamping [¶2605]

- 3.16.3.2.1  The trackside shall always transmit its information with reference to the train time. [¶2606]

- 3.16.3.2.2  To  time-stamp  its  messages,  the  trackside  shall  make  a  safe  estimation  of  the  onboard  time,  based  on  the  time-stamp  of  the  received  messages  and  the  internal processing times. The estimation shall be made in such a way that the on-board time estimated by the trackside shall not be in advance of the real on-board time. [¶2607]

- 3.16.3.2.3  Wrap  around  of  the  onboard  timer  can  occur  during  a  communication  session  and shall have no impact on system behaviour. [¶2608]

# 3.16.3.3 Supervision of Sequence [¶2609]

- 3.16.3.3.1  The trackside shall time-stamp a message with a value corresponding to the time of sending. [¶2610]

- 3.16.3.3.2  There shall always be a time stamp increment between consecutive messages. [¶2611]

- 3.16.3.3.3  If the time stamp of the last received message is lower than or equal to the former one its content shall not be used. [¶2612]

- 3.16.3.3.3.1 Only time stamps of messages received as normal priority data shall be used. [¶2613]

- 3.16.3.3.3.2 Note: The supervision does not detect a lost message. This has to be assured by means of the 'acknowledge' function. [¶2614]

- 3.16.3.3.4  Intentionally deleted. [¶2615]

![](images/image_0075.png)

Figure 60: Supervision of sequence [¶2616]

# 3.16.3.4 Supervision of safe radio connection [¶2617]

- 3.16.3.4.1  When  the  difference  between  the  time  stamp  of  the  latest  consistent  received message and the current on-board time is greater than the T_NVCONTACT parameter (national  value),  the  on-board  shall  apply  the  reaction  required  by  trackside  (see 3.16.3.4.2). [¶2618]


---
<!-- pagina 204 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2619]

- 3.16.3.4.1.1 After  the  on-board  equipment  has  switched  to  L2  or  3  with  no  communication session  established,  the  current  onboard  time  shall  be  compared  with  the  on-board time  at  the  moment  of  the  level  transition  (instead  of  the  time  stamp  of  the  latest consistent received message) until a new consistent message has been received. [¶2620]

- 3.16.3.4.1.2 When an RBC/RBC handover has been announced, the current onboard time shall be compared with the time stamp of the latest consistent message from the Handing over RBC until the train considers the Accepting RBC as the supervising one (refer to 3.15.1.3.5). From then on the current onboard time shall be compared with the time stamp of the latest received consistent message from the Accepting RBC. [¶2621]

- 3.16.3.4.1.3 As long as the train front end is inside an announced radio hole, the ERTMS/ETCS on-board equipment shall stop the supervision of the safe radio connection. Afterwards,  until  a  new  consistent  message  has  been  received,  the current onboard time shall be compared with the on-board time when the train front end left the radio hole (instead of the time stamp of the latest consistent received message). [¶2622]

![](images/image_0076.png)

Figure  61:  Supervision  of  the  safe  radio  connection  (Message  received  within the Window) [¶2623]

![](images/image_0077.png)


---
<!-- pagina 205 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2624]

# Figure 62: Supervision of the safe radio connection (No message received within the Window) [¶2625]

- 3.16.3.4.2  It shall be possible to select one of the following reactions (National value) : [¶2626]

- Train trip [¶2627]

- Apply service brake [¶2628]

-  No reaction [¶2629]

- 3.16.3.4.3  For all reactions, if no new consistent message has been received after an additional delay time (as defined in A.3.1), the on-board shall release the safe radio connection and then set-up it again (maintaining the communication session). [¶2630]

- 3.16.3.4.4  When the reaction leads to train trip or a service brake application, the driver shall be informed that no safe radio message has been received in due time. [¶2631]

- 3.16.3.4.5  If the service brake is initiated, the following reaction shall be taken; [¶2632]

- For brake command release conditions refer to section 3.14.1.7. [¶2633]

- If  no  new  consistent  message  is  received  until  the  train  reaches  standstill,  the location  based  information  stored  on-board  shall  be  shortened  to  the  current position. Refer to appendix A.3.4 for the exhaustive list of information, which shall be shortened. [¶2634]

- 3.16.3.4.6  Intentionally deleted. [¶2635]

- 3.16.3.4.7  To avoid the expiration of the on-board timer and if no new information is needed to be sent, the RBC shall send an empty message. [¶2636]

# 3.16.3.5 Message Acknowledgement [¶2637]

- 3.16.3.5.1  As soon as a consistent message  (see  3.16.3.1.1) including the request for acknowledgement  is  received,  the  on-board  shall  send  an  acknowledgement  to  the trackside. [¶2638]

- 3.16.3.5.1.1 Note:  In  order  to  ensure  trackside  that  the  on-board  has  correctly  received transmitted information, the RBC may ask the on-board to acknowledge. [¶2639]

- 3.16.3.5.2  Intentionally deleted

- 3.16.3.5.3  The acknowledgement message shall refer to the identity of the concerned message sent by the RBC. [¶2640]

- 3.16.3.5.4  Intentionally deleted. [¶2641]

# 3.16.4 Error reporting to RBC [¶2642]

- 3.16.4.1 In level 2/3, if a radio communication session is established, errors shall be reported as soon as the availability of a safe radio connection permits. [¶2643]


---
<!-- pagina 206 -->

- 3.16.4.2 This refers to balise group errors and radio message errors regardless if there is an error reaction. [¶2644]

- 3.16.4.3 If  linking  information  is  used  on-board,  no  error  reporting  shall  be  done  for  balise groups marked as linked but not included in the linking information. [¶2645]

# 3.17 System Version Management [¶2646]

# 3.17.1 Introduction [¶2647]

- 3.17.1.1 Definitions,  high  level  principles  and  rules  regarding  the  offline  management  of ERTMS/ETCS system version during the ERTMS/ETCS system life time are given in SUBSET-104. [¶2648]

- 3.17.1.2 The objective of this section is to define requirements applicable to ERTMS/ETCS onboard  equipment  and  to  trackside  constituents,  when different versions  of the ERTMS/ETCS system have been defined. [¶2649]

- 3.17.1.3 Intentionally deleted. [¶2650]

# 3.17.2 Determination of the operated system version [¶2651]

- 3.17.2.1 The on-board equipment shall be able to operate with (i.e. shall support) any of the ERTMS/ETCS system version numbers X included in the envelope of legally operated system versions, as defined in chapter 6. [¶2652]

- 3.17.2.1.1  Within one of its supported system version numbers X, the on-board equipment shall always  operate  the  highest  system  version  number  Y  defined  in  this  release  of  the SRS, regardless of the system version number Y transmitted by the trackside. [¶2653]

- 3.17.2.2 The on-board equipment shall operate with only one system version at a time, i.e. it shall behave according to the whole set of requirements applicable to a system version (refer  to  chapter  6  in  case  the  operated  system  version  is  older  than  the  last  one introduced in this release of the SRS). [¶2654]

- 3.17.2.3 The  on-board  equipment  shall  determine  the  operated  system  version  number  X,  in relation to non-RBC  trackside constituents, as the system version  number  X transmitted by any balise, loop or RIU, if this system version number X is higher than the currently operated one. [¶2655]

- 3.17.2.4 It  shall  be  possible  from  balise  group  to  order  the  on-board  equipment  to  operate  a system version. [¶2656]

- 3.17.2.5 On  receiving  the  order  to  operate  system  version  from  balise  group,  the  on-board equipment shall immediately operate the system version number X given in the order. After  the  order  is  executed,  the  requirement  3.17.2.3  shall  be  again  applied  for  any further received balise telegram/loop message or any further contacted RIU. [¶2657]


---
<!-- pagina 207 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2658]

- 3.17.2.5.1  Note: the system version order is to be used wherever it is necessary to enforce an operated system version number X lower than the currently operated one. [¶2659]

- 3.17.2.6 If a mismatch has been detected between the country or region identifier read from a balise/loop and the corresponding identifier(s) for which a set of national values is used onboard,  the  on-board  equipment  shall  consider  the  system  version  number  X transmitted  by  this  balise/loop  as  the  operated  one  and  shall  comply  again  with requirement 3.17.2.3. [¶2660]

- 3.17.2.7 If the on-board equipment does not support the system version number X transmitted by a non-RBC trackside constituent or the one specified in the balise group order, it shall consider the operated system version as unchanged. [¶2661]

- 3.17.2.8 In  case  of  communication  session  established  with  an  RBC,  the  system  version number X of the RBC shall take precedence on the operated system version in relation to  non-RBC  constituents  and  on  system  version  ordered  from  balise  group;  the operated  system  version  number  X  shall  be  determined  according  to  the  following principles: [¶2662]

- if the on-board equipment is in level 0, NTC or 1 (e.g. entrance in level 2/3 area), the RBC system version number X shall be operated when the transition to level 2/3 is executed; [¶2663]

- if  the  on-board  equipment  is  in  level  2/3  (SoM  procedure  or  order  received  from trackside), the RBC system version number X shall be operated immediately; [¶2664]

-  in  case  of  session  established  with  an  accepting  RBC  (RBC/RBC  Handover),  the accepting RBC system version number X shall be operated as soon as the engine has passed the RBC/RBC border location with its maximum safe front end; [¶2665]

- in case the on-board equipment switches from level 2/3 to another level (e.g. exit from a level 2/3 area), the system  version  control in relation  to  non-RBC constituents  shall  be  again  applied  and  the  balise  group  orders  shall  be  again considered; [¶2666]

- in  case  the  engine  passes  the  RBC/RBC  border  location  with  its  maximum  safe front end and no session is established with the accepting RBC, the system version control  in  relation  to  non-RBC  constituents  shall  be  again  applied  and  the  balise group orders shall be again considered. [¶2667]

- 3.17.2.9 The system version currently operated when the on-board equipment is switched off (i.e. enters No Power mode) shall be retained and re-used when powered on. [¶2668]

- 3.17.2.9.1  If the on-board  equipment  loses  the  information  (failure  situation), the highest supported system version shall be used. [¶2669]

# 3.17.3 Handling of trackside data in relation to system version [¶2670]

- 3.17.3.1 Every telegram transmitted by a balise, and every message transmitted by Euroloop and Radio Infill Unit shall contain only the data related to one system version. It is not [¶2671]


---
<!-- pagina 208 -->

allowed for the balise, Euroloop and Radio Infill Unit to transmit data correspondent to several system versions. [¶2672]

- 3.17.3.2 All  messages  transmitted  by  an  RBC  shall  contain  data  only  related  to  one  system version. [¶2673]

- 3.17.3.3 The  on-board  equipment  shall  check  the  system  version  prior  to  any  further  checks (data consistency, ..), as they depend on the system version. [¶2674]

- 3.17.3.4 Intentionally deleted. [¶2675]

- 3.17.3.4.1  Intentionally deleted. [¶2676]

- 3.17.3.4.2  Intentionally deleted. [¶2677]

- 3.17.3.5 The  on-board  equipment  shall  check  the  ERTMS/ETCS  system  version  number  X transmitted by any balise: [¶2678]

- In all levels, if this system version number X equals to 0, the balise information shall be ignored. [¶2679]

- In all levels, if this system version number X is different from 0 and lower than the lowest system version number X supported by the on-board equipment, it shall be able  to  interpret  the  balise  information,  to  the  extent  defined  for  each  type  of information (see chapter 6 for detailed requirements). If the on-board is not able to interpret the information, this shall be considered as a message consistency error. [¶2680]

-  In all levels, if this system version number X is amongst its supported ones, the onboard equipment shall be able to interpret the balise information. See chapter 6 for detailed requirements. [¶2681]

- In  levels  1,  2  and  3,  if  this  system  version  number  X  is  greater  than  the  highest version number X supported by the on-board equipment, the information from this balise shall be ignored, the train shall be tripped and an indication shall be given to the driver. [¶2682]

- In  levels  0  and  NTC,  if  this  system  version  number  X  is  greater  than  the  highest version number X supported by the on-board equipment, the information from this balise shall be ignored and no reaction shall be applied. [¶2683]

- 3.17.3.6 In  level  1  the  on-board  equipment  shall  check  the  ERTMS/ETCS  system  version number X transmitted by any Euroloop found: [¶2684]

- if this system version number X is lower than the lowest system version number X supported  by  the  on-board  equipment,  it  shall  be  able  to  interpret  the  loop information,  to  the  extent  defined  for  each  type  of  information  (see  chapter  6  for detailed requirements). If the on-board is not able to interpret the information, this shall be considered as a message consistency error. [¶2685]

- if  this  system  version  number  X  is  amongst  its  supported  ones,  the  on-board equipment shall be able to interpret the loop information. See chapter 6 for detailed requirements. [¶2686]


---
<!-- pagina 209 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2687]

-  If  this  system  version  number  X  is  greater  than  the  highest  version  number  X supported  by  the  on-board  equipment,  no  reaction  shall  be  applied  and  the information from this loop shall be ignored. [¶2688]

- 3.17.3.7 The  on-board  equipment  shall  check  the  ERTMS/ETCS  system  version  number  X transmitted the first time any RBC is contacted (including RBC hand over) or any RIU is contacted. Refer to section 3.5.3.7 d) for details. [¶2689]

- 3.17.3.8 Intentionally deleted. [¶2690]

- 3.17.3.9 Intentionally deleted. [¶2691]

- 3.17.3.10 Intentionally deleted. [¶2692]

- 3.17.3.11 For trackside information only differing by Y with regards to the highest system version number  X  supported  by  on-board,  the  on-board  equipment  shall  not  consider  the reception of unknown packet/message as a message data consistency error (i.e. use of  spare value for NID_PACKET or NID_MESSAGE) and shall ignore the content of the unknown packet/message in the following cases: [¶2693]

- unknown packet included in a balise telegram/loop message related to the higher system version; [¶2694]

- unknown  radio  message  from  an  RBC  or  RIU  operating  with  the  higher  system version; [¶2695]

-  unknown  packet  from  an  RBC  or  RIU  operating  with  the  higher  system  version, included  in  a  message  in  which  one  or  more  optional  packet  can  be  added according to the version operated by on-board. [¶2696]

- 3.17.3.12 Intentionally deleted. [¶2697]

- 3.17.3.12.1  Intentionally deleted. [¶2698]

- 3.17.3.13 Intentionally deleted. [¶2699]

# 3.18 System Data [¶2700]

# 3.18.1 Fixed Values [¶2701]

- 3.18.1.1 Note: Appendix to chapter 3 contains a list of Fixed values used as system parameters in the supervision. These parameters are system related and can easily be changed in later  versions of the ERTMS/ETCS if required. These parameters are not defined as National data. [¶2702]

# 3.18.2 National / Default Values [¶2703]

- 3.18.2.1 Note: Appendix to chapter 3 contains list of National and Default Values. [¶2704]


---
<!-- pagina 210 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2705]

- 3.18.2.2 Trains shall be supervised according to the National Values of the current infrastructure if they are available on-board. [¶2706]

- 3.18.2.3 National Values are transmitted with the area(s) (country or region) in which they are applicable. They shall become applicable at a defined location, or shall be applicable immediately. [¶2707]

- 3.18.2.4 Evaluating  a  balise  group  message,  the  balise  identity  information  referring  to  the country or region shall be used to ensure that correct National Values are used. [¶2708]

- 3.18.2.5 For each National Value, the corresponding Default Value shall be used as fall back value if: [¶2709]

-  the National Value  is not available, or [¶2710]

-  a mismatch has been detected between the country or region identifier read from a balise group and the corresponding identifier(s) of the applicable set with which the National Value was received and stored. [¶2711]

- 3.18.2.6 Note:  even  though  the  National  Values  are  always  transmitted  as  a  single  set  for  a given  system  version,  the  content  of  a  set  depends  on  the  system  version,  so  that when a set of National Values is received or becomes applicable, or when passing a balise  group,  the  on-board  equipment  may  apply  clause  3.18.2.5  for  a  subset  of National Values [¶2712]

- 3.18.2.7 The National Values currently applicable when the on-board equipment is switched off (i.e.  enters  No  Power  mode)  shall  be  retained  and  shall  remain  applicable  when powered on. [¶2713]

- 3.18.2.7.1  Justification:    The  aim  of  this  requirement  is  to  limit  the  number  of  balise  groups containing  National  Value  information.  Once  a  set  of  National  Values  has  been received on-board, there is no need to re-load the information unless National Values change, the on-board equipment loses the information (failure situation), or the train enters an area requiring different National Values. [¶2714]

- 3.18.2.8 The applicable set of National Values data shall be transmitted from the trackside on transition between areas requiring a different set of National Values. [¶2715]

- 3.18.2.8.1  When  a  new  set  of  National  Values  becomes  applicable  its  content  shall  always overwrite  the  corresponding  National  Values  currently  applicable  regardless  of  the country or region identifier(s). [¶2716]

- 3.18.2.9 A  previously  received  set  of  National  Values  which  is  not  yet  applicable  shall  be deleted if: [¶2717]

-  a new set of National Values is received, or [¶2718]

-  the  ERTMS/ETCS  on-board  equipment  is  switched  off  (i.e.,  enters  No  Power mode). [¶2719]

- 3.18.2.10 If a National Value becomes invalid, i.e., a mismatch has been detected between the country or region identifier read from a balise group and the corresponding identifier(s) [¶2720]

3.6.0 [¶2721]

13/05/2016 [¶2722]


---
<!-- pagina 211 -->

of  the  applicable  set  with  which  the  National  Value  was  received  and stored,  then it shall be deleted. [¶2723]

- 3.18.2.11 When  a  new  set  of  National  Values  becomes  applicable,  any  ongoing  supervision involving  an  overwritten  National  Value  of  type  time  or  distance  shall  continue,  but using  the  corresponding  value  from  the  new  set.  However,  the  starting  location  or starting time shall remain unchanged. [¶2724]

# 3.18.3 Train Data [¶2725]

- 3.18.3.1 Train Data can neither be provided nor modified  by  ERTMS/ETCS  trackside equipment. [¶2726]

- 3.18.3.2 Before starting a mission, the Train Data shall be acquired by the ERTMS/ETCS onboard equipment of a leading engine [¶2727]

- Train category(ies) [¶2728]

- Train length [¶2729]

-  Traction / brake parameters: [¶2730]

-  Traction model [¶2731]

-  Braking  models  (brake  build  up  time  and  speed  dependent  deceleration)  or brake percentage [¶2732]

-  Brake position [¶2733]

-  On-board correction factors [¶2734]

-  Nominal rotating mass [¶2735]

- Maximum train speed [¶2736]

- Loading gauge [¶2737]

-  Axle load category [¶2738]

- Traction system(s) accepted by the engine [¶2739]

- Train fitted with airtight system [¶2740]

- List of National Systems available on-board [¶2741]

- Intentionally deleted

-  Axle number [¶2742]

- 3.18.3.2.1  The  Train  Data  may  come  from  ERTMS/ETCS  external  sources  (e.g.  the  Train Interface), from pre-configured values or from the driver. [¶2743]

- 3.18.3.2.2  Exception: The driver shall never be involved in the entry/ modification/validation of the Train  Data  'Traction  system(s)  accepted  by  the  engine',  'List  of  National  Systems available on-board' and 'Axle number'. [¶2744]


---
<!-- pagina 212 -->

- 3.18.3.2.3  The unit,  range  and  resolution  of  the  Train  Data  that  can  be  directly  entered  by  the driver shall be as specified in A.3.11. [¶2745]

- 3.18.3.3 At standstill, it shall be possible for the driver to enter, modify and revalidate the Train Data that requires driver validation according to the specific train implementation. [¶2746]

- 3.18.3.3.1  In normal operation after the start of mission, if a train movement is detected while the driver  is  modifying  or  revalidating  the  Train  Data,  the  ERTMS/ETCS  on-board equipment shall trigger the brake command. [¶2747]

- 3.18.3.4 Following  any  entry/modification  of  Train  Data  when  a  communication  session  is already  established  or  following  the  successful  establishment  of  a  communication session when valid Train Data are already available (e.g. when approaching a level 2/3 area or an accepting RBC area), the ERTMS/ETCS on-board equipment of the leading engine shall send the following set of Train Data to the RBC: [¶2748]

- Train category(ies). [¶2749]

- Train length. [¶2750]

-  Maximum train speed. [¶2751]

- Loading gauge. [¶2752]

- Axle load category. [¶2753]

-  Traction system(s) accepted by the engine. [¶2754]

- Train fitted with airtight system. [¶2755]

- List of National Systems available on-board [¶2756]

-  Axle number [¶2757]

- 3.18.3.4.1  The RBC shall acknowledge the reception of this set of Train Data. [¶2758]

- 3.18.3.4.2  In case the safe radio connection is lost before the acknowledgement is received, the Train Data shall be sent again once the safe radio connection has been re-established within the ongoing communication session. [¶2759]

- 3.18.3.5 Intentionally deleted. [¶2760]

- 3.18.3.6 For modification of Train Data, which is/are affected by a change of input information from  the  ERTMS/ETCS  on-board  equipment  external  interface,  refer  to  procedure "Changing Train Data from sources different from the driver" described in section 5.17. [¶2761]

- 3.18.3.7 In case the Train Data regarding train category, axle load category, loading gauge or traction system has been changed and the train is at standstill: [¶2762]

- the  location  based  information  stored  on-board  shall  be  shortened  to  the  current position of the train. Refer to appendix A.3.4 for the exhaustive list of information, which shall be shortened. [¶2763]


---
<!-- pagina 213 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2764]

- the  stored  MA,  linking  and  track  description,  which  have  been  received  from  the RBC after a level 2/3 transition or a RBC transition for a further location has been ordered, shall be deleted. [¶2765]

- 3.18.3.8 In case the Train Data regarding train length has been increased, the currently used track description, if any, shall be considered as unknown in rear of the former min safe rear end of the train. [¶2766]

# 3.18.4 Additional Data [¶2767]

# 3.18.4.1 Driver ID [¶2768]

- 3.18.4.1.1  The driver ID shall be used to identify the responsible person for operating an active desk. [¶2769]

- 3.18.4.1.1.1 Note: This data is used for recording purposes only. [¶2770]

- 3.18.4.1.2  If  allowed  by  a  National  value,  it  shall  be  possible  for  the  driver  to  change  driver  ID while the train is running. [¶2771]

- 3.18.4.1.3  It shall be possible to enter driver ID also in a non-leading engine. [¶2772]

- 3.18.4.1.4  The unit, range and resolution of the driver ID shall be as specified in A.3.11. [¶2773]

# 3.18.4.2 ERTMS/ETCS Level [¶2774]

- 3.18.4.2.1  The driver shall have the possibility to enter the ERTMS/ETCS level during a start of a mission. [¶2775]

- 3.18.4.2.2  The  ERTMS/ETCS  level  information  is  required  for  train  operation  except  sleeping mode. [¶2776]

- 3.18.4.2.3  In  normal  operation  after  the  start  of  mission  the  driver  shall  not  have  to  select  the ERTMS/ETCS level (all other level transitions are executed automatically). [¶2777]

- 3.18.4.2.4  For operational fallback situations: at standstill, the onboard equipment shall allow the driver to change the ERTMS/ETCS level. [¶2778]

- 3.18.4.2.4.1 Intentionally deleted. [¶2779]

- 3.18.4.2.5  If the table of supported levels given by trackside is available, the selection of level by the  driver  shall  be  limited  to  those  contained  in  this  table.  If  the  table  of  trackside supported  levels  is  not  available,  the  driver  can  select  any  level  within  a  default  list configured on-board. [¶2780]

# 3.18.4.3 Radio data: Network identification / RBC Identification / Telephone Number [¶2781]

- 3.18.4.3.1  The  ERTMS/ETCS  on-board  equipment  shall  store  one  valid  RBC  identity  and telephone  number  at  a  time,  obtained  from  the  last  driver  data  entry,  from  the  last received order to establish a session with an RBC (excluding RBC transition orders) or from the crossing of a RBC/RBC border (see clause 3.15.1.3.7). [¶2782]


---
<!-- pagina 214 -->

- 3.18.4.3.1.1 Note: If a valid RBC identity and telephone number is available on-board, no driver data entry is needed to establish a connection to the RBC when performing a start of mission or after a manual level change to level 2/3. [¶2783]

- 3.18.4.3.2  In  level  2/3  only,  at  standstill,  the  ERTMS/ETCS  on-board  equipment  shall  offer  the driver  different  means  to  select  the  RBC  contact  information  (RBC  identity  and telephone number to be used), for details see step S3, section 5.4, Start of Mission procedure. [¶2784]

- 3.18.4.3.3  Intentionally deleted. [¶2785]

- 3.18.4.3.4  If  the  driver  selects  'Use  of  EIRENE  short  number'  to  contact  the  RBC  and  the communication  session  is  successfully  established,  the  ERTMS/ETCS  on-board equipment shall store as valid RBC identity and telephone number, the RBC identity reported by EURORADIO and the EIRENE short number, respectively. [¶2786]

- 3.18.4.3.4.1 Note: If the short number is re-used by the ERTMS/ETCS on-board equipment (e.g. following a loss of safe radio connection) and does not direct to a RBC with the stored RBC ID, the connection will be terminated (EURORADIO functionality). [¶2787]

- 3.18.4.3.5  The unit, range and resolution of the RBC identity and telephone number shall be as specified in A.3.11. [¶2788]

- 3.18.4.3.6  At  standstill,  the  ERTMS/ETCS  on-board  equipment  shall  offer  the  possibility  to  the driver to modify the Radio Network ID. [¶2789]

# 3.18.4.4 ETCS Identity [¶2790]

- 3.18.4.4.1  The ETCS identity of an on-board equipment is made of a single identity number. The ETCS identity of an RBC, balise group, loop or RIU is composed of a country/region identity number and of an identity number within the country/region. [¶2791]

- 3.18.4.4.2  All on-board equipments in service, balise groups marked as linked, RBC's, RIU's, and loops shall be assigned a unique ETCS identity within their respective group. [¶2792]

- 3.18.4.4.3  The  assignment  of  (unique  or  not)  ETCS  identities  to  balise  groups  marked  as unlinked is the sole responsibility of the entity in charge of the assignment of values (see SUBSET-054), depending on the specific trackside implementation. [¶2793]

# 3.18.4.5 Train Running Number [¶2794]

- 3.18.4.5.1  During the Start of Mission, the ERTMS/ETCS on-board equipment of a leading engine shall acquire the train running number from driver input, from the RBC or from other ERTMS/ETCS external sources. [¶2795]

- 3.18.4.5.2  It shall be possible to enter train running number also in a non-leading engine. [¶2796]

- 3.18.4.5.3  It shall be possible to change the train running number while running, from driver input, from the RBC or from other ERTMS/ETCS external sources. [¶2797]


---
<!-- pagina 215 -->

- 3.18.4.5.4  Following  any  entry/modification  of  the  train  running  number  when  a  communication session is already established or following the successful establishment of a communication  session  when  valid  train  running  number  is  already  available,  the ERTMS/ETCS on-board equipment shall send the train running number to the RBC. [¶2798]

- 3.18.4.5.4.1 Exception: if the train running number has been received from the RBC, it shall not be sent back to the RBC by the ERTMS/ETCS on-board equipment. [¶2799]

- 3.18.4.5.5  The  unit,  range  and  resolution  of  the  train  running  number  shall  be  as  specified  in A.3.11. [¶2800]

# 3.18.4.6 Adhesion Factor [¶2801]

- 3.18.4.6.1  The  adhesion  factor  is  used  to  adjust  the  emergency  brake  model  of  the  train  (see 3.13). [¶2802]

- 3.18.4.6.2  The adhesion factor may be changed while the train is running. [¶2803]

- 3.18.4.6.2.1 It shall be possible to update the adhesion factor from trackside and - if permitted by a National value - by the driver. If, following a change of National Values, the update of the adhesion factor is no more permitted to the driver, the adhesion factor previously modified by the driver to slippery rail shall immediately be reset to non slippery rail. Any trackside adhesion profile is not affected. [¶2804]

- 3.18.4.6.2.2 The adhesion factor shall be sent as profile data from trackside when needed. [¶2805]

- 3.18.4.6.2.3 The driver shall be informed whether the value of the adhesion factor is 'slippery rail'. [¶2806]

- 3.18.4.6.3  The selection of the adhesion value from trackside or by driver entry shall be limited to the options slippery rail/ non slippery rail. [¶2807]

- 3.18.4.6.3.1 Intentionally deleted. [¶2808]

- 3.18.4.6.4  The default value for the adhesion factor shall be the highest value (i.e. not slippery rail). [¶2809]

- 3.18.4.6.5  Intentionally deleted. [¶2810]

# 3.18.5 Date and Time [¶2811]

- 3.18.5.1 Each ERTMS/ETCS on-board equipment shall be able to provide the date (day, month, year) and time (hour, minute, second) in Universal Time Co-ordinated (UTC) and Local Time. [¶2812]

- 3.18.5.2 The local time shall be presented to the driver, while the UTC shall be used for the juridical data. [¶2813]

- 3.18.5.3 Deleted. [¶2814]


---
<!-- pagina 216 -->

# 3.18.6 Data view [¶2815]

- 3.18.6.1 Outside the context of data entry, the ERTMS/ETCS on-board equipment shall offer the  possibility  to  the  driver  to  view  the  driver  ID,  the  train  running  number,  the  RBC contact  information,  the  radio  network  ID,  the  Virtual  Balise  Cover(s)  and  the  Train Data  either  modifiable  by  the  driver  or  modifiable  by  other  ERTMS/ETCS  external sources. [¶2816]

- 3.18.6.2 Only valid data shall be presented to the driver. [¶2817]

# 3.19 Intentionally deleted

# 3.20 Juridical Data [¶2818]

- 3.20.1.1 The on-board recording device of the train is not part of the ERTMS/ETCS on-board equipment. [¶2819]

- 3.20.1.2 The  ERTMS/ETCS  on-board  equipment  shall  transmit  to  the  on-board  recording device the information that may be used for legal purpose after hazardous situations. [¶2820]

- 3.20.1.2.1  For details about data messages that shall be transmitted to the on-board recording device and their related triggering events, refer to SUBSET-027. [¶2821]

- 3.20.1.3 Intentionally deleted. [¶2822]

- 3.20.1.4 Intentionally deleted. [¶2823]

- 3.20.1.5 Intentionally deleted. [¶2824]

- 3.20.1.6 Intentionally deleted. [¶2825]

- 3.20.1.7 Intentionally deleted. [¶2826]

- 3.20.1.8 Intentionally deleted. [¶2827]

- 3.20.1.9 Intentionally deleted. [¶2828]

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2829]


---
<!-- pagina 217 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2830]

# APPENDIX TO CHAPTER 3 [¶2831]

# A.3.1 List of Fixed Value Data [¶2832]

[¶2833]
| Fixed Value Data                                                                                            | Value    | Name           |
|-------------------------------------------------------------------------------------------------------------|----------|----------------|
| The number of times to try to establish a safe radio connection.                                            | 3 times  |                |
| Repetition of radio messages (i.e. excluding the first sending)                                             | 3 times  |                |
| Waiting time before radio message repetition                                                                | 15 s     |                |
| Speed difference between Permitted speed and Emergency Brake Intervention supervision limits, minimum value | 7.5 km/h | dV_ebi_min     |
| Speed difference between Permitted speed and Emergency Brake Intervention supervision limits, maximum value | 15 km/h  | dV_ebi_max     |
| Value of MRSP where dV_ebi starts to increase to dV_ebi_max                                                 | 110 km/h | V_ebi_min      |
| Value of MRSP where dV_ebi stops to increase to dV_ebi_max                                                  | 210 km/h | V_ebi_max      |
| Speed difference between Permitted speed and Service Brake Intervention supervision limits, minimum value   | 5.5 km/h | dV_sbi_min     |
| Speed difference between Permitted speed and Service Brake Intervention supervision limits, maximum value   | 10 km/h  | dV_sbi_max     |
| Value of MRSP where dV_sbi starts to increase to dV_sbi_max                                                 | 110 km/h | V_sbi_min      |
| Value of MRSP where dV_sbi stops to increase to dV_sbi_max                                                  | 210 km/h | V_sbi_max      |
| Speed difference between Permitted speed and Warning supervision limits, minimum value                      | 4 km/h   | dV_warning_min |
| Speed difference between Permitted speed and Warning supervision limits, maximum value                      | 5 km/h   | dV_warning_max |
| Value of MRSP where dV_warning starts to increase to dV_warning_max                                         | 110 km/h | V_warning_min  |
| Value of MRSP where dV_warning stops to increase                                                            | 140 km/h | V_warning_max  |


---
<!-- pagina 218 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2834]

[¶2835]
| to dV_warning_max                                                                                                                |            |                |
|----------------------------------------------------------------------------------------------------------------------------------|------------|----------------|
| Time before the first Indication to display the TTI                                                                              | 14 s       | T_dispTTI      |
| Time between Warning supervision limit and SBI                                                                                   | 2 s        | T_warning      |
| Driver reaction time between Permitted speed supervision limit and SBI                                                           | 4 s        | T_driver       |
| Maximum possible rotating mass as a percentage of the total weight of the train                                                  | 15%        | M_rotating_max |
| Minimum possible rotating mass as a percentage of the total weight of the train                                                  | 2%         | M_rotating_min |
| MA request repetition cycle, default value                                                                                       | 60 s       | T CYCRQSTD     |
| Level/Mode transitions: Driver acknowledgement time                                                                              | 5 s        | T ACK          |
| Maximum time to maintain a communication session in case of failed re-connection attempts                                        | 5 minutes  |                |
| Distance of metal immunity in Levels 0/NTC                                                                                       | 300 metres | D_Metal        |
| Driver reaction time before sounding the horn                                                                                    | 4 s        |                |
| Time between minimum safe rear end of the train leaving a track condition area and on-board deleting the applicable indication   | 5 s        |                |
| Distance to keep on-board information in rear of the min safe rear end of the train                                              | 300 metres |                |
| Additional delay time to disconnection on supervision of safe radio connection                                                   | 60 s       |                |
| 'Connection status' timer for safe radio connection indication                                                                   | 45 s       |                |
| Time from the latest Radio Network registration order to a Mobile Terminal after which the registration is considered as failed. | 40s        |                |

# A.3.2 List of National / Default Data [¶2836]

[¶2837]
| National / Default Data                   | Default Value   | SRS Name (Reference only)   |
|-------------------------------------------|-----------------|-----------------------------|
| Modification of adhesion factor by driver | Not allowed     | Q_NVDRIVER_ADHES            |
| Shunting mode speed limit                 | 30km/h          | V_NVSHUNT                   |
| Staff Responsible mode speed limit        | 40km/h          | V_NVSTFF                    |
| On Sight mode speed limit                 | 30km/h          | V_NVONSIGHT                 |


---
<!-- pagina 219 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2838]

[¶2839]
| Limited Supervision mode speed limit                                                                | 100 km/h           | V_NVLIMSUPERV   |
|-----------------------------------------------------------------------------------------------------|--------------------|-----------------|
| Unfitted mode speed limit                                                                           | 100km/h            | V_NVUNFIT       |
| Release Speed                                                                                       | 40km/h             | V_NVREL         |
| Distance to be used in Roll Away protection, Reverse movement protection and Standstill supervision | 2m                 | D_NVROLL        |
| Permission to use service brake in target speed monitoring                                          | Yes                | Q_NVSBTSMPERM   |
| Permission to release emergency brake                                                               | Only at standstill | Q_NVEMRRLS      |
| Permission to use guidance curves                                                                   | No                 | Q_NVGUIPERM     |
| Permission to use the service brake feedback                                                        | No                 | Q_NVSBFBPERM    |
| Permission to inhibit the compensation of the speed measurement inaccuracy                          | No                 | Q_NVINHSMICPERM |
| Speed limit for triggering the override function                                                    | 0km/h              | V_NVALLOWOVTRP  |
| Override speed limit to be supervised when the 'override' function is active                        | 30 km/h            | V_NVSUPOVTRP    |
| Distance for train trip suppression when override function is triggered                             | 200m               | D_NVOVTRP       |
| Max. time for train trip suppression when override function is triggered                            | 60 s               | T_NVOVTRP       |
| Change of driver ID permitted while running                                                         | Yes                | M_NVDERUN       |
| System reaction if T_NVCONTACT elapses                                                              | No reaction        | M_NVCONTACT     |
| Maximum time since the time-stamp in the last received message                                      |                   | T_NVCONTACT     |
| Distance to be allowed for reversing in Post Trip mode.                                             | 200 m              | D_NVPOTRP       |
| Max permitted distance to run in Staff Responsible mode                                             |                   | D_NVSTFF        |
| Default location accuracy of a balise group                                                         | 12 m               | Q_NVLOCACC      |
| Weighting factor for available wheel/rail adhesion                                                  | 0                  | M_NVAVADH       |
| Confidence level for emergency brake safe deceleration on dry rails                                 | 99.9999999%        | M_NVEBCL        |
| Train length step used for the integrated correction factor Kr_int                                  | N/A                | L_NVKRINT       |
| Train length dependent integrated correction factor Kr_int                                          | 0.9                | M_NVKRINT*      |
| Speed step used for the integrated correction factor Kv_int                                         | N/A                | V_NVKVINT       |
| Speed dependent integrated correction factor Kv_int                                                 | 0.7                | M_NVKVINT*      |


---
<!-- pagina 220 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2840]

[¶2841]
| Integrated correction factor for brake build up time               | 1.1       | M_NVKTINT      |
|--------------------------------------------------------------------|-----------|----------------|
| Maximum deceleration value under reduced adhesion conditions (1)   | 1.0 m/s 2 | A_NVMAXREDADH1 |
| Maximum deceleration value under reduced adhesion conditions (2)   | 0.7 m/s 2 | A_NVMAXREDADH2 |
| Maximum deceleration value under reduced adhesion conditions (3)   | 0.7 m/s 2 | A_NVMAXREDADH3 |
| Lower deceleration limit to determine the set of Kv_int to be used | N/A       | A_NVP12        |
| Upper deceleration limit to determine the set of Kv_int to be used | N/A       | A_NVP23        |

*The default value of the correction factor Kr_int shall be valid for any train length, and likewise the default  value  of  the  correction  factor  Kv_int  shall  be  valid  for  any  brake  position,  speed  and maximum emergency brake deceleration. This means that the Kr_int model does not contain any train length step, and that the Kv_int model is valid for all train types and does neither contain any speed step nor any pivot deceleration limit.

# A.3.3 Handling of information received from trackside [¶2842]

- A.3.3.1 Before it  can  be  accepted  and  used  by  the  ERTMS/ETCS on-board equipment, raw information received from trackside is subject to various checks, which can lead to the individual  rejection/ignoring  of  information  (e.g.  Movement  Authority  not  valid  for  the train  orientation),  the  ignoring  of  a  whole  balise  telegram  or  the  rejection  of  a  whole message. The SRS clauses/sections corresponding to these checks are gathered in Table 17. [¶2843]

[¶2844]
|                             | Type of data           | Type of data         | Type of data                                                                                                     |
|-----------------------------|------------------------|----------------------|------------------------------------------------------------------------------------------------------------------|
| Type of check               | Individual information | Telegram             | Message                                                                                                          |
| System Version              | 3.17.3.11 a) & c)      | 3.17.3.5 a), d) & e) | 3.17.3.5 b) 3.17.3.6 a) 3.17.3.6 c) 3.17.3.11 b)                                                                 |
| Virtual Balise Cover        |                        | 3.15.9.3 a)          |                                                                                                                  |
| Reverse Movement Protection |                        | 3.14.3.6             |                                                                                                                  |
| Duplicated balises          | 3.16.2.4.8.1           | 3.16.2.4.8.2         |                                                                                                                  |
| Linking                     |                        |                      | 3.4.4.4.2 and 3.16.2.4.3 3.4.4.4.2.1 3.16.2.3.1.1 together with 3.4.4.4.3 3.16.2.3.2 with exception 3.16.2.3.2.1 |


---
<!-- pagina 221 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2845]

[¶2846]
|                                                                                   | Type of data                                               | Type of data                                                                                                                                                                                                                                                                                                                     | Type of data   |
|-----------------------------------------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Type of check                                                                     | Individual information                                     | Message                                                                                                                                                                                                                                                                                                                          |                |
| Message consistency                                                               |                                                            | 3.16.2.4.1 together with 3.16.2.4.7, 3.16.2.4.7.1 and with exception 3.16.2.4.2 3.16.2.4.4 together with 3.16.2.4.7, 3.16.2.4.7.1 and with exception 3.16.2.4.4.1 a) 3.16.2.5.1 together with 3.16.2.4.7, 3.16.2.4.7.1 and with exception 3.16.2.5.1.1 a) 3.16.3.1.1.1 together with 3.16.3.1.1 a), 3.16.3.3.3 and 3.16.3.1.1 c) |                |
| Validity direction                                                                | 3.6.3.1.3 3.6.3.1.3.1 3.6.3.1.4 with exception 3.6.3.1.4.1 |                                                                                                                                                                                                                                                                                                                                  |                |
| Level, mode, transmission medium, infill/not infill, other miscellaneous criteria | 4.8                                                        |                                                                                                                                                                                                                                                                                                                                  |                |

Table 17: Check of raw data received from trackside [¶2847]

- A.3.3.2 With the exception of the clauses/sections referred to in  Table 17 and of the clause 3.16.3.5.1, all the clauses in this specification in which trackside information is referred to  (through  the  terms  'balise',  'telegram',  'balise  group  [message]',  'message', '[name of] information'...), shall be applied assuming that the information has not been ignored/rejected by the ERTMS/ETCS on-board equipment due to all the checks listed in Table 17. [¶2848]

- A.3.3.3 Example  1:  clause  3.16.2.4.9  has  to  be  understood  as  follows:  'If  a <consistent> message <composed with telegrams that have passed the system version check, that have  not  been  ignored  because  of  a  VBC,  that  have  not  been  ignored  because  of duplication, and that have been received while no reverse movement was performed> has been received < with one of its telegrams composing it> containing the information 'default balise information' <which is valid for the train orientation (or the balise group crossing  direction  for  NL  or  SL  engines)  and  which  has  passed  the  level  and  mode filters> , the driver shall be informed.' [¶2849]

- A.3.3.4 Example 2: as a result of the clause A.3.3.2, the ERTMS/ETCS on-board equipment will  not  apply requirements in relation to the content of the telegram or the message such as: [¶2850]


---
<!-- pagina 222 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2851]

-  clause  3.6.2.2.2  a),  in  case  the  balise  group  message  is  rejected  because  not consistent (e.g. according to 3.16.2.4.1), it does not become LRBG [¶2852]

-  clause  3.16.3.3.3.1,  in  case  the  radio  message  is  rejected  because  of  its  time stamp,  this  latter  will  not  be  used  by  the  on-board  to  check  the  supervision  of sequence of further messages [¶2853]

-  clause  3.17.2.3,  in  case  the  balise  telegram  is  ignored  because  of  its  system version number (e.g. according to 3.17.3.5 d)), this latter will not affect the system version operated by the on-board [¶2854]

-  clause 3.18.2.5 2 nd  bullet, in case a message from a balise group marked as linked is rejected because  the balise group was  not announced  by  linking (see 3.16.2.4.3), the balise group country or region identifier will not be compared with the one(s) of the currently applicable set of National Values [¶2855]

# A.3.4 Handling of Accepted and Stored Information in specific Situations [¶2856]

# A.3.4.1 Introduction [¶2857]

- A.3.4.1.1 All data that can be stored onboard after being accepted may be influenced in special situations. [¶2858]

- A.3.4.1.2 The situations acting on the 'status' of stored information are: [¶2859]

- the execution of a conditional emergency stop (3.10.2.2); [¶2860]

- the reception of a shortened MA (3.8.5.1.3, 3.8.5.1.4); [¶2861]

-  the stored MA is shortened due to a section time-out (3.8.4.2.2); [¶2862]

- the  SvL  is  shifted  (to  the  DP  if  any  or  to  the  EOA)  due  to  an  overlap  time-out (3.8.4.4.2) ; [¶2863]

- the stored MA is shortened due to an end section time-out (3.8.4.1.2); [¶2864]

-  a cooperative MA revocation is granted by the onboard (3.8.6.2); [¶2865]

- inconsistency  in  a  balise  group  marked  as  unlinked  and  the  train  is  at  standstill (3.16.2.5.2); [¶2866]

- a linking reaction led to a service brake and the train is at standstill (3.16.2.6.2) ; [¶2867]

- the  reaction  due  to  the  supervision  of  the  safe  radio  connection  led  to  a  service brake and the train is at standstill (3.16.3.4.5 b) ; [¶2868]

-  the train category, axle load category, loading gauge or traction system is changed and the train is at standstill (3.18.3.7) ; [¶2869]

-  driver closes the desk during SoM ; [¶2870]

- RAMS  related  supervision  functions  led  to  a  service  brake  and  the  train  is  at standstill (3.16.2.7) [¶2871]


---
<!-- pagina 223 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2872]

-  inconsistency  in  a  balise  group  marked  as  linked  and  no  linking  is  used  onboard and the train is at standstill (3.16.2.4.4.2) [¶2873]

- the Limit of Authority becomes an End of Authority and the on-board considers an SvL (3.8.4.3.2) [¶2874]

- A.3.4.1.3 Depending on the situation, the action shall be one of the following: [¶2875]

- data is deleted, [¶2876]

- data is reset (set to initial states) [¶2877]

-  data status is unchanged, [¶2878]

- data is to be revalidated [¶2879]

D = Deleted U = Unchanged R = Reset TBR = To Be Revalidated [¶2880]

[¶2881]
|                                                                    | Situations listed above   | Situations listed above   | Situations listed above   |
|--------------------------------------------------------------------|---------------------------|---------------------------|---------------------------|
| Data Stored on-board                                               | a - d, f, n               | e, g - j, l,m             | k                         |
| National Values                                                    | U                         | U                         | U                         |
| Not yet applicable National Values                                 | D[1]                      | D[10]                     | D                         |
| Linking                                                            | D[1]                      | D[10]                     | D                         |
| Movement Authority                                                 | D[1] [3]                  | D[10] [11]                | D[5]                      |
| Gradient Profile                                                   | D[1]                      | D[10]                     | D                         |
| International SSP                                                  | D[1]                      | D[10]                     | D                         |
| Axle load speed profile                                            | D[1]                      | D[10]                     | D                         |
| STM max speed                                                      | U                         | U                         | D                         |
| STM system speed/distance                                          | U                         | U                         | D                         |
| Level Transition Order                                             | U                         | U                         | D                         |
| Stop Shunting on desk opening                                      | U                         | U                         | U                         |
| List of balises for SH area                                        | D                         | D[9]                      | D[5]                      |
| MA Request Parameters                                              | U                         | U                         | U                         |
| Position Report parameters                                         | U                         | U                         | U                         |
| List of Balises in SR Authority + SR mode speed limit and distance | U[2]                      | U                         | D[5]                      |
| Temporary Speed Restrictions                                       | U                         | U                         | D                         |
| Inhibition of revocable TSRs from balises in L2/3                  | U                         | U                         | D                         |
| Default Gradient for TSR                                           | U[4]                      | U[4]                      | D                         |


---
<!-- pagina 224 -->

[¶2882]
|                                                 | Situations listed above   | Situations listed above   | Situations listed above   |
|-------------------------------------------------|---------------------------|---------------------------|---------------------------|
| Data Stored on-board                            | a - d, f, n               | e, g - j, l,m             | k                         |
| Signalling related Speed Restriction            | D[1]                      | D[10]                     | D[5]                      |
| Route Suitability Data                          | D[1]                      | D[10]                     | D                         |
| Plain Text Information (location based)         | D[8]                      | D[13]                     | D                         |
| Plain Text Information (not location based)     | U                         | U                         | D                         |
| Fixed Text Information (location based)         | D[8]                      | D[13]                     | D                         |
| Fixed Text Information (not location based)     | U                         | U                         | D                         |
| Geographical Position                           | U                         | U                         | U                         |
| Mode Profile                                    | D[1] [7] [14]             | D[10] [12]                | D[5]                      |
| RBC Transition Order                            | D[1]                      | D[10]                     | D                         |
| Radio Infill Area information                   | D[1]                      | D[10]                     | D                         |
| EOLM information                                | U                         | U                         | U                         |
| Track Conditions excluding big metal masses     | R[1]                      | R[10]                     | R                         |
| Track condition big metal masses                | R[1]                      | R[10]                     | R                         |
| Unconditional Emergency Stop                    | U                         | U                         | D                         |
| Conditional Emergency Stop                      | U                         | U                         | D                         |
| Train Position                                  | U                         | U                         | U                         |
| Train Data                                      | U                         | U                         | TBR                       |
| Adhesion factor                                 | U                         | U                         | D                         |
| ERTMS/ETCS level                                | U                         | U                         | U                         |
| Table of priority of trackside supported levels | U                         | U                         | U                         |
| Driver ID                                       | U                         | U                         | TBR                       |
| Radio Network ID                                | U                         | U                         | U                         |
| RBC ID/Phone Number                             | U                         | U                         | U                         |
| Train Running Number                            | U                         | U                         | TBR                       |
| Reversing Area Information                      | D[1]                      | D[10]                     | D                         |
| Reversing Supervision Information               | U                         | U                         | D                         |
| Track Ahead Free Request                        | U[6]                      | U                         | D                         |
| Level Crossing information                      | U                         | U                         | D                         |


---
<!-- pagina 225 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2883]

[¶2884]
|                                                    | Situations listed above   | Situations listed above   | Situations listed above   |
|----------------------------------------------------|---------------------------|---------------------------|---------------------------|
| Data Stored on-board                               | a - d, f, n               | e, g - j, l,m             | k                         |
| Permitted Braking Distance Information             | D[1]                      | D[10]                     | D                         |
| RBC/RIU System Version                             | U                         | U                         | U                         |
| Operated System Version                            | U                         | U                         | U                         |
| Language used to display information to the driver | U                         | U                         | U                         |
| Virtual Balise Covers                              | U                         | U                         | U                         |
| Generic LS function marker                         | U                         | U                         | U                         |
| LSSMA display toggle on order                      | U                         | U                         | D                         |

[1]: beyond the new SvL or in case of situation a, beyond the stop location of the accepted CES

- [2]:  The  considered  situations  cannot  occur  when  a  list  of  balises  to  be  used  in  SR  is  available  onboard. Indeed, the onboard is in SR mode and since no MA or track description are stored onboard, no new SvL may be defined. [¶2885]

- [3]: In case of reception of a new non-infill MA (situation b or f), the stored MA is fully replaced with the new one. In case of reception of a new infill MA (situation b), the stored MA is replaced beyond the infill location reference, i.e. the balise group at the next main signal [¶2886]

- [4]: The considered situations a-d, f, h, i cannot occur when the default gradient for a TSR is used on-board. [¶2887]

- [5]: The considered situation cannot occur because acceptance of this information has led to exit from SoM procedure. [¶2888]

- [6]: The considered situations b-d, f cannot occur when a TAF request is stored on-board [¶2889]

- [7]: If the start location of the Mode Profile is beyond the new SvL, the acknowledgement window of the Mode Profile shall be deleted as well [¶2890]

- [8]:  only  if  the  location  where  to  start  to  display  the  text  is  beyond  the  new  SvL;  otherwise  all  the  text information (i.e. including end location where to stop display, if any) shall remain unchanged [¶2891]

- [9]: unchanged if the onboard is in SH mode [¶2892]

- [10]: beyond the current max safe front end position of the train [¶2893]

- [11]:  the  ERTMS/ETCS on-board equipment shall consider the current estimated front end and max safe front end positions of the train, as the EOA and SvL respectively, with no release speed [¶2894]

- [12]: If the start location of the Mode Profile is beyond the current max safe front end, the acknowledgement window of the Mode Profile shall be deleted as well [¶2895]

- [13]: only if the location where to start to display the text is beyond the current max safe front end; otherwise all the text information (i.e. including end location where to stop display, if any) shall remain unchanged [¶2896]

- [14]: In case of reception of a new non-infill MA with or without Mode Profile (situation b or f), the stored Mode Profile is deleted. In case of reception of a new infill MA (situation b), the stored Mode Profile is deleted only beyond the infill location reference, i.e. the balise group at the next main signal [¶2897]

# A.3.4.1.4 NOTES: [¶2898]

- A.3.4.1.4.1 'Location' contains LRBG, distance travelled from LRBG, position of the front end in relation  to  the  LRBG,  the  confidence  interval  and  the  orientation  in  relation  to  the LRBG. [¶2899]


---
<!-- pagina 226 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2900]

- A.3.4.1.4.2 The following information is not considered to be stored information: [¶2901]

- Repositioning information [¶2902]

- Session Management (exception: the RBC ID/phone number, which is given with an order to establish a communication session, is stored on-board) [¶2903]

-  Danger for SH information [¶2904]

- Assignment of Co-ordinate system [¶2905]

- Infill Location Reference [¶2906]

-  Location Identity (NID_C + NID_BG transmitted in the balise telegram) [¶2907]

- Recognition of exit from TRIP mode [¶2908]

- Acknowledgement of Train Data [¶2909]

-  SH refused [¶2910]

-  SH authorised [¶2911]

-  Balise/loop system version [¶2912]

- Intentionally deleted

-  Intentionally deleted

- Revocation of Emergency Stop (Conditional or Unconditional) [¶2913]

- Temporary Speed Restriction Revocation [¶2914]

- Intentionally deleted

- Acknowledgement of session termination [¶2915]

-  Default Balise Information [¶2916]

-  Co-operative shortening of MA (if this message is used, it replaces the movement authority) [¶2917]

-  Train Rejected [¶2918]

- Train Accepted [¶2919]

-  SoM position report confirmed by RBC [¶2920]

- Track Ahead Free up to level 2/3 transition location [¶2921]

-  Signalling related speed restriction value zero (i.e., train trip order) [¶2922]

-  Stop if in SR mode [¶2923]

-  Data to be forwarded to a National System through the STM interface [¶2924]

- aa)  LSSMA display toggle off order [¶2925]


---
<!-- pagina 227 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2926]

# A.3.5 Handling of Actions in Specific Situations [¶2927]

- A.3.5.1 Regards actions executed in reference to location information received from trackside, the  on-board  equipment  shall  ensure  that  the  action  related  to  a  location  is  neither reverted,  nor  executed  twice.  Situations  to  be  considered  shall  include  reverse movement  (initiated  by  driver  or  due  to  roll-away)  and  the  sub-sequent  forward movement,  or  adjustment  of  train  position  on  passing  a  new  LRBG.  This  rule  shall apply to the following actions: [¶2928]

-  Change of National Values (see 3.18.2) [¶2929]

-  Request to acknowledge new level, level transition (see SRS chapter 5.10) [¶2930]

-  Start and stop displaying plain or fixed text messages (see 3.12.3) [¶2931]

-  Request to acknowledge a mode profile, mode transition due to mode profile (see 3.12.4) [¶2932]

-  Start and stop accepting radio infill information (see 3.9.3) [¶2933]

-  Actions related to RBC/RBC handover (see 3.15.1) [¶2934]

-  Actions related to track condition information (see 3.12.1) with the exception of big metal masses and non stopping areas [¶2935]

-  Permission to initiate Reversing mode, i.e., limits of Reversing Area (see 3.15.4) [¶2936]

-  Start and stop Track Ahead free request to driver (see 3.15.5) [¶2937]

-  Start and stop calculation of geographical position (see 3.6.6) [¶2938]

-  Substitute the supervision of the LX start location as the EOA/SvL by the inclusion of the LX speed restriction in the MRSP (see 5.16.2 and 5.16.3) [¶2939]

- A.3.5.2 Once  the  ERTMS/ETCS on-board equipment has received  a  balise  group  message (i.e.  once  it  has  received  the  last  balise  telegram  of  the  balise  group),  the  action(s) resulting from its content shall take into account the train position measured at the time of reception of this last telegram and shall take precedence on any other action related to a further location that is reached before the message has been fully processed. [¶2940]

- A.3.5.2.1 Example 1: in level 1, the crossing of the EOA/LOA location with the min safe antenna, before a new extended MA (received when the min safe antenna was in rear of the EOA/LOA)  has  been  processed,  will  not  lead  to  train  trip.  In  other  terms  the replacement of the EOA/LOA is considered by the on-board as happening before the min safe antenna crosses the EOA/LOA  location (i.e. preventing that clause 3.13.10.2.7 applies). [¶2941]

- A.3.5.2.2 Example 2: when the override function is active, the crossing of the former EOA/LOA location by the min safe antenna, before a 'Stop if in SR' information (received when the min safe antenna was in rear of the former EOA/LOA) has been processed, will not [¶2942]


---
<!-- pagina 228 -->

lead to the end of the override procedure followed by a train trip due to 'Stop if in SR'. In  other  terms,  both  the  deletion  of  the  former  EOA/LOA  and  the  end  of  override procedure (see 5.8.3.1.3 and 5.8.4.1 c)) are considered by the on-board as simultaneously happening before the min safe antenna crosses the former EOA/LOA location. [¶2943]

# A.3.6 Deletion of accepted and stored information when used [¶2944]

# A.3.6.1 Standard case [¶2945]

- A.3.6.1.1 When the train moves in the direction of its train orientation, storage capacity occupied by  trackside  information  no  longer  used,  i.e.,  the  related  on-board  functionality  has been completed, shall be made available immediately. [¶2946]

- A.3.6.1.1.1 Note:  The  requirement  is  needed  to  allow  trackside  to  predict  the  storage  capacity available  on-board  in  order  to  comply  with  dimensioning  rules  regards  information stored on-board given in Subset 040. [¶2947]

# A.3.6.2 Exception [¶2948]

- A.3.6.2.1 Following information shall remain stored on-board for a distance defined by a fixed value in rear of the min safe rear end position of the train: [¶2949]

-  location dependent static speed restrictions , i.e., SSP, ASP, TSR, LX SR, PBD SR (see 3.11.2.2) [¶2950]

-  gradient information, [¶2951]

-  reduced adhesion information received from trackside, [¶2952]

-  Track condition 'Big metal masses'. [¶2953]

- A.3.6.2.1.1 Note: The above information remains stored for the case of a reverse movement: [¶2954]

-  With  the  exception  of  the  track  condition  'Big  metal  masses',    the  stored information  allows  the  ERTMS/ETCS  on-board  equipment  to  calculate  speed supervision limits after a reverse movement (roll-away, or initiated by the driver) [¶2955]

-  Track condition 'Big metal masses' is needed also for a reverse movement itself to avoid any false alarms due to Big metal masses in the track. [¶2956]

- A.3.6.2.1.2 Note: The distance to intervention of the roll away or reverse movement supervision is determined by a National/Default value.  This is also true for a reverse movement in Post trip mode. However, following an intervention, the train will not stop immediately. In order to keep the on-board functionality simple, a fixed distance value was chosen to define an unambiguous location in rear of the train where the above information is no longer required and the related on-board storage capacity is made available again. [¶2957]


---
<!-- pagina 229 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2958]

# A.3.7 Calculation of the basic deceleration [¶2959]

- A.3.7.1 The brake percentage (λ) shall be converted into two different input parameters: [¶2960]

λo = λ for calculation of emergency brake deceleration (A_brake_emergency(V)) [¶2961]

λo = MIN (λ, 135) for calculation of service brake deceleration (A_brake_service(V)) [¶2962]

where λ is the brake percentage defined as part of Train Data. [¶2963]

- A.3.7.2 The calculation of the basic deceleration (A_basic(V)) shall use a common algorithm that will be used twice, once for the service brake and once for the emergency brake. [¶2964]

- A.3.7.3 The speed limit for the first step shall be calculated as V_lim = x * λo y . [¶2965]

V_lim is the speed limit for the first step in km/h [¶2966]

x = 16.85 [¶2967]

y = 0.428 [¶2968]

- A.3.7.4 The first step of the basic deceleration shall be calculated as AD_0 = A * λo + B [¶2969]

AD_0 is the basic deceleration in m/s 2  for 0 ≤ speed ≤ V_lim. [¶2970]

A = 0.0075 [¶2971]

B = 0.076 [¶2972]

- A.3.7.5 The following steps of the basic deceleration shall be calculated by means of a set of polynomials of the third order with the following format: [¶2973]

$$
A D _ { - } n = a 3 _ { - } n \, ^ { * } \, \lambda _ { o } ^ { 3 } + a 2 _ { - } n \, ^ { * } \, \lambda _ { o } \, ^ { 2 } + a 1 _ { - } n \, ^ { * } \, \lambda _ { o } + a 0 _ { - } n
$$ [¶2974]

and with the following values for n (all speed limits in km/h): [¶2975]

[¶2976]
| n = 1   | valid for V_lim < speed ≤ 100 to be ignored                 | if V_lim < 100 if V_lim ≥ 100       |
|---------|-------------------------------------------------------------|-------------------------------------|
| n = 2   | valid for V_lim < speed ≤ 120 valid for 100 < speed ≤ 120   | if 100 < V_lim < 120 if V_lim ≤ 100 |
| n = 3   | valid for V_lim < speed ≤ 150 valid for 120 < speed ≤ 150   | if 120 < V_lim < 150 if V_lim ≤ 120 |
| n = 4   | valid for V_lim < speed ≤ 180 valid for 150 < speed ≤ 180   | if 150 < V_lim < 180 if V_lim ≤ 150 |
| n = 5   | to be ignored valid for V_lim < speed valid for 180 < speed | if V_lim ≥ 180 if V_lim > 180       |
|         |                                                             | if V_lim ≤ 180                      |

- A.3.7.6 The coefficients for the polynomials shall be defined as follows: [¶2977]

[¶2978]
| am_n   |   m = |   m = |   m = |   m = |
|--------|-------|-------|-------|-------|
|        |     3 |     2 |     1 |     0 |


---
<!-- pagina 230 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶2979]

[¶2980]
| n =   |   1 |   -6.30E-07 |   6.10E-05 |   4.72E-03 |   0.0663 |
|-------|-----|-------------|------------|------------|----------|
| n =   |   2 |    2.73E-07 |  -4.54E-06 |   5.14E-03 |   0.1300 |
| n =   |   3 |    5.58E-08 |  -6.76E-06 |   5.81E-03 |   0.0479 |
| n =   |   4 |    3.00E-08 |  -3.85E-06 |   5.52E-03 |   0.0480 |
| n =   |   5 |    3.23E-09 |   1.66E-06 |   5.06E-03 |   0.0559 |

# A.3.8 Calculation of the emergency brake equivalent time [¶2981]

- A.3.8.1 The  basic  brake  build  up  time  for  the  emergency  brake  with  the  brake  position  in passenger trains in P shall be calculated as: [¶2982]

T_brake_basic_eb = a + b * (L/100) + c * (L/100) 2 [¶2983]

where [¶2984]

L = MAX (400m; train length in m) [¶2985]

a = 2.30 [¶2986]

b = 0.00 [¶2987]

c = 0.17 [¶2988]

- A.3.8.2 The  basic  brake  build  up  time  for  the  emergency  brake  with  the  brake  position  in freight trains in P shall be calculated as: [¶2989]

T_brake_basic_eb = a + b * (L/100) + c * (L/100) 2 [¶2990]

where [¶2991]

L = MAX (400m; train length in m) [¶2992]

If train length ≤ 900m: [¶2993]

a = 2.30 [¶2994]

b = 0.00 [¶2995]

c = 0.17 [¶2996]

If 900m < train length ≤ 1500m: [¶2997]

a = -0.40 [¶2998]

b = 1.60 [¶2999]

c = 0.03 [¶3000]

- A.3.8.3 The  basic  brake  build  up  time  for  the  emergency  brake  with  the  brake  position  in freight trains in G shall be calculated as: [¶3001]

T_brake_basic_eb = a + b * (L/100) + c * (L/100) 2 [¶3002]

where [¶3003]

L = train length in m [¶3004]

If train length ≤ 900m: [¶3005]

a = 12.00 [¶3006]

b = 0.00 [¶3007]


---
<!-- pagina 231 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3008]

c = 0.05 [¶3009]

If 900m < train length ≤ 1500m: [¶3010]

a = -0.40 [¶3011]

b = 1.60 [¶3012]

c = 0.03 [¶3013]

- A.3.8.4 The  equivalent  brake  build  up  time  for  the  emergency  brake  shall  be  computed  as follows: [¶3014]

T_brake_emergency_cm0 = T_brake_basic_eb when V_target = 0 [¶3015]

T_brake_emergency_cmt = kto * T_brake_basic_eb when V_target > 0 [¶3016]

where [¶3017]

V_target is the target speed [¶3018]

- A.3.8.5 The correction factor kto shall depend on the brake position as follows: [¶3019]

kto = 1 + Ct [¶3020]

where [¶3021]

Ct = 0.16 [¶3022]

for freight trains in G [¶3023]

Ct = 0.20 [¶3024]

for freight trains in P [¶3025]

Ct = 0.20 [¶3026]

for passenger trains [¶3027]

# A.3.9 Calculation of the full service brake equivalent time [¶3028]

- A.3.9.1 The basic brake build up time for full service brake for passenger trains in P shall be calculated as: [¶3029]

- A.3.9.2 The  basic  brake  build  up  time  for  full  service  brake  for  freight  trains  in  P  shall  be calculated as: [¶3030]

T_brake_basic_sb = a + b * (L/100) + c * (L/100) 2 [¶3031]

where [¶3032]

L = train length in m [¶3033]

a = 3.00 [¶3034]

b = 1.50 [¶3035]

c = 0.10 [¶3036]

T_brake_basic_sb = a + b * (L/100) + c * (L/100) 2 [¶3037]

where [¶3038]

L = train length in m [¶3039]

If train length ≤ 900m: [¶3040]

a = 3.00 [¶3041]

b = 2.77 [¶3042]

c = 0.00 [¶3043]


---
<!-- pagina 232 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3044]

If 900m < train length ≤ 1500m: [¶3045]

a = 10.50 [¶3046]

b = 0.32 [¶3047]

c = 0.18 [¶3048]

- A.3.9.3 The  basic  brake  build  up  time  for  full  service  brake  for  freight  trains  in  G  shall  be calculated as: [¶3049]

T_brake_basic_sb = a + b * (L/100) + c * (L/100) 2 [¶3050]

where [¶3051]

L = MAX (400m; train length in m) [¶3052]

If train length ≤ 900m: [¶3053]

a = 3.00 [¶3054]

b = 2.77 [¶3055]

c = 0.00 [¶3056]

If 900m < train length ≤ 1500m: [¶3057]

a = 10.50 [¶3058]

b = 0.32 [¶3059]

c = 0.18 [¶3060]

- A.3.9.4 The equivalent brake build up time for the service brake shall be computed as follows: [¶3061]

T_brake_service_cm0 = T_brake_basic_sb when V_target = 0 [¶3062]

T_brake_service_cmt = kto * T_brake_basic_sb when V_target > 0 [¶3063]

- A.3.9.5 The correction factor kto shall be defined as in A.3.8.5 [¶3064]

- A.3.9.6 The  values  of  a,  b,  c  and  kto  used  in  A.3.9.1,  A.3.9.2,  A.3.9.3  and  A.3.9.4  define reference  values  for  the  equivalent  brake  build  up  time  for  the  service  brake,  which shall be considered as maximum ones. If justified by the specific brake system of the train other values of these coefficients, which lead to shorter values of the equivalent brake build up time for the service brake, may be used. [¶3065]

- A.3.9.7 Note:  Although  certain  trains  may  perform  better,  the  reference  values  for  the equivalent  brake  build  up  time  for  the  service  brake,  as  defined  here,  are  the appropriate basis for infrastructure planning. [¶3066]

# A.3.10 Service brake feedback [¶3067]

- A.3.10.1 The purpose of service brake feedback is to reduce the distance between the SBI and EBI supervision limits and between the SBI and SBD curves. [¶3068]

- A.3.10.2 The on-board shall consider the service brake feedback as available for use if: [¶3069]

- The service brake feedback is implemented, AND [¶3070]

- The national value does not inhibit its use. [¶3071]


---
<!-- pagina 233 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3072]

- A.3.10.3 Two different types of feedback from the service brake are specified, main brake pipe pressure and brake cylinder pressure. The algorithms below are made for main brake pipe pressure. When brake cylinder pressure is used instead this shall be converted into a fictive main brake pressure value in the following way: [¶3073]

p = fictive main brake pipe pressure (kPa) [¶3074]

p_cylinder = brake cylinder pressure (kPa) [¶3075]

k1 = vehicle dependent constant (set by engineering of ETCS on-board; k1 is normally between 2.0 and 2.7) [¶3076]

p =  500  - p_cylinder / k1 [¶3077]

- A.3.10.4 The value of T_bs1 and T_bs2 shall be calculated according to the following algorithm to take the service brake feedback into account: [¶3078]

p = current main brake pipe pressure (or fictive main brake pipe pressure calculated in A.3.10.3) [¶3079]

p0 = reference pressure when not braking [¶3080]

p1 = pressure at which the train starts to brake = p0 - 30 [¶3081]

p2 = pressure limit, under which T_bs1 and T_bs2 are locked = p0 - 60 [¶3082]

p3 = pressure at full service brake = p0 - 150 [¶3083]

Q_feedback_active = a Boolean stating whether the feedback function is active, i.e. once it  has  started  to  reduce  T_bs1  and  T_bs2  until  the  ceiling  speed  monitoring  is entered. [¶3084]

Q_Tbslocked = a boolean stating whether T_bs1 and T_bs2 have been locked to the following values due to enough main brake pipe pressure reduction: [¶3085]

T_bs1_locked =  0 s. [¶3086]

T_bs2_locked =  2 s. [¶3087]

Q_displaylocked_P  =  a  boolean  stating  whether  the  displayed  permitted  speed  is locked due to SB feedback. [¶3088]

Q_displaylocked_SBI = a boolean stating whether the displayed SBI speed (if any) is locked due to SB feedback. [¶3089]

Q_displaylocked_TD  =  a  boolean  stating  whether  the  displayed  target  distance  is locked due to SB feedback. [¶3090]

A displayed value is locked from the moment the SB feedback has started to reduce T_bs1  and  T_bs2  until  the  calculated  value  becomes  less  than  the  displayed  and locked value. Note: It is only SB feedback that can start the locking of the displayed values.  Once  started  and  still  locked  it  remains  locked  also  in  case  the  calculated values are increased due to other reasons (e.g. due to relocation), which will prolong the locking period. [¶3091]

Initial values when the target speed monitoring is entered or when the release speed monitoring is entered not from target speed monitoring: [¶3092]

Tbs1_prev= Tbs [¶3093]


---
<!-- pagina 234 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3094]

```unknown
Q_feedback_active = false Q_displaylocked_P = false Q_displaylocked_SBI = false Q_displaylocked_TD = false Q_Tbslocked =false If on-board is in target speed monitoring or release speed monitoring then If Q_Tbslocked then T_bs1 = T_bs1_locked T_bs2 = T_bs2_locked Else If p > p2 then If Q_feedback_active or p ≤ p1 then Q_feedback_active = true T_bs_feedback = T_bs * (p - p3) / (p0 - p3) T_bs1 = T_bs2 = T_bs_feedback If T_bs_feedback > T_bs then T_bs1 = T_bs2 = T_bs Else if T_bs_feedback < T_bs2_locked then T_bs2 = T_bs2_locked End If Else T_bs1 = T_bs T_bs2 = T_bs End If Else T_bs1 = T_bs1_locked T_bs2 = T_bs2_locked Q_feedback_active = true Q_Tbslocked = true End If End If Else T_bs1 = T_bs T_bs2 = T_bs End if If Q_feedback_active and T_bs1 < T_bs1_prev then
``` [¶3095]


---
<!-- pagina 235 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3096]

Q_displaylocked_P = true [¶3097]

Q_displaylocked_SBI = true [¶3098]

Q_displaylocked_TD = true [¶3099]

End If [¶3100]

T_bs1_prev = T_bs1 [¶3101]

If Q_displaylocked_P and the permitted speed computed for display purposes (VP-DMI) as per clause 3.13.10.4.3 is less than the locked and displayed permitted speed, then [¶3102]

Q_displaylocked_P = false [¶3103]

End If [¶3104]

If Q_displaylocked_SBI and the SBI speed computed for display purposes (VSBI-DMI) as per clause 3.13.10.4.4 is less than the locked and displayed SBI speed, then [¶3105]

Q_displaylocked_SBI = false [¶3106]

End If [¶3107]

If  Q_displaylocked_TD and the target distance computed for display purposes as per clause 3.13.10.4.7 is less than the locked and displayed target distance, then [¶3108]

Q_displaylocked_TD = false [¶3109]

End If [¶3110]

If the MRDT changes then [¶3111]

Q_displaylocked_P = false [¶3112]

Q_displaylocked_SBI = false [¶3113]

Q_displaylocked_TD = false [¶3114]

End If [¶3115]

![](images/image_0078.png)


---
<!-- pagina 236 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3116]

The reference pressure p0 (nominal value 500 kPa) shall be set on starting the ETCS: [¶3117]

- To the first stable p value between 400-550 kPa achieved. [¶3118]

- Stable in this instance means that the pressure has not varied more than ± 20 kPa over 3 seconds. [¶3119]

The reference pressure p0 shall thereafter be adapted to the current pressure according to the following table (which applies if the calculation is performed once per second): [¶3120]

[¶3121]
|    | CONDITIONS:     | ACTION:       | REMARKS             |
|----|-----------------|---------------|---------------------|
| a) | p = p0          | No change     | Constant pressure   |
| b) | p > p0          | p0 = p0 + 1,5 | Increasing pressure |
| c) | p < p0 - 30     | No change     | Braking             |
| d) | p0 > p > p0- 30 | p0 = p0  0,5 | Decreasing pressure |

# Where: [¶3122]

- -p is limited to max 550 kPa. [¶3123]

- -Values given in kPa. [¶3124]

- A.3.10.5 Note: If T_bs1 and T_bs2 have been locked to 0s and 2 s on approaching a non zero target, the locking will remain even if the train speed comes below the target speed. This  avoids  'jumping'  indications  related  to  the  values  of  T_bs1  and  T_bs2.  It  also makes it possible to release the brakes before a speed reduction, without having the curves moving back again. It might though result in emergency brake intervention if the driver releases the brakes too early. But since EBI is not moved, this is not a safety issue. To keep 2 s between the SBI and EBI enables the service brake to be activated first and thus may avoid emergency brake. [¶3125]

- A.3.10.6 Note: If feedback is active but T_bs1 and T_bs2 are not locked, the feedback function will  remain active until the ceiling speed monitoring is entered. This avoids 'jumping' indications in some rare situations. [¶3126]

# A.3.11 Data unit, range and resolution [¶3127]

[¶3128]
| Data                         | Unit   | Range   | Resolution   |
|------------------------------|--------|---------|--------------|
| Train Data: Train length     | m      | 0-4095  | 1 m          |
| Train Data: Brake percentage | %      | 10-250  | 1%           |
| Train Data: Maximum train    | km/h   | 0-600   | 5 km/h       |


---
<!-- pagina 237 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3129]

[¶3130]
| speed                                         |      |                                                                              |        |
|-----------------------------------------------|------|------------------------------------------------------------------------------|--------|
| Train Data: Loading gauge                     | n/a  | G1, GA, GB, GC, does not fit any of the interoperable loading gauge profiles | n/a    |
| Train Data: Axle load category                | n/a  | A, HS17, B1, B2, C2, C3, C4, D2, D3, D4, D4XL, E4, E5                        | n/a    |
| Train Data: Train fitted with airtight system | n/a  | Yes, No                                                                      | n/a    |
| Driver ID                                     | n/a  | 1 to 16 alphanumeric characters (selected from 0 to 9 and a to z)            | n/a    |
| RBC ID                                        | n/a  | 0-16777214                                                                   | 1      |
| RBC phone number                              | n/a  | no restriction                                                               | n/a    |
| Train running number                          | n/a  | no restriction                                                               | n/a    |
| Distance to run in SR mode                    | m    | 0-100000                                                                     | 1 m    |
| Maximum SR speed                              | km/h | 0-600                                                                        | 5 km/h |


---
<!-- pagina 238 -->

# ERTMS/ETCS [¶3131]

# System Requirements Specification Chapter 4 Modes and Transitions [¶3132]

REF : [¶3133]

SUBSET-026-4 [¶3134]

ISSUE : [¶3135]

3.6.0 [¶3136]

DATE  : [¶3137]

13/05/2016 [¶3138]


---
<!-- pagina 239 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3139]

# 4.1 Modification History [¶3140]

[¶3141]
| Issue Number Date      | Section Number                     | Modification / Description                                                                      | Author         |
|------------------------|------------------------------------|-------------------------------------------------------------------------------------------------|----------------|
| Issue 0.0.1 1999-07-05 | /                                  | This document is based on 'SRS Class P - Modes and Transitions' issue 1.1.2 (ref. Subset-006-4) | Laffineur J.C. |
| Issue 0.0.2 1999-07-16 | /                                  | New modes/functions/transitions due to Class 1 scope, and impact from WPs (of 1999- 07-13).     | Laffineur J.C. |
| Issue 0.1.0 1999-07-23 | /                                  | Unisig Review - Stockholm - 22 & 23 July 1999                                                   | Laffineur J.C. |
| 1.0.0 1999-07-29       | Version number, editorial changes. | Finalisation meeting, Stuttgart 990729.                                                         | HE             |
| 1.2.0 990730           | Version number                     | Release version                                                                                 | HE             |
| 1.3.0 991209           | /                                  | Modifications due to Work Packages on SRS Class 1 v 1.0.0                                       | Laffineur J.C. |
| 1.4.0 991220           | /                                  | Modifications due to review meeting in Stockholm (991215 and 991216)                            | Laffineur J.C. |
| 1.4.1 991221           | /                                  | Presentation changes                                                                            | Laffineur J.C. |
| 2.0.0 991222           | Minor editing                      | Release version                                                                                 | Laffineur J.C. |
| 2.0.1                  | All                                | Modifications respect to Unisig review (doc. Unisig_all_com_SRS_2.0.0 _2)                       | Laffineur J.C. |
| 2.1.0                  | All                                | Modifications respect to Unisig review (doc. Unisig_all_com_SRS_2.0.1)                          | Laffineur J.C. |
| 2.2.0                  | Version number                     | UNISIG release                                                                                  | SAB            |


---
<!-- pagina 240 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3142]

[¶3143]
| 2.2.2 02 02 01            | /                                                                                                                                                                                       | SUBSET-026 Corrected Paragraphs, Issue 2.2.2                                                                                                                                            | Laffineur J.C.   |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| 2.2.4                     | Including all CLRs being in state 'EEIG' as per list of CLRs agreed by EEIG on 06/05/04.                                                                                                | Including all CLRs being in state 'EEIG' as per list of CLRs agreed by EEIG on 06/05/04.                                                                                                | Hougardy A.      |
| 2.2.4 SG checked 28/05/04 | Including all CLRs agreed with the EEIG (see 'List of CLRs agreed with EEIG for SRS v2.2.4' dated 28/05/04)                                                                             | Including all CLRs agreed with the EEIG (see 'List of CLRs agreed with EEIG for SRS v2.2.4' dated 28/05/04)                                                                             | H. Kast          |
| 2.2.5 21/01/05            | Incorporation of solution proposal for CLR 007 with EEIG users group comments Corrections according to erratum list agreed in SG meeting 170105                                         | Incorporation of solution proposal for CLR 007 with EEIG users group comments Corrections according to erratum list agreed in SG meeting 170105                                         | Hougardy A.      |
| 2.2.6 04/02/05            | Including all CLRs being in state 'EEIG pending' as per list of CLRs extracted on 28/01/05.                                                                                             | Including all CLRs being in state 'EEIG pending' as per list of CLRs extracted on 28/01/05.                                                                                             | Hougardy A.      |
| 2.2.7 16/06/05            | Including all CLRs extracted from "CR- Report_10.6.05-by number.rtf" and mentioned in column 2.2.7 in "CR status 13.6.05.xls"                                                           | Including all CLRs extracted from "CR- Report_10.6.05-by number.rtf" and mentioned in column 2.2.7 in "CR status 13.6.05.xls"                                                           | Hougardy A.      |
| 2.2.8 29/11/05            | Change marks cleaned up and updated according to last CRs decisions (including split of CRs7&126)                                                                                       | Change marks cleaned up and updated according to last CRs decisions (including split of CRs7&126)                                                                                       | Hougardy A.      |
| 2.2.9 24/02/06            | Including all CRs that are classified as "IN" as per SUBSET-108 version 1.0.0 Removal of all CRs that are not classified as "IN" as per SUBSET-108 version 1.0.0, with the exception of | Including all CRs that are classified as "IN" as per SUBSET-108 version 1.0.0 Removal of all CRs that are not classified as "IN" as per SUBSET-108 version 1.0.0, with the exception of | Hougardy A.      |
| 2.3.0 24/02/06            | Release version                                                                                                                                                                         | Release version                                                                                                                                                                         | HK               |
| 2.3.1 15/06/06            | Including SG CR decision made since SRS 2.2.8, correct errors in 2.2.8 detected when creating SRS 2.3.0                                                                                 | Including SG CR decision made since SRS 2.2.8, correct errors in 2.2.8 detected when creating SRS 2.3.0                                                                                 | Hougardy A.      |
| 2.3.2 17/03/08            | Including all CRs that are classified as "IN" as per SUBSET-108 version 1.2.0 and all CRs that are in state 'Analysis completed' according to ERA CCM                                   | Including all CRs that are classified as "IN" as per SUBSET-108 version 1.2.0 and all CRs that are in state 'Analysis completed' according to ERA CCM                                   | Hougardy A.      |


---
<!-- pagina 241 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3144]

[¶3145]
| 2.9.1 06/10/08   | Including all enhancement CR's retained for 3.0.0 baseline and all other error CR's that are in state 'Analysis completed' according to ERA CCM For editorial reasons, the following CR's are also included: CR656, CR804, CR821   | Hougardy A.   |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| 3.0.0 23/12/08   | Release version                                                                                                                                                                                                                    | Hougardy A.   |
| 3.0.1 22/12/09   | Including the results of the editorial review of the SRS 3.0.0 and the other error CR's that are in state 'Analysis completed' according to ERA CCM                                                                                | Hougardy A.   |
| 3.1.0 22/02/10   | Release version                                                                                                                                                                                                                    | Hougardy A.   |
| 3.1.1 08/11/10   | Including all CR's that are in state 'Analysis completed' according to ERA CCM, plus CR972 and 1000.                                                                                                                               | Hougardy A.   |
| 3.2.0 22/12/10   | Release version                                                                                                                                                                                                                    | Hougardy A.   |
| 3.2.1 13/12/11   | Including all CR's that are in state 'Analysis completed' according to ERA CCM, plus CR772                                                                                                                                         | Hougardy A.   |
| 3.3.0 07/03/12   | Baseline 3 release version                                                                                                                                                                                                         | Hougardy A.   |
| 3.3.1 04/04/14   | CR's 944, 1124, 1176, 1183, 1185                                                                                                                                                                                                   | Gemine O.     |
| 3.3.2 23/04/14   | Baseline 3 1 st maintenance pre-release version                                                                                                                                                                                    | Gemine O.     |
| 3.3.3 06/05/14   | CR 1223 Baseline 3 1 st maintenance 2 nd pre-release version                                                                                                                                                                       | Gemine O.     |
| 3.4.0 12/05/14   | Baseline 3 1 st maintenance release version                                                                                                                                                                                        | Gemine O.     |
| 3.4.1 23/06/15   | CR's 1033, 1094                                                                                                                                                                                                                    | Gemine O.     |
| 3.4.2 17/11/15   | CR's 539, 740, 933, 1087, 1089, 1091, 1107, 1128, 1187, 1190, 1197, 1249, 1262, 1265, 1266                                                                                                                                         | Gemine O.     |
| 3.4.3 16/12/15   | 1128 removed, 1117, 1283 plus update due to overall CR consolation phase                                                                                                                                                           | Gemine O.     |
| 3.5.0 18/12/15   | Baseline 3 2 nd release version as recommended to EC (see ERA-REC-123-2015/REC)                                                                                                                                                    | Gemine O.     |


---
<!-- pagina 242 -->

[¶3146]
| 3.5.1 28/04/16   | CR 1249 reopening following RISC #75   | Gemine O.   |
|------------------|----------------------------------------|-------------|
| 3.6.0            | Baseline 3 2 nd release version        | Hougardy A. |


---
<!-- pagina 243 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3147]

# 4.2 Table of Contents [¶3148]

| 4.1                                                                                                                                      | 4.1                                                                                                                                      | Modification History...........................................................................................................2                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4.2 Table                                                                                                                                | 4.2 Table                                                                                                                                | of Contents..............................................................................................................6                                                                                                            |
| 4.3 Introduction.......................................................................................................................8 | 4.3 Introduction.......................................................................................................................8 |                                                                                                                                                                                                                                       |
| 4.3.1 Presentation                                                                                                                       | 4.3.1 Presentation                                                                                                                       | of the document ....................................................................................8                                                                                                                                 |
| 4.3.2 Identification of                                                                                                                  | 4.3.2 Identification of                                                                                                                  | the possible modes...........................................................................8                                                                                                                                        |
| 4.4.1                                                                                                                                    | 4.4.1                                                                                                                                    | Introduction..............................................................................................................10                                                                                                          |
| 4.4.2                                                                                                                                    | 4.4.2                                                                                                                                    | General Requirements.............................................................................................10                                                                                                                   |
| 4.4.3                                                                                                                                    | 4.4.3                                                                                                                                    | ISOLATION..............................................................................................................11                                                                                                             |
| 4.4.4                                                                                                                                    | 4.4.4                                                                                                                                    | NO POWER.............................................................................................................12                                                                                                               |
| 4.4.5 SYSTEM                                                                                                                             | 4.4.5 SYSTEM                                                                                                                             |                                                                                                                                                                                                                                       |
| 4.4.6                                                                                                                                    | 4.4.6                                                                                                                                    | FAILURE..................................................................................................13 SLEEPING...............................................................................................................14 |
| 4.4.7 STAND                                                                                                                              | 4.4.7 STAND                                                                                                                              | BY...............................................................................................................16                                                                                                                   |
| 4.4.8                                                                                                                                    | 4.4.8                                                                                                                                    | SHUNTING..............................................................................................................17                                                                                                              |
| 4.4.9 FULL                                                                                                                               | 4.4.9 FULL                                                                                                                               | SUPERVISION...............................................................................................19                                                                                                                          |
| 4.4.10                                                                                                                                   | 4.4.10                                                                                                                                   | UNFITTED...............................................................................................................20                                                                                                             |
| 4.4.11                                                                                                                                   | 4.4.11                                                                                                                                   | STAFF RESPONSIBLE ...........................................................................................21                                                                                                                       |
| 4.4.12 ON                                                                                                                                | 4.4.12 ON                                                                                                                                | SIGHT ...............................................................................................................24                                                                                                               |
| 4.4.13                                                                                                                                   | 4.4.13                                                                                                                                   | TRIP ........................................................................................................................25                                                                                                       |
| 4.4.14                                                                                                                                   | 4.4.14                                                                                                                                   | POST TRIP..............................................................................................................26                                                                                                             |
| 4.4.15 NON                                                                                                                               | 4.4.15 NON                                                                                                                               | LEADING........................................................................................................28                                                                                                                     |
| 4.4.16 Intentionally                                                                                                                     | 4.4.16 Intentionally                                                                                                                     | deleted .................................................................................................30                                                                                                                           |
| 4.4.17 National System                                                                                                                   | 4.4.17 National System                                                                                                                   | (SN) mode.....................................................................................31                                                                                                                                      |
| 4.4.18                                                                                                                                   | 4.4.18                                                                                                                                   | REVERSING............................................................................................................32                                                                                                               |
| 4.4.19 LIMITED                                                                                                                           | 4.4.19 LIMITED                                                                                                                           | SUPERVISION .........................................................................................34                                                                                                                               |
| 4.4.20 PASSIVE SHUNTING..............................................................................................37                  | 4.4.20 PASSIVE SHUNTING..............................................................................................37                  |                                                                                                                                                                                                                                       |
| 4.5 Modes and on-board functions........................................................................................39               | 4.5 Modes and on-board functions........................................................................................39               | 4.5 Modes and on-board functions........................................................................................39                                                                                                            |
| 4.5.1                                                                                                                                    | 4.5.1                                                                                                                                    | Introduction..............................................................................................................39                                                                                                          |
| 4.5.2                                                                                                                                    | 4.5.2                                                                                                                                    | Active Functions Table.............................................................................................39                                                                                                                 |
| 4.6                                                                                                                                      | Transitions between modes ............................................................................................44                 | Transitions between modes ............................................................................................44                                                                                                              |
| 4.6.1                                                                                                                                    | 4.6.1                                                                                                                                    | Symbols...................................................................................................................44                                                                                                          |
| 4.6.2                                                                                                                                    | 4.6.2                                                                                                                                    | Transitions Table .....................................................................................................45                                                                                                             |
| 4.6.3                                                                                                                                    | 4.6.3                                                                                                                                    | Transitions Conditions Table....................................................................................46                                                                                                                    |
| 4.7.1                                                                                                                                    | DMI depending on modes...............................................................................................50                  | DMI depending on modes...............................................................................................50                                                                                                               |
|                                                                                                                                          | Introduction..............................................................................................................50             | Introduction..............................................................................................................50                                                                                                          | [¶3149]


---
<!-- pagina 244 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3150]

| 4.7.2                                                                                                                                      | 4.7.2                                                                                                                                      | DMI versus Mode Table...........................................................................................50                         |
|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 4.8                                                                                                                                        | Acceptance of received information ................................................................................55                      | Acceptance of received information ................................................................................55                      |
| 4.8.1                                                                                                                                      | 4.8.1                                                                                                                                      | Introduction..............................................................................................................55               |
| 4.8.2                                                                                                                                      | 4.8.2                                                                                                                                      | Assumptions ............................................................................................................57                 |
| 4.8.3                                                                                                                                      | 4.8.3                                                                                                                                      | Accepted information depending on the level and transmission media ....................58                                                  |
| 4.8.4                                                                                                                                      | 4.8.4                                                                                                                                      | Accepted Information depending on the modes.......................................................64                                       |
| 4.8.5                                                                                                                                      | 4.8.5                                                                                                                                      | Handling of transition buffer in case of level transition announcement or RBC/RBC                                                          |
| handover................................................................................................................................68 | handover................................................................................................................................68 | handover................................................................................................................................68 |
| 4.9                                                                                                                                        | What happens to accepted and stored information when entering a given level .............70                                                | What happens to accepted and stored information when entering a given level .............70                                                |
| 4.9.1                                                                                                                                      | 4.9.1                                                                                                                                      | Introduction..............................................................................................................70               |
| 4.10                                                                                                                                       | 4.10                                                                                                                                       | What happens to accepted and stored information when entering a given mode........71                                                       |
| 4.10.1                                                                                                                                     | 4.10.1                                                                                                                                     | Introduction..............................................................................................................71               |
| 4.11                                                                                                                                       | What happens to stored information when exiting NP mode .......................................75                                          | What happens to stored information when exiting NP mode .......................................75                                          | [¶3151]


---
<!-- pagina 245 -->

# 4.3 Introduction [¶3152]

# 4.3.1 Presentation of the document [¶3153]

- 4.3.1.1 This  document  defines  the  modes  of  the  ERTMS/ETCS  on-board  equipment  (see chapter 4.4 'Definition of the modes' and chapter 4.5 'Modes and on-board functions'. [¶3154]

- 4.3.1.2 This  document  gives  all  transitions  between  modes  (see  chapter  4.6  'Transitions between modes'). [¶3155]

- 4.3.1.3 This document describes the possible exchanged information between the driver and the  ERTMS/ETCS on-board equipment, respect  to  the  mode  (see  chapter  4.7  'DMI depending on modes'). [¶3156]

- 4.3.1.4 This  document  describes  how the received information is filtered,  respect  to  several criteria  such  as  the  level,  the  mode,  etc..  (see  chapter  4.8  'Acceptance  of  received information'). [¶3157]

- 4.3.1.5 This  document  describes  how  the  stored  information  is  handled,  respect  to  several criteria such as the level, the mode, etc. (see chapter 4.9 'What happens to accepted and stored information when entering a given level', and chapter 4.10 'What happens to accepted and stored information when entering a given mode'). [¶3158]

- 4.3.1.6 All  the  tables  that  are  included  in  this  document  shall  be  considered  as  mandatory requirements. [¶3159]

- 4.3.1.7 Some  notes  appear  in  this  document.  These  notes  are  here  to  help  the  reader  to understand the specifications, or to explain the reason(s) of a requirement. [¶3160]

# 4.3.2 Identification of the possible modes [¶3161]

# 4.3.2.1 List of the modes: [¶3162]

[¶3163]
| Full Supervision    | (FS)   |
|---------------------|--------|
| Limited Supervision | (LS)   |
| On Sight            | (OS)   |
| Staff Responsible   | (SR)   |
| Shunting            | (SH)   |
| Unfitted            | (UN)   |
| Passive Shunting    | (PS)   |
| Sleeping            | (SL)   |
| Stand By            | (SB)   |
| Trip                | (TR)   |


---
<!-- pagina 246 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3164]

[¶3165]
| Post Trip       | (PT)   |
|-----------------|--------|
| System Failure  | (SF)   |
| Isolation       | (IS)   |
| No Power        | (NP)   |
| Non Leading     | (NL)   |
| National System | (SN)   |
| Reversing       | (RV)   |


---
<!-- pagina 247 -->

# 4.4 Definition of the modes [¶3166]

# 4.4.1 Introduction [¶3167]

- 4.4.1.1 For each mode the following information is given: [¶3168]

- The context of utilisation of the mode and the functions that characterise the mode (chapter 'Description'). [¶3169]

- The  ERTMS/ETCS  levels  in  which  the  mode  can  be  used  (chapter  'Used  in levels'). [¶3170]

- The  related  responsibility  of  the  ERTMS/ETCS  on-board  equipment  and  of  the driver, once the equipment is in this mode (chapter 'Responsibilities'). [¶3171]

- 4.4.1.2 A  complete  list  of  transitions  to  and  from  each  mode  is  given  in  the  section  4.6.2 'Transitions Table' ). [¶3172]

# 4.4.2 General Requirements [¶3173]

- 4.4.2.1 When the desk is open, a clear indication of the ERTMS/ETCS mode shall be shown to the driver. [¶3174]

- 4.4.2.2 Intentionally deleted. [¶3175]


---
<!-- pagina 248 -->

# 4.4.3 ISOLATION [¶3176]

# 4.4.3.1 Description [¶3177]

- 4.4.3.1.1 In Isolation mode, the ERTMS/ETCS on-board equipment shall be physically isolated from  the  brakes  and  can  be  isolated  from  other  on-board  equipments/systems depending on the specific on-board implementation. [¶3178]

- 4.4.3.1.2 There  shall  be  a  clear  indication  to  the  driver  that  the  ERTMS/ETCS  on-board equipment is isolated. [¶3179]

- 4.4.3.1.3 To leave Isolation mode, a special operating procedure is needed (no transition from Isolation is specified). This procedure shall ensure that the on-board equipment is only put back into service when it has been proven that this is safe for operation. [¶3180]

- 4.4.3.1.4 Note: for the list  of  main  functions  related  to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3181]

# 4.4.3.2 Used in levels [¶3182]

- 4.4.3.2.1 Used in all levels: Level 0, level 1, level 2, level 3 and level NTC. [¶3183]

# 4.4.3.3 Responsibilities [¶3184]

- 4.4.3.3.1 Isolation of the ERTMS/ETCS on-board equipment is performed by the driver under his complete responsibility. [¶3185]

- 4.4.3.3.2 Once the ERTMS/ETCS on-board equipment is isolated, the ERTMS/ETCS on-board equipment has no more responsibility. [¶3186]


---
<!-- pagina 249 -->

# 4.4.4 NO POWER [¶3187]

# 4.4.4.1 Description [¶3188]

- 4.4.4.1.1 When the ERTMS/ETCS on-board equipment is not powered, the equipment is in the No Power mode. [¶3189]

- 4.4.4.1.1.1 Note:  in  order  to  ensure  cold  movement  detection  function,  some  parts  of  the ERTMS/ETCS on-board equipment may be fed by an auxiliary power supply. [¶3190]

- 4.4.4.1.2 The ERTMS/ETCS on-board equipment shall permanently command the emergency brake. [¶3191]

- 4.4.4.1.3 Note: for the list  of  main  functions  related  to this mode, refer to chapter  4.5 'Modes and on-board functions'. [¶3192]

# 4.4.4.2 Used in levels [¶3193]

- 4.4.4.2.1 Used in all levels: Level 0, level 1, level 2, level 3 and level NTC. [¶3194]

# 4.4.4.3 Responsibilities [¶3195]

- 4.4.4.3.1 The  ERTMS/ETCS  on-board  equipment  has  no  responsibility  in  this  mode,  except commanding the emergency brake and (optionally) monitoring cold movements. [¶3196]

- 4.4.4.3.2 The notion of responsibility of the driver is not relevant for the No Power mode. [¶3197]

- 4.4.4.3.3 If it is required to move a loco in NP mode as a wagon, ETCS brake command must be overridden by external means. [¶3198]


---
<!-- pagina 250 -->

# 4.4.5 SYSTEM FAILURE [¶3199]

# 4.4.5.1 Description [¶3200]

- 4.4.5.1.1 The  ERTMS/ETCS on-board  equipment  shall  switch  to  the  System  Failure  mode  in case of a fault, which affects safety. [¶3201]

- 4.4.5.1.2 The ERTMS/ETCS on-board equipment shall permanently command the Emergency Brakes. [¶3202]

- 4.4.5.1.3 Note: for the list  of  main  functions  related  to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3203]

# 4.4.5.2 Used in levels [¶3204]

- 4.4.5.2.1 Used in all levels: Level 0, level 1, level 2, level 3 and level NTC. [¶3205]

# 4.4.5.3 Responsibilities [¶3206]

- 4.4.5.3.1 The ERTMS/ETCS on-board equipment is responsible for commanding the Emergency Brakes. [¶3207]

- 4.4.5.3.2 No responsibility of the driver. [¶3208]


---
<!-- pagina 251 -->

# 4.4.6 SLEEPING [¶3209]

# 4.4.6.1 Description [¶3210]

- 4.4.6.1.1 The Sleeping mode is defined to manage the ERTMS/ETCS on-board equipment of a slave engine that is remote controlled. [¶3211]

- 4.4.6.1.2 The  desk(s)  of  a  sleeping  engine  must  be  closed  (since  there  is  no  driver,  no information shall be shown). [¶3212]

- 4.4.6.1.3 As the engine is remote controlled by the leading engine, its ERTMS/ETCS on-board equipment shall not perform any train movement supervision. [¶3213]

- 4.4.6.1.4 The  ERTMS/ETCS on-board equipment shall perform the Train Position function; in particular, the front/rear end of the engine (i.e., not the train) shall be used to refer to train front/rear end. [¶3214]

- 4.4.6.1.5 Sleeping mode shall be automatically detected on-board via the train interface. [¶3215]

- 4.4.6.1.6 If  possible,  the  train  must  not  be  stopped  due  to  a  safety  critical  fault  in  a  sleeping engine. The ERTMS/ETCS on-board equipment should therefore try to memorise the occurrence  of  such  fault(s),  which  should  be  handled  when  the  engine  leaves  the Sleeping  mode.  The  ERTMS/ETCS  on-board  equipment  should  also  try  to  send  an error information to the RBC. [¶3216]

- 4.4.6.1.7 If  a  desk  of  the  sleeping  engine  is  opened  while  the  train  is  running  (this  is  an abnormal operation), the ERTMS/ETCS on-board equipment shall switch to Stand-By mode. [¶3217]

- 4.4.6.1.8 If  the  'sleeping  input  signal'  is  lost  (no  more  detection  of  the  remote  control),  the switch to Stand-By mode shall be made only if the train is at standstill. [¶3218]

- 4.4.6.1.9 Intentionally deleted. [¶3219]

- 4.4.6.1.10  The ERTMS/ETCS on-board equipment shall open a communication session with the RBC when at least one of the following events occurs: [¶3220]

- in all levels, on receipt of the order to contact the RBC. [¶3221]

- In level 2/3, when entering or exiting Sleeping mode (to report the change of mode to the RBC). [¶3222]

-  In  level  2/3,  when  a  safety  critical  fault  of  the  ERTMS/ETCS  on-board  equipment occurs (to report the fault to the RBC). [¶3223]

- 4.4.6.1.11  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3224]

- 4.4.6.1.12  In case of balise group message consistency error (refer to 3.16.2.4.4 and 3.16.2.5.1), the ERTMS/ETCS onboard equipment shall not command the service brake. [¶3225]


---
<!-- pagina 252 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3226]

- 4.4.6.1.13  When in levels 2 or 3, if no compatible version has been established between the onboard  equipment  in  Sleeping  mode  and  the  RBC,  the  ERTMS/ETCS  onboard equipment shall react as specified in 3.5.3.7 d) 2 nd  bullet but no driver's indication shall be given. [¶3227]

# 4.4.6.2 Used in levels [¶3228]

- 4.4.6.2.1 Used in all levels: Level 0, level 1, level 2, level 3 and level NTC. [¶3229]

# 4.4.6.3 Responsibilities [¶3230]

- 4.4.6.3.1 The  ERTMS/ETCS  on-board  equipment  of  an  engine  in  Sleeping  mode  has  no responsibility for the train protection. [¶3231]

- 4.4.6.3.2 The notion of responsibility of the driver is not relevant for the Sleeping mode. [¶3232]

- 4.4.6.3.2.1 Note : The leading engine is responsible for the movement of the train. It is then the ERTMS/ETCS  on-board  equipment  of  the  leading  engine  that  is  fully/partially/not responsible for the train protection, with respect to its mode. [¶3233]


---
<!-- pagina 253 -->

# 4.4.7 STAND BY [¶3234]

# 4.4.7.1 Description [¶3235]

- 4.4.7.1.1 The Stand-By mode is a default mode and cannot be selected by the driver. [¶3236]

- 4.4.7.1.2 It is in the Stand-By mode that the ERTMS/ETCS on-board equipment awakes. [¶3237]

- 4.4.7.1.3 Data  for  mission  are  collected  in  Stand-By  (see  SRS-chapter  5:  'Start  of  Mission' procedure). [¶3238]

- 4.4.7.1.4 In Stand-By mode, the desk of the engine can be open or closed. No interaction with the  driver  shall  be  possible  as  long  as  the  desk  is  closed,  except  isolation  of  the ERTMS/ETCS on-board equipment. [¶3239]

- 4.4.7.1.5 The ERTMS/ETCS on-board equipment shall perform the Standstill Supervision. [¶3240]

- 4.4.7.1.6 Note: for the list  of  main  functions  related  to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3241]

# 4.4.7.2 Used in levels [¶3242]

- 4.4.7.2.1 Used in all levels: Level 0, level 1, level 2, level 3 and level NTC. [¶3243]

# 4.4.7.3 Responsibilities [¶3244]

- 4.4.7.3.1 The  ERTMS/ETCS  on-board  equipment  is  responsible  for  maintaining  the  train  at standstill. [¶3245]

- 4.4.7.3.2 The driver has no responsibility for train movements. [¶3246]


---
<!-- pagina 254 -->

# 4.4.8 SHUNTING [¶3247]

# 4.4.8.1 Description [¶3248]

- 4.4.8.1.1 The  purpose  of  the  Shunting  mode  is  to  enable  shunting  movements.  In  Shunting mode,  The  ERTMS/ETCS  on-board  equipment  shall  supervise  the  train  movements against: [¶3249]

- a ceiling speed: the shunting mode speed limit [¶3250]

- a list of expected balise groups (if such list was sent by the trackside equipment). The  train  shall  be  tripped  if  a  balise  group,  not  contained  in  the  list,  is  passed (When an empty list is sent, no balise group can be passed. When no list is sent, all balise groups can be passed) [¶3251]

- 'stop  if  in  shunting  mode'  information.  The  train  is  tripped  if  such  information  is received from balise groups [¶3252]

- Intentionally deleted

- 4.4.8.1.2 The Shunting mode shall not require Train Data. [¶3253]

- 4.4.8.1.3 The ERTMS/ETCS on-board equipment shall perform the Train Position function [¶3254]

- 4.4.8.1.4 Intentionally deleted. [¶3255]

- 4.4.8.1.5 When  in  Shunting  mode,  the  ERTMS/ETCS  on-board  shall  not  manage  level transitions. However,  an  immediate  level  transition  order  or  a conditional level transition order shall be stored and evaluated only when another mode than Shunting or Passive  Shunting has  been  entered  (i.e.  when  the  Shunting  movement  is terminated). [¶3256]

- 4.4.8.1.5.1 When receiving a communication session establishment order, the ERTMS/ETCS onboard in Shunting mode shall not establish the communication session, but shall store the RBC ID/phone number. [¶3257]

- 4.4.8.1.5.2 When  in  Shunting  mode,  the  ERTMS/ETCS  on-board  shall  not  manage  RBC-RBC hand-over, except for storing the RBC ID/phone number given at the RBC/RBC border. [¶3258]

- 4.4.8.1.6 Shunting  mode  can  be  selected  by  the  driver,  only  accepted  when  the  train  is  at standstill, or ordered by the trackside. [¶3259]

- 4.4.8.1.7 In case of selection of Shunting mode by the driver: [¶3260]

-  in  level  1  operations,  the  switch  to  shunting  is  always  accepted  by  the  on-board equipment [¶3261]

-  in  level  2  and  3  areas,  the  on-board  asks  the  trackside  for  an  authorisation.  The switch to shunting is possible only after receiving such authorisation. The trackside can send a list of balises, that the train is allowed to pass while in SH, together with the authorisation [¶3262]


---
<!-- pagina 255 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3263]

- 4.4.8.1.8 In case of order to switch to Shunting mode from trackside, the order: [¶3264]

-  in level 1 is given by a balise group. A list of balises, that the train is allowed to pass after the entry in Shunting, can be sent together with the order [¶3265]

-  in level 2 and 3 is sent via radio. A list of balises, that the train is allowed to pass after the entry in Shunting, can be sent together with the order [¶3266]

- 4.4.8.1.9 When  the  switch  to  shunting  is  ordered  by  trackside,  a  driver  acknowledgement  is requested. [¶3267]

- 4.4.8.1.9.1 Note: in Shunting mode the train is only partially supervised, therefore it is necessary that the driver takes the responsibility. [¶3268]

- 4.4.8.1.10  The  ERTMS/ETCS  on-board  equipment  shall  display  the  train  speed  and,  only  on driver request, the permitted speed. The display of the permitted speed shall also be stopped on driver request. [¶3269]

- 4.4.8.1.11  Intentionally deleted. [¶3270]

- 4.4.8.1.12  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3271]

# 4.4.8.2 Used in levels [¶3272]

- 4.4.8.2.1 Used in level 0, NTC, 1, 2 and 3. [¶3273]

# 4.4.8.3 Responsibilities [¶3274]

- 4.4.8.3.1 The  ERTMS/ETCS  on-board  equipment  is  responsible  for  the  supervision  of  the shunting mode speed limit, and that the engine with the active antenna is tripped when passing  the  defined  border  of  the  shunting  area  (only  if  there  is  a  defined  border: balise  group  not  in  the  list  given  by  trackside,  or  balise  group  giving  the  information 'stop if in shunting'). [¶3275]

- 4.4.8.3.2 The driver is responsible for : [¶3276]

- Remaining inside the shunting area defined by a procedure or an external system outside ERTMS/ETCS (also when the shunting area is protected by balises) [¶3277]

- Train/engine movements and shunting operations [¶3278]


---
<!-- pagina 256 -->

# 4.4.9 FULL SUPERVISION [¶3279]

# 4.4.9.1 Description [¶3280]

- 4.4.9.1.1 The ERTMS/ETCS on-board equipment shall be in the Full Supervision mode when all train  and  track  data,  which  is  required  for  a  complete  supervision  of  the  train,  is available on board. [¶3281]

- 4.4.9.1.2 Full supervision cannot be selected by the driver, but is entered automatically when all necessary conditions are fulfilled. [¶3282]

- 4.4.9.1.3 To  be  in  Full  Supervision  mode,  SSP  and  gradient  are  not  required  for  the  whole length of the train, but must be available at least from the FRONT END of the train. [¶3283]

- 4.4.9.1.4 Once in Full Supervision mode, if SSP and gradient are not known for the whole length of the train, an indication 'ENTRY IN FULL SUPERVISION' shall be clearly displayed to the driver until SSP and gradient are known for the whole length of the train. [¶3284]

- 4.4.9.1.4.1 Note: this indication may also be displayed in case the train length has been increased, see 3.18.3.8. [¶3285]

- 4.4.9.1.5 The  ERTMS/ETCS  on-board  equipment  shall  supervise  train  movements  against  a dynamic speed profile. [¶3286]

- 4.4.9.1.6 The  ERTMS/ETCS  on-board  equipment  shall  display  the  train  speed,  the  permitted speed, the target distance and the target speed to the driver (this list is not exhaustive - refer to chapter 4.7 'DMI depending on modes'). [¶3287]

- 4.4.9.1.7 Note: for the list  of  main  functions  related  to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3288]

# 4.4.9.2 Used in levels [¶3289]

- 4.4.9.2.1 Used in level 1, 2 and 3. [¶3290]

# 4.4.9.3 Responsibilities [¶3291]

- 4.4.9.3.1 The  ERTMS/ETCS  on-board  equipment  is  fully  responsible  for  the  train  protection (except for the 2 situations described below). [¶3292]

- 4.4.9.3.2 The  driver  is  responsible  for  respecting  the  EOA  when  approaching  an  EOA  with  a release speed. [¶3293]

- 4.4.9.3.3 When  'ENTRY  IN  FULL  SUPERVISION'  is  displayed  to  the  driver,  the  driver  is responsible for respecting speed restrictions that apply for the part of the train that is not covered by SSP and gradient data. [¶3294]


---
<!-- pagina 257 -->

# 4.4.10 UNFITTED [¶3295]

# 4.4.10.1 Description [¶3296]

- 4.4.10.1.1  The Unfitted mode is used to allow train movements in either: [¶3297]

-  Areas that are equipped neither with ERTMS/ETCS track-side equipment nor with national train control system [¶3298]

- Intentionally deleted

- Areas that  are  equipped  with  ERTMS/ETCS trackside equipment and/or  national train  control  system(s),  but  operation  under  their  supervision  is  currently  not possible [¶3299]

- 4.4.10.1.2  The  ERTMS/ETCS  on-board  equipment  shall  supervise  train  movements  against  a ceiling  speed:  the  lowest  of  the  maximum  train  speed  and  the  Unfitted  mode  speed limit for unfitted area (national value). [¶3300]

- 4.4.10.1.2.1 Intentionally deleted. [¶3301]

- 4.4.10.1.3  The ERTMS/ETCS  on-board  equipment  shall also supervise temporary speed restrictions. [¶3302]

- 4.4.10.1.4  The ERTMS/ETCS on-board equipment shall display the train speed to the driver. [¶3303]

- 4.4.10.1.5  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3304]

# 4.4.10.2 Used in levels [¶3305]

- 4.4.10.2.1  Used in level 0. [¶3306]

# 4.4.10.3 Responsibilities [¶3307]

- 4.4.10.3.1  The ERTMS/ETCS on-board equipment supervises a ceiling speed and (if available) temporary speed restrictions. [¶3308]

- 4.4.10.3.2  The driver must respect the existing line-side signals and is fully responsible for train movements. [¶3309]


---
<!-- pagina 258 -->

# 4.4.11 STAFF RESPONSIBLE [¶3310]

# 4.4.11.1 Description [¶3311]

- 4.4.11.1.1  The  Staff  Responsible  mode  allows  the  driver  to  move  the  train  under  his  own responsibility in an ERTMS/ETCS equipped area. [¶3312]

- 4.4.11.1.2  This mode is used when the system does not know the route. For example: [¶3313]

- After the ERTMS/ETCS on-board equipment starts-up (awakening of the train). [¶3314]

- To pass a signal at danger / override an EOA. [¶3315]

-  After a trackside failure (for example: loss of radio contact). [¶3316]

- 4.4.11.1.3  The ERTMS/ETCS on-board equipment shall supervise train movements against : [¶3317]

- a ceiling speed: the staff responsible mode speed limit [¶3318]

- a given distance (regarding its origin location see 4.4.11.1.3.1). The ERTMS/ETCS on-board equipment shall supervise braking curves with a target speed of zero to the end of this distance. If the train overpasses this distance (see next note) the ERTMS/ETCS on-board equipment shall trip the train [¶3319]

- a  list  of  expected  balise  groups,  if  this  list  has  been  sent  by  the  RBC.  The  train shall  be  tripped  if  over-passing  a  balise  group  that  is  not  in  the  list.  (When  an empty list is sent, no balise group can be passed. When no list is sent, all balise groups can be passed) [¶3320]

- balise groups giving the order 'stop if in SR'. This order shall immediately trip the train, unless the over-passed balise group is included in a list of expected balises as defined in item c) [¶3321]

- running  in  the  direction  opposite  to  the  train  orientation  (reverse  movement protection) [¶3322]

- 4.4.11.1.3.1 The ERTMS/ETCS on-board shall determine the start location of the SR distance as follows: [¶3323]

- If  the  National/Default value determines the max permitted distance to run in SR mode, the starting point of this distance shall refer to the estimated position of the train  front  when  SR  mode  was  entered,  or,  already  in  Staff  Responsible  mode, when Override was activated. [¶3324]

- If  the  max  permitted  distance  to  run  in  SR  mode  is  determined  by  the  value transmitted by the RBC, or entered by the driver, the start location of the distance shall refer to the estimated position of the train front when the distance information is received or entered. [¶3325]

- If  the  max  permitted  distance  to  run  in  SR  mode  is  determined  by  the  value transmitted by EUROLOOP, the distance information transmitted by EUROLOOP shall be referred to one or more reference balise groups. On-board shall evaluate [¶3326]


---
<!-- pagina 259 -->

the distance to run in SR mode by matching the reference balise groups given with the LRBG. [¶3327]

In case the LRBG is, due to a change of orientation, in front of the train when the distance to run in SR mode is to be determined from the EUROLOOP information, the  complete  distance  to  run  in  SR  mode  shall  be  determined  as  the  distance given by EUROLOOP plus the distance between the estimated train front end and the LRBG. [¶3328]

- 4.4.11.1.4  Note:  Since  the  gradient  is  unknown,  the  supervision  of  the  braking  curves  in  Staff Responsible mode does not ensure that the train will not pass the given distance. [¶3329]

- 4.4.11.1.5  The ERTMS/ETCS on-board equipment shall give the possibility to the driver to modify the value of the SR mode speed limit and of the given distance. This shall be possible only at standstill. [¶3330]

- 4.4.11.1.5.1 If a train movement is detected while the driver is entering the SR speed/distance limits, the ERTMS/ETCS on-board equipment shall trigger the brake command. [¶3331]

- 4.4.11.1.5.2 The unit, range and resolution of the SR mode speed limit and distance entered by the driver shall be as specified in A.3.11. [¶3332]

- 4.4.11.1.6  If  the  level  is  2/3  and  a  communication  session  is  open,  the  driver  shall  have  the possibility to request a new distance to run in Staff Responsible, by selecting "Start". This triggers an MA request. [¶3333]

- 4.4.11.1.6.1 Note: Once the SR distance is covered, the driver may have to go further. [¶3334]

- 4.4.11.1.6.2 When entering SR mode, the value applicable for SR mode speed limit and the value applicable for  SR  distance  shall  be  the  corresponding  National/Default  values. Exception for SR distance: SR mode is authorised by RBC giving an SR distance. [¶3335]

- 4.4.11.1.6.3 While in SR mode, the value applicable for the SR mode speed limit shall be, if available, the last value entered by the driver. [¶3336]

- 4.4.11.1.6.4 While in SR mode, the value applicable for the SR distance shall be, if available, the last value received by the ERTMS/ETCS on-board equipment amongst: [¶3337]

- the distance to run in SR entered by the driver; [¶3338]

- the distance to run in SR given by trackside. [¶3339]

- 4.4.11.1.6.5 When "Override" is selected, the SR mode speed limit value and the SR distance value previously entered by driver or given by trackside, if any, shall be deleted. The corresponding National/Default values shall enter in force. [¶3340]

- 4.4.11.1.6.6 If  the  train  is  in  SR  and  receives  a  new  distance  to  run  in  SR  mode  from  the RBC,  the  stored  list  of  expected  balise  groups,  if  any,  shall  be  deleted  or  shall  be replaced by the list of expected balise groups sent together with the distance to run in SR. [¶3341]


---
<!-- pagina 260 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3342]

- 4.4.11.1.6.7 If an ERTMS/ETCS on-board equipment in SR mode, after having received from EUROLOOP max permitted distance to run in SR mode information, detects the main signal  balise  group  being  part  of  this  information  then  it  shall  ignore  any  new  max permitted distance to run in SR mode information from that loop. [¶3343]

- 4.4.11.1.7  The  ERTMS/ETCS on-board equipment shall display the train speed and the (when active)  override  (permission to pass a signal at danger, trip inhibited). The permitted speed, target distance and the target speed shall be displayed only on driver request, until the driver requests to stop their display. [¶3344]

- 4.4.11.1.8  Intentionally deleted. [¶3345]

- 4.4.11.1.9  If  receiving  a  "track  ahead  free"  request  from  the  RBC,  the  ERTMS/ETCS on-board equipment requests the driver to enter the "track ahead free" information. [¶3346]

- 4.4.11.1.10  Note: for  the  list  of  main  functions  related  to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3347]

- 4.4.11.1.11  Intentionally deleted. [¶3348]

# 4.4.11.2 Used in levels [¶3349]

- 4.4.11.2.1  Level 1, 2 and 3. [¶3350]

# 4.4.11.3 Responsibilities [¶3351]

- 4.4.11.3.1  The ERTMS/ETCS on-board equipment supervises a ceiling speed, a SR distance if finite and, if available, a list of balises. [¶3352]

- 4.4.11.3.2  The driver must check if the track is free, if points are correctly positioned, and must respect the existing line-side information (signals, speed boards etc.). [¶3353]

- 4.4.11.3.3  When using the possibility to modify the value of the SR mode speed limit and of the given distance, the driver is responsible for entering reasonable values. [¶3354]


---
<!-- pagina 261 -->

# 4.4.12 ON SIGHT [¶3355]

# 4.4.12.1 Description [¶3356]

- 4.4.12.1.1  The On Sight mode enables the train to enter into a track section that could be already occupied by another train, or obstructed by any kind of obstacle. [¶3357]

- 4.4.12.1.2  On  Sight  mode  cannot  be  selected  by  the  driver,  but  shall  be  entered  automatically when commanded by trackside and all necessary conditions are fulfilled. [¶3358]

- 4.4.12.1.3  The  ERTMS/ETCS  on-board  equipment  shall  supervise  train  movements  against  a dynamic speed profile. [¶3359]

- 4.4.12.1.4  The ERTMS/ETCS on-board equipment shall display the train speed to the driver. The permitted  speed,  target  distance,  target  speed  and  release  speed  (if  any)  shall  be displayed only on driver request, until the driver requests to stop their display (this list is not exhaustive - refer to chapter 4.7 'DMI depending on modes'). [¶3360]

- 4.4.12.1.5  If  receiving  a  "track  ahead  free"  request  from  the  RBC,  the  ERTMS/ETCS on-board equipment requests the driver to enter the "track ahead free" information. [¶3361]

- 4.4.12.1.6  To be in On Sight mode, SSP and gradient are not required for the whole length of the train, but must be available at least from the FRONT END of the train. [¶3362]

- 4.4.12.1.7  Once in On Sight mode, if SSP and gradient are not known for the whole length of the train, an indication 'ENTRY IN ON SIGHT' shall be clearly displayed to the driver until SSP and gradient are known for the whole length of the train. [¶3363]

- 4.4.12.1.7.1 Note:  this  indication  may  also  be  displayed  in  case  the  train  length  has  been increased, see 3.18.3.8. [¶3364]

- 4.4.12.1.8  Deleted [¶3365]

- 4.4.12.1.9  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3366]

# 4.4.12.2 Used in levels [¶3367]

- 4.4.12.2.1  Used in level 1, 2 and 3. [¶3368]

# 4.4.12.3 Responsibilities [¶3369]

- 4.4.12.3.1  The ERTMS/ETCS on-board equipment is responsible for the supervision of the train movements. [¶3370]

- 4.4.12.3.2  The  driver  is  responsible  for  checking  the  track  occupancy  when  moving  the  train, because the track may be occupied. [¶3371]


---
<!-- pagina 262 -->

# 4.4.13 TRIP [¶3372]

# 4.4.13.1 Description [¶3373]

- 4.4.13.1.1  Deleted [¶3374]

- 4.4.13.1.1.1 Note: Application of emergency brakes and train trip are two different things. For example, exceeding the permitted speed leads to application of the emergency brakes, but as long as the train does not pass the EOA/LOA, it is not a train trip. [¶3375]

- 4.4.13.1.2  The  ERTMS/ETCS  on-board  equipment  shall  command  the  emergency  brakes  (no brake release is possible in Trip mode). [¶3376]

- 4.4.13.1.3  The ERTMS/ETCS on-board equipment shall indicate to the driver the reason of the train trip. [¶3377]

- 4.4.13.1.4  The ERTMS/ETCS on-board equipment shall request an acknowledgement from the driver once train is at standstill (to allow the driver to acknowledge the train trip). [¶3378]

- 4.4.13.1.4.1 Note: This acknowledgement is mandatory to exit from Trip mode. [¶3379]

- 4.4.13.1.5  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3380]

- 4.4.13.1.6  Closing  the  desk  while  being  in  Trip  mode  will  not  cause  a  mode  change  but  no interaction  with  the  driver  shall  be  possible  as  long  as  the  desk  is  closed,  except isolation of the ERTMS/ETCS on-board equipment [¶3381]

# 4.4.13.2 Used in levels [¶3382]

- 4.4.13.2.1  Used in level 0, NTC, 1, 2 and 3. [¶3383]

# 4.4.13.3 Responsibilities [¶3384]

- 4.4.13.3.1  The  ERTMS/ETCS on-board equipment is responsible for stopping the train and for maintaining the train at standstill. [¶3385]

- 4.4.13.3.2  The driver has no responsibility for train movements. [¶3386]


---
<!-- pagina 263 -->

# 4.4.14 POST TRIP [¶3387]

# 4.4.14.1 Description [¶3388]

- 4.4.14.1.1  The Post Trip mode shall be entered immediately after the driver acknowledges the trip. [¶3389]

- 4.4.14.1.2  Once  in  post  trip  mode,  the  onboard  equipment  shall  release  the  Command  of  the emergency brake. [¶3390]

- 4.4.14.1.2.1 The ERTMS/ETCS on-board equipment shall keep on indicating to the driver the reason of the train trip. [¶3391]

- 4.4.14.1.3  The train shall only be authorised to move backwards a given distance (national value). The  ERTMS/ETCS  on-board  equipment  shall  supervise  this  national  distance  for reverse  movements,  and  shall  command  the  service  brakes  if  the  distance  is  overpassed. The driver shall be informed about the reason for the brake application. [¶3392]

- 4.4.14.1.3.1 Note:  The  ERTMS/ETCS onboard equipment performs the Reverse Movement Protection (as in PT mode, the "normally allowed movement" is backwards, then the Reverse Movement Protection avoids the train running in forward direction when in PT mode). This implies that the given distance to run backwards in PT is considered as a directional data, oriented backwards. [¶3393]

- 4.4.14.1.3.2 After  the  release  of  a  brake  command initiated due to an overpassed distance allowed  for  moving  backwards  in  Post  Trip  mode,  the  ERTMS/ETCS  on-board equipment shall command the service brake for any further movement in the direction opposite to the train orientation. [¶3394]

- 4.4.14.1.4  When moving backwards in Post Trip mode, the train trip shall be inhibited. [¶3395]

- 4.4.14.1.5  Intentionally deleted. [¶3396]

- 4.4.14.1.6  When  ERTMS/ETCS  level  is  1,  if  the  driver  selects  'Start'  the  onboard  equipment proposes Staff Responsible. When ERTMS/ETCS level is 2 or 3, the selection of Start leads  to  an  MA  Request  to  the  RBC.  It  is  the  RBC  responsibility  to  give  an  SR authorisation, or a Full Supervision MA  or an On  Sight/Shunting MA  to an ERTMS/ETCS equipment that is in Post Trip mode. [¶3397]

- 4.4.14.1.7  Intentionally deleted. [¶3398]

- 4.4.14.1.8  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3399]

- 4.4.14.1.9  In case of balise group message consistency error (refer to 3.16.2.4.4 and 3.16.2.5.1), the ERTMS/ETCS onboard equipment shall not command the service brake. [¶3400]

# 4.4.14.2 Used in levels [¶3401]


---
<!-- pagina 264 -->

- 4.4.14.2.1  Used in level 1, 2 and 3. [¶3402]

# 4.4.14.3 Responsibilities [¶3403]

- 4.4.14.3.1  The  ERTMS/ETCS  on-board  equipment  is  responsible  for  supervising  that  the  train moves  only  backwards  and  that  the  backward  movement  does  not  exceed  the maximum permitted distance (national value). [¶3404]

- 4.4.14.3.2  The driver is responsible if moving the train backwards. [¶3405]


---
<!-- pagina 265 -->

# 4.4.15 NON LEADING [¶3406]

# 4.4.15.1 Description [¶3407]

- 4.4.15.1.1  The Non-Leading mode is defined to manage the ERTMS/ETCS on-board equipment of a slave engine that is NOT electrically coupled to the leading engine (and so, not remote controlled) but has its own driver. [¶3408]

- 4.4.15.1.1.1 Note: This operating situation is called Tandem. [¶3409]

- 4.4.15.1.1.2 The ERTMS/ETCS on-board equipment shall use, as a necessary condition to enter in Non-Leading mode, a 'non leading input signal" from the train interface. [¶3410]

- 4.4.15.1.1.3 If  the  'non  leading  input  signal"  is  no  longer  present,  the  switch  to  Stand-By mode shall be made only if the train is at standstill. [¶3411]

- 4.4.15.1.2  The  ERTMS/ETCS  on-board  equipment  shall  not  perform  any  train  movement supervision in Non-Leading mode. [¶3412]

- 4.4.15.1.3  The  ERTMS/ETCS  on-board  equipment  shall  perform  the  Train  Position  function;  in particular, the front/rear end of the engine (i.e., not the train) shall be used to refer to train front/rear end. [¶3413]

- 4.4.15.1.4  When level is 2 or 3, the ERTMS/ETCS on-board equipment shall report its position to the RBC, according to the previously received parameters. [¶3414]

- 4.4.15.1.5  If possible, the train must not be stopped due to a safety critical fault in a non-leading engine. The ERTMS/ETCS on-board equipment should therefore try to memorise the occurrence  of  such  fault(s),  which  should  be  handled  when  the  engine  leaves  Non Leading  mode.  The  ERTMS/ETCS  on-board  equipment  should  also  try  to  send  an error information to the RBC. [¶3415]

- 4.4.15.1.6  The ERTMS/ETCS on-board equipment shall display the train speed to the driver. [¶3416]

- 4.4.15.1.7  Intentionally deleted

- 4.4.15.1.8  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3417]

- 4.4.15.1.9  The supervision of linking consistency shall not be performed in Non Leading mode. [¶3418]

- 4.4.15.1.10  In case of balise group message consistency error (refer to 3.16.2.4.4 and 3.16.2.5.1), the ERTMS/ETCS onboard equipment shall not command the service brake. [¶3419]

# 4.4.15.2 Used in levels [¶3420]

- 4.4.15.2.1  Used in all levels: Level 0, level 1, level 2, level 3 and level NTC. [¶3421]


---
<!-- pagina 266 -->

# 4.4.15.3 Responsibilities [¶3422]

- 4.4.15.3.1  The  ERTMS/ETCS  on-board  equipment  performs  NO  protection  functions,  except forwarding track conditions associated orders through DMI or train interface. [¶3423]

- 4.4.15.3.2  The driver is responsible for obeying the orders associated to track conditions, when they are displayed by the DMI. [¶3424]


---
<!-- pagina 267 -->

# 4.4.16 Intentionally deleted


---
<!-- pagina 268 -->

# 4.4.17 National System (SN) mode [¶3425]

# 4.4.17.1 Description [¶3426]

- 4.4.17.1.1  In SN mode, according to the specific on-board implementation, the National System may access the following resources via the ERTMS/ETCS on-board equipment: DMI, Juridical  Recording  interface,  odometer,  train  interface  and  brakes.  This  can  be achieved through the STM interface. [¶3427]

- 4.4.17.1.2  A limited set of data coming from balises shall be used by the ERTMS/ETCS on-board equipment, refer to SRS chapter 4.8 'Use of received information'. [¶3428]

- 4.4.17.1.3  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3429]

# 4.4.17.2 Used in levels [¶3430]

- 4.4.17.2.1  Level NTC. [¶3431]

# 4.4.17.3 Responsibilities of ERTMS/ETCS Onboard [¶3432]

- 4.4.17.3.1  No train supervision functionality is provided by the ERTMS/ETCS  on-board equipment. In case the ERTMS/ETCS on-board equipment is interfaced to the National System  through  an  STM,  refer  to  the  FFFIS  STM  (Subset  035)  for  the  functionality provided by ERTMS/ETCS on-board. [¶3433]

- 4.4.17.3.2  Intentionally deleted. [¶3434]

# 4.4.17.4 Responsibilities of the National System [¶3435]

- 4.4.17.4.1  The National System is responsible for all train supervision and protection functions. [¶3436]

- 4.4.17.4.2  The National System is responsible for issuing and revoking brake command. [¶3437]

- 4.4.17.4.3  The  National  System  is  responsible  for  maintaining  national  system  behaviour  and interact with national trackside equipment. [¶3438]

- 4.4.17.4.4  The National System is responsible for interaction with the driver. [¶3439]

# 4.4.17.5 Responsibilities of the driver [¶3440]

- 4.4.17.5.1  The responsibility of the driver depends on the National System in use. [¶3441]


---
<!-- pagina 269 -->

# 4.4.18 REVERSING [¶3442]

# 4.4.18.1 Description [¶3443]

- 4.4.18.1.1  The Reversing mode allows the driver to change the direction of movement of the train and  drive  from  the  same  cab,  i.e.  the  train  orientation  remains  unchanged.  This  is possible only in areas so marked by trackside. [¶3444]

- 4.4.18.1.2  Note: This mode is used to allow the train to escape from a dangerous situation and to reach as fast as possible a 'safer' location. [¶3445]

- 4.4.18.1.3  The ERTMS/ETCS on-board equipment shall supervise train movements against : [¶3446]

- a ceiling speed: the Reversing mode speed limit given from trackside [¶3447]

- a  distance  to  run  in  the  direction  opposite  to  the  train  orientation,  given  from trackside. The emergency brake shall be commanded if overpassing this distance [¶3448]

- 4.4.18.1.4  After  the  release  of  a  brake  command  initiated  due  to  an  overpassed  reversing distance, and while the reversing distance is still overpassed, the ERTMS/ETCS onboard equipment shall command the emergency brake for any further movement in the direction opposite to the train orientation. [¶3449]

- 4.4.18.1.5  The  ERTMS/ETCS  on-board  equipment  shall  display  the  train  speed,  the  permitted speed and the remaining distance to run. [¶3450]

- 4.4.18.1.6  In  case  the  SBI  supervision  limit  is  exceeded  (refer  to  chapter  3  table  5,  triggering condition  t4),  the  ERTMS/ETCS on-board equipment shall command the emergency brake instead of the service brake. For the revocation of the brake command, refer to 3.13.10.2.4. [¶3451]

- 4.4.18.1.7  The  position  reports  sent  when  in  reversing  mode  shall  refer  to  the  location  of  the driving cab (as before reversing). [¶3452]

- 4.4.18.1.8  Note:  The  ERTMS/ETCS  onboard  equipment  performs  the  Reverse  Movement Protection (as in RV mode, the "normally allowed movement" is backwards, then the Reverse Movement Protection avoids the train running in forward direction when in RV mode).  This  implies  that  the  given  distance  to  run  in  reversing  is  considered  as  a directional data, oriented backwards. [¶3453]

- 4.4.18.1.9  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'. [¶3454]

- 4.4.18.1.10  In case of balise group message consistency error (refer to 3.16.2.4.4 and 3.16.2.5.1), the ERTMS/ETCS onboard equipment shall not command the service brake. [¶3455]

- 4.4.18.1.11  In case there is an alarm reporting a malfunction for the onboard balise transmission function, the ERTMS/ETCS onboard equipment shall ignore this alarm. [¶3456]


---
<!-- pagina 270 -->

- 4.4.18.1.12  In  case  the  ERTMS/ETCS  system  version  number  X  transmitted  by  any  balise  is greater  than  the  highest  version  X  supported  by  the  onboard  equipment  (refer  to 3.17.3.5), the information from this balise shall be ignored, the train shall not be tripped and the driver shall not be informed. [¶3457]

# 4.4.18.2 Used in levels [¶3458]

- 4.4.18.2.1  Level 1, 2, 3. [¶3459]

# 4.4.18.3 Responsibilities [¶3460]

- 4.4.18.3.1  The ERTMS/ETCS on-board equipment supervises a ceiling speed and a distance to run in reverse direction. [¶3461]

- 4.4.18.3.2  The driver must keep the train movement inside the received distance to run. [¶3462]


---
<!-- pagina 271 -->

# 4.4.19 LIMITED SUPERVISION [¶3463]

# 4.4.19.1 Description [¶3464]

- 4.4.19.1.1  The  Limited  Supervision  mode  enables  the  train  to  be  operated  in  areas  where trackside information can be supplied to realise background supervision of the train. [¶3465]

- 4.4.19.1.2  Limited supervision can not be selected by the driver, but shall be entered automatically when commanded by trackside and all necessary conditions are fulfilled. [¶3466]

- 4.4.19.1.3  The  ERTMS/ETCS  on-board  equipment  shall  supervise  train  movements  against  a dynamic speed profile. [¶3467]

- 4.4.19.1.4  The ERTMS/ETCS on-board equipment shall display the train speed and the release speed,  if  any  (this  list  is  not  exhaustive  -  refer  to  chapter  4.7  'DMI  depending  on modes'). Upon request by trackside (refer to clauses 4.4.19.1.4.2 to 4.4.19.1.4.6) if the generic LS  function marker  is stored on-board  or if the conditions in clause 4.4.19.1.4.7 are fulfilled, the ERTMS/ETCS on-board equipment shall also display the lowest speed amongst: [¶3468]

- the lowest MRSP element between the minimum safe front end of the train and the EOA/LOA, AND [¶3469]

- the target speed at the EOA/LOA [¶3470]

- 4.4.19.1.4.1 The speed resulting from 4.4.19.1.4 a) and b) is called the Lowest Supervised Speed within the Movement Authority (LSSMA) [¶3471]

- 4.4.19.1.4.2 Upon  an  order  to  toggle  on  the  LSSMA  display,  the  ERTMS/ETCS  on-board equipment shall start a delay timer: [¶3472]

- For order received from RBC/RIU: at the value of the time stamp of the message including the order. [¶3473]

- For  order  received  from  balise  group:  at  the  time  of  passage  over  the  first encountered balise of the balise group giving the order. [¶3474]

-  Exception to a) and b): for order that has been stored in the level transition buffer (see section 4.8.3): at the time the level transition is performed. [¶3475]

- 4.4.19.1.4.3 When the delay timer value becomes greater than the time-out value given by trackside, the ERTMS/ETCS on-board equipment shall display the LSSMA. [¶3476]

- 4.4.19.1.4.4 On reception of an order to toggle (on or off) the LSSMA display, a toggle on order  which  has  not  been  executed  yet  (because  the  on-board  delay  timer  has  not reached the delay time-out value) shall be deleted by the on-board equipment. [¶3477]

- 4.4.19.1.4.5 If  the  LSSMA  display  is  already  toggled  on,  the  ERTMS/ETCS  on-board equipment shall toggle off the LSSMA display in case: [¶3478]


---
<!-- pagina 272 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3479]

- the clause 4.4.19.1.4.3 is not immediately fulfilled upon reception of a new order to toggle on the LSSMA display [¶3480]

- an order to toggle off the LSSMA display is received. [¶3481]

- 4.4.19.1.4.6 When  entering  the  Limited  Supervision  mode,  the  LSSMA  display  shall  be toggled  off  by  the  ERTMS/ETCS  on-board  equipment,  unless  a  toggle  on  order  is received  and  leads  immediately  to  the  display  of  the  LSSMA  as  per  clauses 4.4.19.1.4.2 and 4.4.19.1.4.3. [¶3482]

- 4.4.19.1.4.7 If the generic LS function marker is not stored on-board, the clauses 4.4.19.1.4.2 to 4.4.19.1.4.6 shall not apply and the LSSMA shall be displayed if: [¶3483]

- the target speed at the EOA/LOA is lower than the Limited Supervision mode speed limit, AND [¶3484]

- the LSSMA is lower than the maximum train speed. [¶3485]

- 4.4.19.1.4.8 The generic LS function marker shall be deleted by the ERTMS/ETCS on-board equipment as soon as a Limited Supervision mode profile is received without it in the same balise group message. [¶3486]

- 4.4.19.1.5  If  receiving  a  "track  ahead  free"  request  from  the  RBC,  the  ERTMS/ETCS on-board equipment requests the driver to enter the "track ahead free" information. [¶3487]

- 4.4.19.1.6  To be in Limited Supervision mode, SSP and gradient are not required for the whole length of the train, but shall be at least available from the FRONT END of the train. [¶3488]

- 4.4.19.1.7  Note: for the list of main functions related to this mode, refer to 4.5 'Modes and  onboard functions'. [¶3489]

# 4.4.19.2 Used in levels [¶3490]

- 4.4.19.2.1  Used in levels 1, 2 and 3. [¶3491]

# 4.4.19.3 Responsibilities [¶3492]

- 4.4.19.3.1  The ERTMS/ETCS on-board equipment is responsible for the background supervision of the train movement to the extent permitted by the information provided by trackside. [¶3493]

- 4.4.19.3.1.1 Note: The Limited Supervision mode enables the train to be operated in areas equipped with lineside signals where ETCS does not have information regarding the status of some signals, i.e. not all signals are fitted with LEUs or connected to an RBC [¶3494]

- 4.4.19.3.2  The  driver  must  always  observe  the  existing  line-side  information  (signals,  speed boards etc.) and National operating rules. [¶3495]

- 4.4.19.3.2.1 Note: the indications  given  to  the  driver  by  the  ERTMS/ETCS  on-board equipment do not substitute the observance of the line-side information. In particular the  display  of  the  LSSMA, if  deemed necessary by the trackside, only complements [¶3496]


---
<!-- pagina 273 -->

the line-side information, e.g. in case there could be a discrepancy between this latter and the background supervision. [¶3497]


---
<!-- pagina 274 -->

# 4.4.20 PASSIVE SHUNTING [¶3498]

# 4.4.20.1 Description [¶3499]

- 4.4.20.1.1  The  Passive  Shunting  mode  is  defined  to  manage  the  ERTMS/ETCS  on-board equipment of a slave engine (NOT remote controlled, but mechanically coupled to the leading engine), being part of a shunting consist. This mode can also be used to carry on a shunting movement with a single engine fitted with one on-board equipment and two cabs, when the driver has to change the driving cab. [¶3500]

- 4.4.20.1.2  The desk of a Passive Shunting engine must be closed (since there is no driver, no information shall be shown). [¶3501]

- 4.4.20.1.3  As the engine is coupled to a leading engine, its ERTMS/ETCS on-board equipment shall not perform any train movement supervision. [¶3502]

- 4.4.20.1.4  The  ERTMS/ETCS  on-board  equipment  shall  perform  Train  Position  function;  in particular, the front/rear end of the engine (i.e., not the train) shall be used to refer to train front/rear end. [¶3503]

- 4.4.20.1.5  It shall only be possible to enter in Passive Shunting mode from the Shunting mode; while  in  Shunting  mode,  the  driver  shall  have  the  possibility  to  enable  the  function 'Continue Shunting on desk closure'. [¶3504]

- 4.4.20.1.6  When the active desk is closed, the ERTMS/ETCS on-board equipment shall switch to Passive Shunting mode if the function 'Continue Shunting on desk closure' is active and  the  'passive  shunting  input  signal'  is  received  from  the  train  interface.  If  the function  'Continue  Shunting  on  desk  closure'  is  not  active  or  the  'passive  shunting input  signal'  is  not  present,  the  ERTMS/ETCS  on-board  equipment  shall  switch  to Stand-By mode instead. [¶3505]

- 4.4.20.1.7  The special function 'Continue Shunting on desk closure' shall allow one and only one transition from Shunting mode to Passive Shunting mode. The special function shall be inactive once the Shunting mode is left. [¶3506]

- 4.4.20.1.8  If  a  desk  of  the  Passive  Shunting  engine  is  opened  and no  'Stop Shunting on desk opening'  information  previously  received  from  balise  group  is  stored  onboard,  the ERTMS/ETCS on-board equipment shall switch to Shunting mode. [¶3507]

- 4.4.20.1.9  If  a  desk  of  the  Passive  Shunting  engine  is  opened  and  'Stop  Shunting  on  desk opening'  information  previously  received  from  balise  group  is  stored  onboard,  the ERTMS/ETCS on-board equipment shall switch to Stand By mode. [¶3508]

- 4.4.20.1.10  If  possible,  the  train  must  not  be  stopped  due  to  a  safety  critical  fault  in  a  Passive Shunting  engine.  The  ERTMS/ETCS  on-board  equipment  should  therefore  try  to memorise the occurrence of such fault(s), which should be handled when the engine leaves the Passive Shunting mode. [¶3509]


---
<!-- pagina 275 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3510]

- 4.4.20.1.11  When in Passive Shunting mode, the ERTMS/ETCS on-board shall not manage level transitions.  However,  an  immediate  level  transition  order  or  a conditional level transition order shall be stored and shall be evaluated only when another mode than Shunting or Passive Shunting has been entered (i.e. when the Shunting movement is terminated). [¶3511]

- 4.4.20.1.12  When receiving a communication session establishment order, the ERTMS/ETCS onboard  in  Passive  Shunting  mode  shall  not  establish  the  communication  session,  but shall store the RBC ID/phone number information. [¶3512]

- 4.4.20.1.13  When in Passive Shunting mode, the ERTMS/ETCS on-board shall not manage RBCRBC hand-over, except for storing the RBC ID/phone number information given at the RBC/RBC border. [¶3513]

- 4.4.20.1.14  Note: for  the  list  of  main  functions  related  to this mode, refer to chapter  4.5 'Modes and on-board functions'. [¶3514]

- 4.4.20.1.15  In case of balise group message consistency error (refer to 3.16.2.4.4 and 3.16.2.5.1), the ERTMS/ETCS onboard equipment shall not command the service brake. [¶3515]

# 4.4.20.2 Used in levels [¶3516]

- 4.4.20.2.1  Used in all levels: Level 0, level 1, level 2, level 3 and level NTC [¶3517]

# 4.4.20.3 Responsibilities [¶3518]

- 4.4.20.3.1  The ERTMS/ETCS on-board equipment of an engine in Passive Shunting mode has no responsibility for the train protection. [¶3519]

- 4.4.20.3.2  The notion of responsibility of the driver is not relevant for the Passive Shunting mode. [¶3520]

- 4.4.20.3.3  Note: The leading engine is responsible for the movement of the train. It is then the ERTMS/ETCS  on-board  equipment  of  the  leading  engine  that  is  fully/partially/not responsible for the train protection, with respect to its mode. [¶3521]


---
<!-- pagina 276 -->

# 4.5 Modes and on-board functions [¶3522]

# 4.5.1 Introduction [¶3523]

- 4.5.1.1 The following table specifies in which modes the on-board functions are active or not. The functions are described in the 'Related SRS §' (second column of the table). [¶3524]

- 4.5.1.2 Note: Modes are not the only thing that can influence an onboard function. This is why this  Table  is  not  enough  in  itself  to  understand  all  the  ERTMS/ETCS  onboard behaviour.  It  must  be  understood  as  a  complement  to  all  other  SRS  chapters (especially §4.7, 4.8, 4.9 and 4.10). [¶3525]

- 4.5.1.3 Note: for DMI depending on modes, refer to §4.7. [¶3526]

# 4.5.2 Active Functions Table [¶3527]

# 4.5.2.1 X = functions shall be active [¶3528]

Empty case = function shall be inactive [¶3529]

O = Optional (function is not required for interoperability, but is not forbidden) [¶3530]

[¶3531]
| ONBOARD-FUNCTIONS                                                                                                                                                                              | RELATED SRS §         | N P   | S B   | P S   | S H   | F S   | L S   | S R O S   | S L   |    | N L   | U N   | T R P T   | I S S N   | R V   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-------|-------|-------|-------|-------|-------|-----------|-------|----|-------|-------|-----------|-----------|-------|
| Data Consistency                                                                                                                                                                               |                       |       |       |       |       |       |       |           |       |    |       |       |           |           |       |
| Check linking consistency                                                                                                                                                                      | 3.16.2.3 3.4.4        |       |       |       |       | X     | X     | X         |       |    |       |       |           |           |       |
| Check Balise Group Message Consistency if linking consistency is checked                                                                                                                       | 3.16.2.4.1 3.16.2.4.3 |       |       |       |       | X     | X     | X         |       |    |       |       |           |           |       |
| Check Balise Group Message Consistency if no linking consistency is checked (because no linking information is available and/or because the function 'check linking consistency is not active) | 3.16.2.4.4            |       | X     | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X         | X         | X     |
| Check Unlinked Balise Group Message Consistency                                                                                                                                                | 3.16.2.5              |       | X     | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X         | X         | X     |
| Check correctness of radio messages                                                                                                                                                            | 3.16.3.1.1            |       | X     | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X         | X         | X     |
| Check radio sequence                                                                                                                                                                           | 3.16.3.3              |       | X     | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X         | X         | X     |
| Check safe radio connection (only level 2/3)                                                                                                                                                   | 3.16.3.4              |       |       |       |       | X     | X     | X         |       |    |       |       |           |           |       |
| Determine Train Speed and Position:                                                                                                                                                            |                       |       |       |       |       |       |       |           |       |    |       |       |           |           |       |


---
<!-- pagina 277 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3532]

[¶3533]
| ONBOARD-FUNCTIONS                                                                                    | RELATED SRS §             | N P   | S B   | P S   | S H   | F S   | L S   | S R   | O S   | S L   | N L   | U N   | T R P T   | S F I S   | S N   | R V   |
|------------------------------------------------------------------------------------------------------|---------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-----------|-----------|-------|-------|
| Determine train position referenced to LRBG                                                          | 3.6.1 3.6.4               |       | X     | X     | X     | X     | X     | X     | X X   | X     | X     | X     | X         |           | X     | X     |
| Determine train speed, train acceleration, train standstill                                          | None                      |       | X     | X     | X     | X     | X     | X     | X X   | X     | X     | X     | X         | O         | X     | X     |
| Determine Geographical Position                                                                      | 3.6.6                     |       | X     |       |       | X     | X     | X     | X     | X     | X     | X     | X         |           |       |       |
| Report train position when train reaches standstill                                                  | 3.6.5.1.4 a)              |       |       |       |       | X     | X     | X     | X     |       |       |       |           | O         |       | X     |
| Report train position when mode changes to… 1                                                        | 3.6.5.1.4 b)              |       | X     |       | X 2   | X     | X     | X     | X X   | X     | X     | X     | X         | X O       | X     | X     |
| Report train position when train integrity confirmed by driver                                       | 3.6.5.1.4 c)              |       | X     |       |       | X     | X     | X     | X     |       |       |       | X         |           |       |       |
| Report train position when loss of train integrity is detected                                       | 3.6.5.1.4 d)              |       | X     |       |       | X     | X     | X     | X     |       |       | X     | X         |           |       | X     |
| Report train position when train front/rear passes an RBC/RBC border (only level 2/3)                | 3.6.5.1.4 e) 3.6.5.1.4 k) |       |       |       |       | X     | X     | X     | X     |       |       | X     |           |           |       |       |
| Report train position when train rear passes a level transition border (from level 2/3 to 0, NTC, 1) | 3.6.5.1.4 f)              |       |       |       |       | X     | X     | X     | X     |       | X     | X     |           |           | X     |       |
| Report train position when change of level due to trackside order                                    | 3.6.5.1.4 g)              |       |       |       |       | X     | X     | X     | X     | X     |       | X     |           |           |       |       |
| Report train position when change of level due to driver request                                     | 3.6.5.1.4 g)              |       | X     |       |       | X     | X     | X     | X     | X     |       |       |           |           |       |       |
| Report train position when establishing a session with RBC                                           | 3.6.5.1.4 h)              |       | X     |       | X     | X     | X     | X     | X X   | X     | X     | X     | X         |           | X     | X     |
| Report train position when a data consistency error is detected (only level 2/3)                     | 3.6.5.1.4 l)              |       | X     |       |       | X     | X     | X     | X X   | X     | X     | X     | X         |           | X     | X     |
| Report train position as requested byRBC…                                                            | 3.6.5.1.4                 |       | X     |       |       | X     | X     | X     | X     | X     | X     | X     | X         |           | X     | X     |
| …or Report train position at every passage of an LRBG compliant balise group                         | 3.6.5.1.4 j)              |       |       |       |       | X     | X     | X     | X     | X     | X     | X     | X         |           | X     | X     |
| Manage MA                                                                                            |                           |       |       |       |       |       |       |       |       |       |       |       |           |           |       |       |

1  For ETCS level 2 and 3 this may imply establishing a radio communication session if none is established.

2  Exception: the transition PS => SH shall not be reported


---
<!-- pagina 278 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3534]

[¶3535]
| ONBOARD-FUNCTIONS                                                                                                                | RELATED SRS §     | N P   | S B P S   | S H   | F S   | L S   |    | S R O S   | S L N L   | U N   | T R P T   | S F   | I S S N   | R V   |
|----------------------------------------------------------------------------------------------------------------------------------|-------------------|-------|-----------|-------|-------|-------|----|-----------|-----------|-------|-----------|-------|-----------|-------|
| Request MA Cyclically respect to approach of perturbation location (T_MAR) or MA timer elapsing (T_TIMEOUTRQST) (only level 2/3) | 3.8.2.3 a) and b) |       |           |       | X     | X     |    | X         |           |       |           |       |           |       |
| Request MA Cyclically when 'Start' is selected (only level 2/3)                                                                  | 4.4.11 5.4, 5.11  | X     |           |       |       |       | X  |           |           |       | X         |       |           |       |
| Request MA on reception of "track ahead free up to the level 2/3 transition location" (only level 0,1,NTC)                       | 3.8.2.7.1         | X     |           |       | X     | X     | X  | X         | X         | X     | X         |       | X         |       |
| Request MA on track description deletion (only level 2/3)                                                                        | 3.8.2.7.3         |       |           |       | X     | X     |    | X         |           |       |           |       |           |       |
| Determine EOA/LOA, SvL, Danger Point, etc…                                                                                       | 3.8.4 3.8.5       |       |           |       | X     | X     |    | X         |           |       |           |       |           |       |
| Handle Co-operative MA revocation (only level 2/3)                                                                               | 3.8.6             |       |           |       | X     | X     |    | X         |           |       |           |       |           |       |
| Manage Unconditional Emergency Stop                                                                                              | 3.10              | X     |           |       | X     | X     | X  | X         |           |       | X         |       |           |       |
| Manage Conditional Emergency Stop                                                                                                | 3.10              |       |           |       | X     | X     |    | X         |           |       | X         |       |           |       |
| Determine Most Restrictive Speed Profile, based on :                                                                             |                   |       |           |       |       |       |    |           |           |       |           |       |           |       |
| SSP                                                                                                                              | 3.11.3            |       |           |       | X     | X     |    | X         |           |       |           |       |           |       |
| ASP                                                                                                                              | 3.11.4            |       |           |       | X     | X     |    | X         |           |       |           |       |           |       |
| TSR                                                                                                                              | 3.11.5            |       |           |       | X     | X     | X  | X         | X         |       |           |       |           |       |
| Signalling related speed restriction when evaluated as a speed limit                                                             | 3.11.6            |       |           |       | X     | X     |    | X         |           |       |           |       |           |       |
| Mode related speed restriction                                                                                                   | 3.11.7            |       |           | X     |       | X     | X  | X         | X         |       |           |       |           | X     |
| Train related speed restriction                                                                                                  | 3.11.8            |       |           |       | X     | X     | X  | X         | X         |       |           |       |           | X     |
| STM max speed                                                                                                                    | 3.11.2.2 g)       |       |           |       | X     | X     | X  | X         | X         |       |           |       | X         |       |
| STM system speed                                                                                                                 | 3.11.2.2 h)       |       |           |       | X     | X     | X  | X         | X         |       |           |       |           |       |
| LX speed                                                                                                                         | 3.12.5.6          |       |           |       | X     | X     |    | X         |           |       |           |       |           |       |
| Speed restriction to ensure a given permitted braking distance                                                                   | 3.11.11           |       |           |       | X     | X     |    | X         |           |       |           |       |           |       |
| Override related speed restriction                                                                                               | 5.8.3.6           |       |           | X     |       |       | X  |           | X         |       |           |       |           |       |
| Supervise Train Speed                                                                                                            |                   |       |           |       |       |       |    |           |           |       |           |       |           |       |


---
<!-- pagina 279 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3536]

[¶3537]
| ONBOARD-FUNCTIONS                                                                                                                                         | RELATED SRS §                          | N P S B   | P S   | S H   |    | F S   | L S   | S R   | O S   | S L   | N L   | U N   | T R   | P T   | S F   | I S S N   | R V   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|-----------|-------|-------|----|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-----------|-------|
| Speed and Distance Monitoring based on MRSP, MA, release speed, gradient, mode profile, non protected LX start location, and route unsuitability location | 3.13 5.9.3.5 5.7.3.4 3.12.2.8 3.12.5.4 |           |       |       | X  | X     |       |       | X     |       |       |       |       |       |       |           |       |
| Speed and Distance Monitoring based on MRSP                                                                                                               | 4.4.10.1                               |           |       |       |    |       |       |       |       |       | X     |       |       |       |       |           |       |
| Speed and Distance Monitoring based on MRSP, allowed distance to run in Staff Resp. mode                                                                  | 4.4.11                                 |           |       |       |    |       | X     |       |       |       |       |       |       |       |       |           |       |
| Ceiling Speed Monitoring only (no braking curve) based on MRSP                                                                                            | 4.4.8.1.1 a) 4.4.18.1.3 a)             |           |       | X     |    |       |       |       |       |       |       |       |       |       |       | X 3       | X     |
| Supervise Train Movements                                                                                                                                 |                                        |           |       |       |    |       |       |       |       |       |       |       |       |       |       |           |       |
| Backwards Distance Monitoring                                                                                                                             | 4.4                                    |           |       |       |    |       |       |       |       |       |       |       | X     |       |       |           | X     |
| Roll Away Protection                                                                                                                                      | 3.14.2                                 |           |       | X     | X  | X     | X     | X     |       |       | X     |       | X     |       |       |           | X     |
| Reverse Movement Protection                                                                                                                               | 3.14.3                                 |           |       |       | X  | X     | X     | X     |       |       |       |       | X     |       |       |           | X     |
| Standstill Supervision                                                                                                                                    | 3.14.4 4.4.7.1.5                       | X         |       |       |    |       |       |       |       |       |       |       |       |       |       |           |       |
| Supervise 'danger for shunting' information and list of expected balises for shunting                                                                     | 4.4.8.1.1 b) and c)                    |           |       | X     |    |       |       |       |       |       |       |       |       |       |       |           |       |
| Supervise 'Stop if in SR' information and list of expected balises for Staff Responsible                                                                  | 4.4.11.1.3 c) and d)                   |           |       |       |    |       | X     |       |       |       |       |       |       |       |       |           |       |
| Supervise signalling related speed restriction when evaluated as a trip order                                                                             | 3.11.6.4                               |           |       |       | X  | X     | X     | X     |       |       |       |       |       |       |       |           |       |
| Command Emergency Brake                                                                                                                                   | 4                                      | X         |       |       |    |       |       |       |       |       |       | X     |       | X     |       |           |       |
| Determine Mode and Level                                                                                                                                  |                                        |           |       |       |    |       |       |       |       |       |       |       |       |       |       |           |       |
| Determine ERTMS/ETCS Mode                                                                                                                                 | 3.12.4, 4.6                            | X X       | X     | X     | X  | X     | X     | X     | X     | X     | X     | X     | X     | X     | X     | X         | X     |
| Determine ERTMS/ETCS level                                                                                                                                | 5.10                                   | X         | X     | X     | X  | X     | X     | X X   |       | X     | X     | X     | X     |       | X     | X         | X     |
| Other functions                                                                                                                                           |                                        |           |       |       |    |       |       |       |       |       |       |       |       |       |       |           |       |
| System Version Management                                                                                                                                 | 3.17                                   | X         | X     | X     | X  | X     |       | X X   | X     | X     | X     | X     | X     |       |       | X         | X     |
| Manage Communication Session                                                                                                                              | 3.5                                    | X         | X     | X     | X  | X     |       | X X   | X     | X     | X     | X     | X     |       |       | X         | X     |
| Delete Revoked TSR                                                                                                                                        | 3.11.5.5                               | X         |       |       | X  | X     | X     |       | X     |       | X     | X     |       | X     |       |           |       |
| Override (Trip inhibition) 4                                                                                                                              | 5.8                                    |           |       | X     |    |       | X     |       |       | X     |       |       |       |       |       | X         |       |

3   In  case  the  ERTMS  on-board  equipment  is  interfaced  to  the  National  System  through  an  STM,  refer  to SUBSET-035 for details [¶3538]


---
<!-- pagina 280 -->

# ERA * UNISIG * EEIG ERTMS USERS GROUP [¶3539]

[¶3540]
| ONBOARD-FUNCTIONS                                                                                            | RELATED SRS §                           | N P S B   | P S   | S H   | F S   | L S   | S R O S   | S L   |    | N L   | U N   | T R   | P T   | S F   | I S S N   | R V   |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------|-----------|-------|-------|-------|-------|-----------|-------|----|-------|-------|-------|-------|-------|-----------|-------|
| Manage Track Conditions excluding Sound Horn, Non Stopping Areas, Tunnel Stopping Areas and Big Metal Masses | 3.12.1                                  |           |       |       | X     | X     | X         |       | X  |       | X     | X     |       |       |           |       |
| Manage Track Conditions Sound Horn, Non Stopping Areas, Tunnel Stopping Areas                                | 3.12.1                                  |           |       |       | X     | X     | X         |       |    |       |       |       |       |       |           |       |
| Manage Track Condition Big Metal Masses                                                                      | 3.12.1                                  | X         | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X     | O     |       | X         |       |
| Manage Route Suitability                                                                                     | 3.12.2                                  |           |       |       | X     | X     | X         |       |    |       |       |       |       |       |           |       |
| Manage Text Display to the driver                                                                            | 3.12.3                                  | X         |       |       | X     | X     | X X       |       |    | X     | X     | X     |       |       |           | X     |
| Manage LSSMA display to the driver                                                                           | 4.4.19.1                                |           |       |       |       | X     |           |       |    |       |       |       |       |       |           |       |
| Manage RBC/RBC Handover (only level 2/3)                                                                     | 3.15.1, 5.15                            |           |       |       | X     | X     | X X       | X     | X  |       | X     |       |       |       |           |       |
| Manage Track Ahead Free Request (only level 2/3)                                                             | 3.15.5                                  | X         |       |       |       | X     | X X       |       |    |       |       | X     |       |       |           |       |
| Provide Fixed Values, and Default/National Values                                                            | 3.18.1 3.18.2                           | X         | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X     |       |       | X         | X     |
| Manage change of Train Data from external sources                                                            | 5.17                                    | X         |       |       | X     | X     | X X       |       |    | X     | X     | X     |       |       | X         |       |
| Provide Date and Time                                                                                        | 3.18.5                                  | X         | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X     |       |       | X         | X     |
| Provide Juridical Data                                                                                       | 3.20                                    | X         | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X     | O     | O     | X         | X     |
| Inhibition of revocable TSRs from balises(only level 2/3)                                                    | 3.11.5.12 3.11.5.13 3.11.5.14 3.11.5.15 |           |       |       | X     | X     | X         |       |    |       | X     | X     |       |       |           |       |
| Cold Movement Detection                                                                                      | 3.15.8                                  | O         |       |       |       |       |           |       |    |       |       |       |       |       |           |       |
| Continue Shunting on desk closure (Enabling transition to Passive Shunting mode)                             | 5.12.4                                  |           |       | X     |       |       |           |       |    |       |       |       |       |       |           |       |
| Manage 'Stop Shunting on desk opening' information                                                           | 4.4.20.1.8 4.4.20.1.9                   |           | X     |       |       |       |           |       |    |       |       |       |       |       |           |       |
| Manage Virtual Balise Covers                                                                                 | 3.15.9                                  | X         | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X     | O     | O     | X         | X     |
| Advance display of route related information                                                                 | 3.15.10                                 |           |       |       | X     |       | X         |       |    |       |       |       |       |       |           |       |

# Figure 1: Active Functions table [¶3541]

4  For UN and SN mode, conditions for re-activation of transition to Trip mode (see § 5.8.4.1a) & b)) shall be supervised.


---
<!-- pagina 281 -->

# 4.6 Transitions between modes [¶3542]

# 4.6.1 Symbols [¶3543]

- 4.6.1.1 The indication ' 4> ' means: The condition n°4 must be fulfilled to trigger the transition [¶3544]

- 4.6.1.2 From the mode located in the column [¶3545]

- 4.6.1.3 To the mode that is indicated by the arrow ' > '. [¶3546]

- 4.6.1.4 Each transition from a given mode receives a priority order (indicated by ' -px', x is the priority order) to avoid a conflict between the different transitions when they occur at the same time (i.e. in the same clock cycle). P1 has a higher priority than P2. [¶3547]

- 4.6.1.5 Some transitions have received the same priority order. This has been decided when it is obvious that these transitions cannot occur at the same time, and so can never lead to a conflicting situation (for example, the RBC cannot give in the same time a MA for FS and a MA for OS to a given engine, this is why the transition 'from SR to FS' and the transition 'from SR to OS' have the same priority order). [¶3548]

- 4.6.1.6 "16, 17, 18" means "16 or 17 or 18". [¶3549]


---
<!-- pagina 282 -->