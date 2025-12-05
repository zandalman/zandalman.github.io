research = [
  {
    "id": "tde",
    "name": "Tidal Disruption Events",
    "pub_ids": ["Andalman+2022", "Andalman+2026a"],
    "pub_text": ["Andalman+2022, MNRAS", "Andalman+2026a, in prep."],
    "image": "tde.png",
    "text": [
      r"""
      When a star passes within the Roche limit of a SMBH, it is pulled apart by the BH's tidal field in a tidal disruption event (TDE). 
      These rare events are unique astrophysical probes of quiescent SMBHs, accretion physics, and the dynamics of the galactic center. 
      The Vera C. Rubin Observatory's Legacy Survey of Space and Time (LSST) promises to dramatically increase the observed TDE rate, making this an exciting time for TDE modeling.
      """,
      r"""
      I use numerical simulations and (semi-)analytics to study the physics behind TDE emission.
      Ultimately, TDE emission is powered by the circularization and accretion of bound stellar debris, which falls back to the BH on eccentric orbits as a thin debris stream.
      Circularization is driven by stream-stream collisions induced by relativistic apsidal precession
      and, once a disk forms, interactions between the stream and the disk.
      These processes are affected by ballistic dynamics, chemical processes (e.g. Hydrogen recombination),
      relativistic nodal precession, and extreme vertical compression as the debris passes pericenter,
      which produces a nozzle shock.
      """,
      r"""
      In [1], I perform one of the first simulations of debris disk formation in a realistic TDE using the GRMHD code H-AMR,
      although these simulations are limited to a small fraction of the peak fallback time.
      In my ongoing work [2], I develop an idealized model to study the role of the nozzle shock in detail, 
      including the effect of chemical processes and the implications for the stream self-intersection.
      """
    ]
  },
  {
    "id": "galaxy",
    "name": "Cosmic Dawn Galaxies",
    "pub_ids": ["Andalman+2025", "Sunseri+2025"],
    "pub_text": ["Andalman+2025, MNRAS", "Sunseri+2025, preprint"],
    "image": "galaxy.png",
    "text": [
      r"""
      The JWST has opened a new frontier for empirical constraints on galaxy formation models at Cosmic Dawn (z>9), 
      an epoch starting with the formation of the firststars and ending with the reionization of the intergalactic medium (IGM).
      JWST has discovered a growing list of galaxies at Cosmic Dawn with high stellar masses >1e8 Msol and/or high SFRs >1 Msol/yr,
      in tension with the expectations of standard galaxy formation models,
      and overmassive SMBHs relative to the local BH-stellar mass relation.
      I study the interplay between star formation, feedback, and BH growth in these unique environments,
      with extreme gas surface densities and intense accretion of cold streams.
      """,
      r"""
      In [1], I run cosmological zoom-in simulations of a massive galaxy at Cosmic Dawn,
      using a physically-motivated star formation recipe, which avoids ad hoc extrapolation from lower redshifts.
      In [2], we add SMBHs to these simulations to study their co-evolution with the galaxy.
      """
    ]
  },
  {
    "id": "kilonova",
    "name": "Kilonovae",
    "pub_ids": ["Andalman+2026b"],
    "pub_text": ["Andalman+2026b, in prep."],
    "image": "kilonova.png",
    "text": [
      r"""
      The observation of GW170817 confirmed that binary neutron star mergers are not only strong sources of gravitational waves, but also sites of nucleosynthesis by the rapid neutron capture process (r-process). 
      The radioactive decay of r-process nuclides in the merger ejecta produces energetic gamma-rays, beta and alpha particles that, when thermalized, power a bright transient in the optical and near-infrared known as a kilonova (KN). 
      In my ongoing work [1], I develop a new model for the transport and thermalization of beta decay electrons using the two-moment method
      and detailed electron-atom cross sections.
      """
    ]
  },
  {
    "id": "misc",
    "name": "Miscellaneous",
    "pub_ids": None,
    "pub_text": None,
    "image": "misc.png",
    "text": [
      r"<h3>Optical Tweezer Arrays</h3>",
      r"""
      Optical tweezers are micrometer-sized optical traps obtained by tightly focusing a laser beam.
      Optical techniques can diffract the beam into many spots, making it possible to form arrays of atoms in a variety of geometries.
      In such an array, the interactions between atoms can be controlled by inducing quantum tunneling between array sites or by placing atoms into high-energy Rydberg states.
      This property makes them great analog quantum simulators (AQS), i.e.
      a controllable quantum system that mimics a less experimentally feasible one via a direct mapping between their Hamiltonians.
      """,
      r"""
      As part of Nir Navon's Ultracold Quantum Matter Lab, I worked on an apparatus to cool bosonic Sr to nano-Kelvin temperatures so that it could be captured by optical tweezers.
      My main contribution was the design and construction of a control box for the electromagnetic coils of a magneto-optical trap (MOT).
      The MOT uses a quadrapole magnetic field and a set of counter-propagating lasers slightly detuned from an electronic transition to create an effective damped oscillator potential.
      Once the atoms are trapped, the MOT coils switch to a Helmholtz configuration to generate a strong ~700 G magnetic field to allow Sr's usually forbidden  S  -  P  clock transition.
      """,
      r"""
      My control box switches between these configurations rapidly using insulated gate bipolar transistors (IGBTs) to operate a fast-switching H-bridge drawing up to 300 A.
      The control box also includes a water cooling system, a temperature interlock, and a custom printed circuit board for running the control box from a digital display.
      Aside from the control box, I also contributed the development of a new user interface for the parametric experimental control software Artiq, 
      the application of convolution neural networks to the fast sorting of atom arrays via the assignment problem, 
      the deployment of a network of sensors to monitor ambient lab conditions and log the data to an online database, 
      and the alignment and testing of a double-pass acousto-optic modulator (AOM).
      """,
      r"<h3>CubeSat</h3>",
      r"""
      During my senior year of undergrad, I was president of the Yale Undergraduate Aerospace Association (YUAA), Yale's largest undergraduate engineering organization, with more than 80 members and several concurrent aerospace projects.
      In 2018, YUAA received a grant from NASA's CubeSat Launch Initiative (CSLI) to develop the Bouchet Low Earth Alpha-Beta Space Telescope (BLAST), a 2U CubeSat with a cosmic ray detector payload, to be launched into Low Earth Orbit (LEO).
      BLAST's main science objective is to detect high energy protons and map the changing morphology of the South Atlantic Anamoly (SAA), a region where the Earth's lower Van Allen Belt crosses LEO resulting in increased magnetic and charged particle fluxes.
      The SAA impacts satellites by interfering with astronomical observations and producing memory errors through bit flips.
      BLAST includes multiple interacting subsystems, including a gravity gradient boom and magnotorquers for attitude determination and control.
      """,
      r"""
      I lead the design of the cosmic ray detector (CRD) payload.
      The CRD consists of a plastic scintillator and a Silicon photomultiplier (SiPM).
      The signal from the SiPM is processed by several amplification stages and a custom multi-channel analyzer before count data is fed back to the on-board computer.
      The project was funded in part by the Connecticut Space Grant Consortium and we presented our progress at the Connecticut Space Grant expo.
      """,
      r"""
      I also worked on several smaller projects during my time with YUAA.
      During my first year, I worked on a team designing the rover payload for a rocket, to be flown at the Intercollegiate Rocket Engineering Competition (IREC).
      During my second year, I lead a small team designing and constructing an ornithopter, or robotic bird, capable of self-correcting flight.
      The ornithopter used high-torque servos to flap wings made of carbon fiber rods and kite fabric.
      By applying different offsets to the flapping cycle of the wings, we independently controlled roll, pitch, and yaw.
      The ornithopter included a custom printed circuit board which monitored acceleration and magnetic fields to calibrate steering and apply real-time corrections to its flight.
      """
    ]
  }
]

publications = [
  {
    "id": "Andalman+2026a",
    "year": 2026,
    "authors": "Z. L. Andalman, E. Quataert, E. R. Coughlin, et al.",
    "authors_long": "Z. L. Andalman, E. Quataert, E. R. Coughlin, & C. Nixon",
    "title": "Resolving the (Debate About) Nozzle Shocks in Tidal Disruption Events",
    "journal": "in prep.",
    "link": None,
    "arxiv": None,
    "pdf": None,
    "data": "eos.zip",
    "fig": "Andalman+2026a.png",
    "data_description": r"""
    Python code for generating EOS tables and their inversions using the partition function from Tomida+2013.
    Code in gen.py, example usage in gen.ipynb.
    """,
    "fig_caption": r"""
    The density as a function of vertical height in the debris stream, from our 1D hydrodynamic simulations in Athena++.
    We show 12 profiles before (top panel) and after (bottom panel) the nozzle. 
    We indicate the time of each profile by its color in the color bar. 
    The snapshots and the color bar are concentrated near the nozzle, where the evolution is most rapid. 
    Before the nozzle, a shock forms and propagates towards the center of the stream slice, where it collides with the shock from the other side of the xy-plane. 
    The resulting dissipation launches outward-propagating shocks that rapidly reach the surface of the stream slice and break out. 
    At the nozzle, the vertical height of the stream is 1e-4 Rsol.
    """,
    "abstract": r"""
    When a star passes within the Roche limit of a supermassive black hole (BH), it is pulled apart by the BH's tidal field in a tidal disruption event (TDE). 
    The resulting flare is powered by the circularization and accretion of bound stellar debris, which returns to the BH on eccentric orbits as a thin debris stream. 
    The returning fluid elements follow inclined orbits that converge near pericenter, resulting in extreme vertical compression to scales 1e-4 Rsol and the formation of a nozzle shock. 
    Dissipation at the nozzle shock may affect circularization by altering the properties of the debris stream, but its role is the subject of ongoing debate. 
    We develop an idealized model for the debris stream evolution combining 3D smooth particle hydrodynamics simulations, the semi-analytic affine model, and 1D finite-volume hydrodynamic simulations. 
    Because our model is computationally cheap, we can unambiguously resolve the nozzle shock, use a realistic equation of state, and follow the debris stream evolution at many different times. 
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
    "authors": "Z. L. Andalman, C. Fryer, C. Fontes, et al.",
    "authors_long": "Z. L. Andalman, C. Fryer, C. Fontes, M. Mumpower, & R. Wollaeger",
    "title": "Thermalization in Kilonova Ejecta with Transport and Detailed Microphysics",
    "journal": "in prep.",
    "link": None,
    "arxiv": None,
    "pdf": None,
    "data": None,
    "fig": None,
    "data_description": None,
    "fig_caption": None,
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
    "fig": "Sunseri+2025.png",
    "data_description": None,
    "fig_caption": r"""
    SMBH mass evolution in our suite of cosmological zoom-in simulations of a massive galaxy at Cosmic Dawn in RAMSES.
    The suite includes simulations with/without AGN feedback (solid/dashed lines) and across a range of maximum Eddington factors (lam_Edd) and initial SMBH masses.
    For context, we also show empirical SMBH mass estimates from JWST.
    The zoom-in panels show snapshots of the projected density field within a 500 pc region around the SMBH.
    The SMBH stochastically samples the multi-phase ISM, 
    resulting in alternating phases of slow Bondi-limited accretion in hot-diffuse regions (starve mode)
    and fast Eddington-limited accretion in cold-dense regions (feast mode).
    AGN feedback only regulates the SMBH growth if the SMBH becomes massive enough to homogenize the ISM in the nuclear region.
    """,
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
    "fig": "Andalman+2025.png",
    "data_description": r"""
    Star formation histories of simulated massive galaxies at Cosmic Dawn.
    Data available for the fiducial model and models lowPhot, highPhot, solTurb, varTurb.
    See README.txt for more information.
    """,
    "fig_caption": r"""
    Density-temperature distribution of gas in our suite of cosmological zoom-in simulations of a massive galaxy at Cosmic Dawn in RAMSES.
    The suite includes simulations with/without SNe feedback and across a range of photoionization feedback strengths.
    We overplot contours outlining the smallest phase space areas containing 75% of star formation events weighted by stellar mass (black) and 75% of SN events (red). 
    In the bottom right panel, we show a schematic diagram of the gas evolution.
    """,
    "abstract": r"""
    Motivated by the early excess of bright galaxies seen by JWST, we run zoom-in cosmological simulations of a massive galaxy at Cosmic Dawn, in a halo of 1e11 Msol at z=9, using the hydro-gravitational code RAMSES at an effective resolution ~10 pc. 
    We investigate physical mechanisms that enhance the star formation efficiencies (SFEs) at the high gas densities of the star-forming regions in this galaxy (~3000 H/cc, ~1e4 Msol/pc^2). 
    Our fiducial star formation recipe uses a physically motivated, turbulence-based, multi-freefall model, avoiding ad hoc extrapolation from lower redshifts. 
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
    "authors": "N. Kaaz, M. T. P. Liska, J. Jacquemin-Ide, et al.",
    "authors_long": "N. Kaaz, M. T. P. Liska, J. Jacquemin-Ide, Z. L. Andalman, G. Musoke, A. Tchekhovskoy, & O. Porth",
    "title": "Nozzle Shocks, Disk Tearing, and Streamers Drive Rapid Accretion in 3D GRMHD Simulations of Warped Thin Disks",
    "journal": "ApJ",
    "link": "https://iopscience.iop.org/article/10.3847/1538-4357/ace051",
    "arxiv": "https://arxiv.org/abs/2210.10053",
    "pdf": "Kaaz+2023.pdf",
    "data": None,
    "fig": "Kaaz+2023.png",
    "data_description": None,
    "fig_caption": r"""
    The LT torques induced by the rotation of the central BH cause the accretion disk to warp and, sometimes, tear into discrete subdisks. 
    In each panel, we plot a 3D rendering of the fluid frame gas density, separated by 1000 rg/c. 
    Azimuthal oscillations in the scale height are apparent in the outer subdisk, where orbiting fluid parcels experience compressions and expansions twice an orbit (evidenced by the light-blue "spokes" in the outer subdisk). 
    """,
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
    "authors": "Z. L. Andalman, M. T. P. Liska, A. Tchekhovskoy, et al.",
    "authors": "Z. L. Andalman, M. T. P. Liska, A. Tchekhovskoy, E. R. Coughlin, & N. Stone",
    "title": "Tidal Disruption Discs Formed and Fed by Stream-Stream and Stream-Disc Interactions in Global GRHD Simulations",
    "journal": "MNRAS",
    "link": "https://academic.oup.com/mnras/article/510/2/1627/6446812",
    "arxiv": "https://arxiv.org/abs/2008.04922",
    "pdf": "Andalman+2022.pdf",
    "data": None,
    "fig": "Andalman+2022.jpeg",
    "data_description": None,
    "fig_caption": r"""
    Contour plots of the logarithmic rest mass density in the equatorial plane during the debris’ initial pericentre passage (first row) 
    and the first (second row) and third (third row) self-intersection events. 
    In the initial pericentre passage, the stream falls back through near vacuum and matter from the stream begins to accumulate near the BH. 
    In the self-intersection events, the stream undergoes apsidal precession and self-intersects close to the analytical self-intersection radius at 142 rg. 
    As a result, the inner parts of the stream are completely disrupted. 
    These violent events are a key dissipation mechanism in the early stages of the TDE evolution. 
    Although powerful, we count only five such events. 
    At late times in our simulation, dissipation occurs primarily through interactions with the newly formed disc.
    """,
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
