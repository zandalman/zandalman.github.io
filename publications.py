publications = [
  {
    "id": "Andalman+2026a",
    "year": 2026,
    "authors": "Z. L. Andalman, E. Quataert, E. R. Coughlin, <i>et al.</i>",
    "authors_long": "Z. L. Andalman, E. Quataert, E. R. Coughlin, & C. Nixon",
    "title": "Resolving the (Debate About) Nozzle Shocks in Tidal Disruption Events",
    "journal": "in prep.",
    "link": None,
    "arxiv": None,
    "pdf": None,
    "data": "eos.zip",
    "data_description": r"""
    Python code for generating EOS tables and their inversions using the partition function from Tomida+2013.
    Code in gen.py, example usage in gen.ipynb.
    """,
    "abstract": r"""
    When a star passes within the Roche limit of a supermassive black hole (BH), it is pulled apart by the BH's tidal field in a tidal disruption event (TDE). 
    The resulting flare is powered by the circularization and accretion of bound stellar debris, which returns to the BH on eccentric orbits as a thin debris stream. 
    The returning fluid elements follow inclined orbits that converge near pericenter, resulting in extreme vertical compression to scales 1e-4 Rsol and the formation of a nozzle shock. 
    Dissipation at the nozzle shock may affect circularization by altering the properties of the debris stream, but its role is the subject of ongoing debate. 
    We develop an idealized model for the debris stream evolution combining 3D smooth particle hydrodynamics simulations, the semi-analytic affine model, and 1D finite-volume hydrodynamic simulations, which unambiguously resolve the nozzle shock. 
    Because our model is computationally inexpensive, we can analyze the debris stream evolution for a wide range of conditions using a realistic equation of state. 
    Near peak fallback, Hydrogen recombination and molecular Hydrogen formation broaden the stream by a factor ~5, enhancing dissipation at the nozzle.
    However, the dissipation is still insufficient to directly circularize the debris by in-plane pressure gradients. 
    Instead, the thicker stream substantially increases the likelihood that the stream self-intersects on the second orbit, despite relativistic nodal precession. 
    The stream properties at self-intersection are sensitive to dissipation at the nozzle and the timing of focal points where the ballistic trajectories of the debris converge.
    Our results clarify the nozzle shock's role in circularization in TDEs, providing a foundation for more realistic circularization and emission models.
    """
  },
  {
    "id": "Andalman+2026b",
    "year": 2026,
    "authors": "Z. L. Andalman, C. Fryer, C. Fontes, <i>et al.</i>",
    "authors_long": "Z. L. Andalman, C. Fryer, C. Fontes, M. Mumpower, & R. Wollaeger",
    "title": "Thermalization in Kilonova Ejecta with Transport and Deatiled Microphysics",
    "journal": "in prep.",
    "link": None,
    "arxiv": None,
    "pdf": None,
    "data": None,
    "data_description": None,
    "abstract": None
  },
  {
    "id": "Sunseri+2025",
    "year": 2025,
    "authors": "J. Sunseri, Z. L. Andalman, & R. Teyssier",
    "authors_long": "J. Sunseri, Z. L. Andalman, & R. Teyssier",
    "title": "Supermassive Black Hole Growth in Massive Galaxies at Cosmic Dawn",
    "journal": "preprint",
    "link": None,
    "arxiv": "https://arxiv.org/pdf/2510.19822",
    "pdf": "Sunseri+2025.pdf",
    "data_description": None,
    "abstract": r"""
    Among the emerging excess of massive, bright galaxies at Cosmic Dawn (z > 9) seen by the James Webb Space Telescope, several exhibit spectral features associated with active galactic nuclei (AGN). 
    These AGN candidates suggest that supermassive black holes (SMBHs) grow rapidly in the early Universe. 
    In a series of numerical experiments, we investigate how SMBHs grow within and influence the most massive galaxies at Cosmic Dawn using cosmological hydrodynamic zoom-in simulations run with the adaptive mesh refinement code RAMSES. 
    Our suite of simulations explore how super-Eddington accretion, seed mass, and the strength of feedback influence SMBH-galaxy co-evolution in the early Universe. 
    We find that SMBH growth is sensitive to stellar feedback which generates a turbulent-multiphase interstellar medium (ISM) that stochastically starves the SMBH. 
    In the absence of AGN feedback, we find that the SMBH is starved ~50% of the time after the onset of star formation in the galaxy. 
    SMBH growth can become self-regulated by AGN feedback if the SMBH becomes massive enough, either by accretion or seeding, for its feedback to dominate the surrounding nuclear region. 
    We find no evidence of galaxy-scale, AGN-driven quenching in the star formation rate (SFR) across all simulations in our suite.
    """
  },
  {
    "id": "Andalman+2025",
    "year": 2025,
    "authors": "Z. L. Andalman, R. Teyssier, & A. Dekel",
    "authors_long": "Z. L. Andalman, R. Teyssier, & A. Dekel",
    "title": "On the Origin of the High Star-Formation Efficiency in Massive Galaxies at Cosmic Dawn",
    "journal": "MNRAS",
    "link": "https://academic.oup.com/mnras/article/540/4/3350/8157902",
    "arxiv": "https://arxiv.org/abs/2410.20530",
    "pdf": "Andalman+2025.pdf",
    "data": "sfr.zip",
    "data_description": r"""
    Star formation histories of simulated massive galaxies at Cosmic Dawn.
    Data available for the fiducial model and models lowPhot, highPhot, solTurb, varTurb.
    See README.txt for more information.
    """,
    "abstract": r"""
    Motivated by the early excess of bright galaxies seen by JWST, we run zoom-in cosmological simulations of a massive galaxy at Cosmic Dawn, in a halo of 1e11 Msol at z=9, using the hydro-gravitational code RAMSES at an effective resolution ~10 pc. 
    We investigate physical mechanisms that enhance the star formation efficiencies (SFEs) at the high gas densities of the star-forming regions in this galaxy (~3000 H/cc, ~1e4 Msol/pc^2). 
    Our fiducial star formation recipe uses a physically motivated, turbulence-based, multi-freefall model, avoiding <i>ad hoc</i> extrapolation from lower redshifts. 
    By z=9, our simulated galaxy is a clumpy, thick, rotating disc with a high stellar mass ~3e9 Msol and high star formation rate ~50 Msol/yr.
    The high gas density makes supernova (SN) feedback less efficient, producing a high local SFE >10%. 
    The global SFE is set by feedback-driven outflows and only weakly correlated with the local SFE. 
    Photoionization heating makes SN feedback more efficient, but the integrated SFE always remains high. 
    Intense accretion at Cosmic Dawn seeds turbulence that reduces local SFE, but this only weakly affects the global SFE. 
    The star formation histories of our simulated galaxies are similar to observed massive galaxies at Cosmic Dawn, despite our limited resolution. 
    We set the stage for future simulations which treat radiation self-consistently and use a higher effective resolution ~1 pc that captures the physics of star-forming clouds.
    """
  },
  {
    "id": "Kaaz+2023",
    "year": 2023,
    "authors": "N. Kaaz, M. T. P. Liska, J. Jacquemin-Ide, <i>et al.</i>",
    "authors_long": "N. Kaaz, M. T. P. Liska, J. Jacquemin-Ide, Z. L. Andalman, G. Musoke, A. Tchekhovskoy, & O. Porth",
    "title": "Nozzle Shocks, Disk Tearing, and Streamers Drive Rapid Accretion in 3D GRMHD Simulations of Warped Thin Disks",
    "journal": "ApJ",
    "link": "https://iopscience.iop.org/article/10.3847/1538-4357/ace051",
    "arxiv": "https://arxiv.org/abs/2210.10053",
    "pdf": "Kaaz+2023.pdf",
    "data": None,
    "data_description": None,
    "abstract": r"""
    The angular momentum of gas feeding a black hole (BH) may be misaligned with respect to the BH spin, resulting in a tilted accretion disk. 
    Rotation of the BH drags the surrounding spacetime, manifesting as Lense-Thirring torques that lead to disk precession and warping. 
    We study these processes by simulating a thin (h/r = 0.02), highly tilted (T = 65 deg) accretion disk around a rapidly rotating (a = 0.9375) BH at extremely high resolutions, which we performed using the general-relativistic magnetohydrodynamic code H-AMR. 
    The disk becomes significantly warped and continuously tears into two individually precessing subdisks. 
    We find that mass accretion rates far exceed the standard alpha-viscosity expectations. 
    We identify two novel dissipation mechanisms specific to warped disks that are the main drivers of accretion, distinct from the local turbulent stresses that are usually thought to drive accretion. 
    In particular, we identify extreme scale height oscillations that occur twice an orbit throughout our disk. 
    When the scale height compresses, "nozzle" shocks form, dissipating orbital energy and driving accretion. 
    Separate from this phenomenon, there is also extreme dissipation at the location of the tear. 
    This leads to the formation of low-angular momentum "streamers" that rain down onto the inner subdisk, shocking it.
    The addition of low-angular momentum gas to the inner subdisk causes it to rapidly accrete, even when it is transiently aligned with the BH spin and thus unwarped. 
    These mechanisms, if general, significantly modify the standard accretion paradigm. 
    Additionally, they may drive structural changes on much shorter timescales than expected in alpha-disks, potentially explaining some of the extreme variability observed in active galactic nuclei.
    """
  },
  {
    "id": "Andalman+2022",
    "year": 2022,
    "authors": "Z. L. Andalman, M. T. P. Liska, A. Tchekhovskoy, <i>et al.</i>",
    "authors": "Z. L. Andalman, M. T. P. Liska, A. Tchekhovskoy, E. R. Coughlin, & N. Stone",
    "title": "Tidal Disruption Discs Formed and Fed by Stream-Stream and Stream-Disc Interactions in Global GRHD Simulations",
    "journal": "MNRAS",
    "link": "https://academic.oup.com/mnras/article/510/2/1627/6446812",
    "arxiv": "https://arxiv.org/abs/2008.04922",
    "pdf": "Andalman+2022.pdf",
    "data": None,
    "data_description": None,
    "abstract": r"""
    When a star passes close to a supermassive black hole (BH), the BH's tidal forces rip it apart into a thin stream, leading to a tidal disruption event (TDE). 
    In this work, we study the post-disruption phase of TDEs in general relativistic hydrodynamics (GRHD) using our GPU-accelerated code H-AMR. 
    We carry out the first grid-based simulation of a deep-penetration TDE (beta = 7) with realistic system parameters: a black hole-to-star mass ratio of 1e6, a parabolic stellar trajectory, and a non-zero BH spin. 
    We also carry out a simulation of a tilted TDE whose stellar orbit is inclined relative to the BH midplane. 
    We show that for our aligned TDE, an accretion disc forms due to the dissipation of orbital energy with ~20% of the infalling material reaching the BH. 
    The dissipation is initially dominated by violent self-intersections and later by stream-disc interactions near the pericentre. 
    The self-intersections completely disrupt the incoming stream, resulting in five distinct self-intersection events separated by approximately 12 hours and a flaring in the accretion rate.
    We also find that the disc is eccentric with mean eccentricity e = 0.88. 
    For our tilted TDE, we find only partial self-intersections due to nodal precession near pericentre. 
    Although these partial intersections eject gas out of the orbital plane, an accretion disc still forms with a similar accreted fraction of the material to the aligned case. 
    These results have important implications for disc formation in realistic tidal disruptions. 
    For instance, the periodicity in accretion rate induced by the complete stream disruption may explain the flaring events from Swift J1644+57.
    """
  }
]
