from pathlib import Path
from html import escape
from textwrap import dedent
import json

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT/'assets'
(ASSETS/'css').mkdir(parents=True, exist_ok=True)
(ASSETS/'js').mkdir(parents=True, exist_ok=True)
(ASSETS/'img').mkdir(parents=True, exist_ok=True)
(ROOT/'projects').mkdir(parents=True, exist_ok=True)

SITE_NAME = 'The STELLAR Lab'
TAGLINE = 'Statistical Field Theory, Hydrodynamics, and Holography'
CONTACT = 'stellar-lab@googlegroups.com'
ABSTRACTS = json.loads((ROOT/'abstracts.json').read_text(encoding='utf-8'))

projects = [{'slug': 'analytic',
  'status': 'Active',
  'title': 'Analytic structure and the limits of hydrodynamics',
  'kicker': 'Complex momentum · non-hydrodynamic modes · response',
  'summary': 'We study where hydrodynamic expansions stop being analytic and what that breakdown reveals about '
             'microscopic dynamics. The programme compares static screening scales with dynamical pole collisions, '
             'follows quasinormal modes through complex momentum, and studies how isolated poles reorganise into '
             'branch cuts.',
  'questions': ['Which singularity actually sets the radius of convergence of a hydrodynamic expansion?',
                'How are static screening poles ordered relative to hydrodynamic/non-hydrodynamic mode collisions?',
                'What do branch cuts, multiple spectral sheets and complex-momentum spectra tell us about effective '
                'descriptions?'],
  'impact': 'Hydrodynamics is useful only inside a finite domain of frequency and momentum. Mapping its analytic '
            'boundary tells us which additional degrees of freedom must be retained, clarifies the relation between '
            'static and dynamical response, and gives controlled tests of effective theory using holography and '
            'kinetic theory.',
  'img': 'sk-concept.png',
  'strands': ['Hydrostatic failure: static poles versus mode collisions',
              'Complex-momentum quasinormal modes and spectral sheets',
              'Non-hydrodynamic poles, branch cuts and effective-theory domains']},
 {'slug': 'critical',
  'status': 'Active',
  'title': 'Critical phenomena and quantum field theory',
  'kicker': 'CFT · renormalisation · topological phases',
  'summary': 'We study universal behaviour near phase transitions using conformal field theory, conformal perturbation '
             'theory, renormalisation-group methods, dualities and Monte Carlo calculations. Topological quantum field '
             'theory provides a complementary language for phases beyond ordinary symmetry breaking.',
  'questions': ['How accurately can conformal data determine off-critical observables?',
                'Which universal structures persist across lattice, continuum and dual descriptions?',
                'How do topological and symmetry-based descriptions meet near criticality?'],
  'impact': 'This programme connects analytical and numerical descriptions of criticality, confinement, phase '
            'structure and topological order across statistical mechanics, condensed matter and high-energy theory.',
  'img': 'critical-concept.png',
  'strands': ['Conformal perturbation theory away from criticality',
              'Effective strings, confinement and lattice comparisons',
              'Infrared dualities and topological quantum field theory']},
 {'slug': 'exotic',
  'status': 'Active',
  'title': 'Exotic dynamics and search',
  'kicker': 'Boost-agnostic mechanics · kinetic theory · optimisation',
  'summary': 'We study particles whose velocity need not be proportional to momentum and ask what can be gained by '
             'treating the dispersion relation itself as a design variable. The programme runs from boost-agnostic '
             'Hamiltonian and kinetic theory to hard-particle simulations, first-passage search in mazes and '
             'dispersion-engineered optimisation algorithms.',
  'questions': ['How do non-quadratic dispersions change equilibration, collisions and transport in an interacting '
                'gas?',
                'Can changing only the free-particle dynamics improve exploration or first-passage performance after '
                'matching energy, speed and time scales?',
                'Can dispersion engineering provide an optimisation control that cannot be reduced to standard '
                'particle-swarm parameters or coordinate redefinitions?'],
  'impact': 'This programme connects foundational mechanics without boost symmetry to reproducible numerical '
            'experiments and computational search. A successful result would turn microscopic dynamics into a '
            'controllable ingredient rather than a fixed background assumption.',
  'img': 'exotic-concept.png',
  'strands': ['Numerical Lifshitz / boost-agnostic hard-particle gas',
              'Dynamics-engineered maze and first-passage search',
              'Dispersion-engineered particle swarm optimisation']},
 {'slug': 'multiscale',
  'status': 'Active',
  'title': 'Fluctuations, memory and non-equilibrium dynamics',
  'kicker': 'Schwinger-Keldysh EFT · noise · rare events',
  'summary': 'We develop effective theories of fluctuations, memory and rare events in systems driven away from '
             'equilibrium. Schwinger-Keldysh methods let us connect dissipation to noise, test whether non-Gaussian '
             'stochastic sectors correspond to genuine positive probabilities, and keep track of memory when '
             'additional relaxation modes are resolved or integrated out.',
  'questions': ['Which non-Gaussian noise couplings are compatible with positive probability distributions and thermal '
                'KMS symmetry?',
                'How does integrating out relaxation modes generate memory, coloured noise and scale-dependent '
                'stochastic transport?',
                'How can effective theories describe rare events, Brownian motion and local detailed balance beyond '
                'the Gaussian hydrodynamic limit?'],
  'impact': 'The programme turns consistency conditions such as positivity, causality and KMS symmetry into '
            'quantitative constraints on stochastic dynamics. It links hydrodynamics to large-deviation theory, '
            'open-system dynamics and coarse graining while retaining explicit control of non-hydrodynamic memory.',
  'img': 'fluctuations-concept.png',
  'strands': ['Positive stochastic completion and optimisation of non-Gaussian noise',
              'Spectral RG matching of positive-noise Schwinger-Keldysh EFTs',
              'Large deviations and contraction to macroscopic fluctuation theory',
              'Maxwell-Cattaneo memory, temperature and velocity modes',
              'Modified KMS / local detailed balance and Brownian-particle couplings']},
 {'slug': 'relaxation',
  'status': 'Active',
  'title': 'Relaxation and driven steady states in holography and beyond',
  'kicker': 'Quasihydrodynamics · holography · transport',
  'summary': 'We study driven systems that settle into non-equilibrium steady states because forcing is balanced by '
             'relaxation. Gauge-gravity duality supplies controlled strongly coupled examples, while '
             'quasihydrodynamics organises approximately conserved quantities and other long-lived degrees of freedom.',
  'questions': ['Which relaxation terms are compatible with symmetry, thermodynamics and microscopic response?',
                'How do long-lived non-hydrodynamic modes modify transport in driven states?',
                'When can holographic steady states be captured by a local effective theory?'],
  'impact': 'The programme links holography, anomalous transport and effective field theory, with applications to '
            'strongly correlated materials and more general driven many-body systems.',
  'img': 'relaxation-concept.png',
  'strands': ['Electrically driven non-equilibrium steady states',
              'Relaxed and anomalous hydrodynamics',
              'Holographic models of long-lived modes and transport']},
 {'slug': 'flocks',
  'status': 'On hiatus',
  'title': 'Simulating herds, flocks and swarms',
  'kicker': 'Collective motion · flocking · computation',
  'summary': 'We use collective-motion models as a numerical laboratory for non-equilibrium hydrodynamics. The '
             'programme connects Vicsek- and Toner-Tu-type dynamics, boost-agnostic effective theories and '
             'quenched-disorder tests of collective flow.',
  'questions': ['How do thermodynamic and symmetry constraints restrict effective theories of flocking matter?',
                'Which steady states and interfaces survive beyond mean-field descriptions?',
                'How robust are predicted scaling relations when microscopic alignment rules are disordered or '
                'quenched?'],
  'impact': 'The same mathematical structures appear in biological swarms, active materials and traffic-like flows. '
            'Collective motion therefore provides a concrete arena in which to test how symmetry, fluctuations and '
            'disorder shape non-equilibrium phases.',
  'img': 'flocks-concept.png',
  'strands': ['Boost-agnostic hydrodynamic constraints on flocking',
              'Quenched Vicsek tests and disorder',
              'Collective-motion simulations and scaling']},
 {'slug': 'superconductive',
  'status': 'On hiatus',
  'title': 'The superconductive field effect',
  'kicker': 'Superconductivity · strong fields · quantum devices',
  'summary': 'We investigate the suppression of superconductivity by strong electric fields in thin films and related '
             'structures. A central idea is the analogy between superconducting quasiparticles and relativistic '
             'quantum fields, including a superconducting counterpart of Schwinger pair production.',
  'questions': ['How can static electric fields modify superconductivity despite conventional screening arguments?',
                'Which microscopic mechanisms reproduce experimentally observed field effects?',
                'Can electrically controlled superconductivity be turned into useful device architectures?'],
  'impact': 'The work connects condensed-matter physics and quantum field theory while motivating low-dissipation, '
            'electrically tunable superconducting elements.',
  'img': 'superconductive-concept.png',
  'strands': ["Microscopic Gor'kov / Bogoliubov-de Gennes response",
              'Sauter-Schwinger analogy in BCS superconductors',
              'Electrostatic control and device-motivated modelling']}]

STATUS_ORDER = {
    'open': 0,
    'active': 0,
    'on hiatus': 1,
    'hiatus': 1,
    'closed': 2,
}

def project_sort_key(project):
    return (STATUS_ORDER.get(project.get('status', 'active').lower(), 99), project['title'].casefold())

ordered_projects = sorted(projects, key=project_sort_key)

team = [
    {
        'name':'Andrea Amoretti','role':'Associate Professor','email':'andrea.amoretti@unige.it',
        'bio':"Andrea's research sits at the interface of high-energy theory, condensed-matter physics and statistical field theory. He trained at the University of Genoa, completing a PhD on AdS/CFT and its applications, and then held postdoctoral positions at the University of Cambridge, the University of Wuerzburg and the Universite libre de Bruxelles before returning to Genoa, where he is now Associate Professor. His research connects hydrodynamic effective theory, gauge-gravity duality and conformal methods to strongly correlated matter, spanning transport in quantum critical systems, strong-field effects in superconductors, conformal perturbation theory near critical points and topological quantum field theories with boundaries. At the STELLAR Lab, he develops effective descriptions of strongly interacting and non-equilibrium systems, including driven fluids and active matter, combining statistical field theory, hydrodynamics, kinetic theory and holography.",
        'img':'andrea.jpg','orcid':'0000-0002-5911-3689','website':'https://www.ge.infn.it/~amoretti/','website_label':'Personal website',
        'profile':'https://rubrica.unige.it/personale/U0tHUl1g','profile_label':'UniGe profile',
        'cv':'assets/cv/andrea-amoretti.pdf','cv_label':'CV (PDF)'
    },
    {
        'name':'Nicodemo Magnoli','role':'Associate Professor','email':'nicodemo.magnoli@ge.infn.it',
        'bio':"Nico's research spans statistical and conformal field theory, critical phenomena and non-perturbative questions in quantum field theory. At the University of Genoa and INFN Genova he has developed conformal perturbation theory as a practical tool for moving away from critical points, including quantitative comparisons with lattice gauge theory. His more recent work also studies effective-string descriptions of confining flux tubes and how universal critical behaviour emerges across continuum and lattice formulations. At the STELLAR Lab, he anchors the statistical-field-theory programme, with particular emphasis on conformal methods, confinement, universality and phase transitions.",
        'img':'nicodemo.jpg','orcid':'0000-0001-5372-4836','website':None,
        'profile':'https://rubrica.unige.it/personale/VUZEUllg','profile_label':'UniGe profile'
    },
    {
        'name':'Daniel K. Brattan','role':'Senior Research Associate (ricercatore tipo A)','email':'daniel.keith.brattan@edu.unige.it',
        'bio':"Daniel's research spans hydrodynamics, non-equilibrium effective theory and gauge-gravity duality, with a particular interest in how collective descriptions fail, reorganise or acquire additional long-lived degrees of freedom. He earned his PhD in string theory at Durham University and subsequently held postdoctoral positions at the Technion, the University of Science and Technology of China, INFN Genova and Ecole Polytechnique before joining the University of Genoa as a researcher. His work has included holographic quantum liquids, anyonic systems, quasihydrodynamics, anomalous transport, active matter and boost-agnostic Hamiltonian and kinetic theory. At the STELLAR Lab, he works on Schwinger-Keldysh effective theory, non-Gaussian noise and positivity, hydrodynamics beyond isolated poles, driven steady states and the use of non-Galilean dynamics in statistical and computational problems.",
        'img':'daniel.jpg','orcid':'0000-0002-7182-7019','website':'https://www.ge.infn.it/~dbrattan/',
        'profile':None,'profile_label':None,
        'cv':'assets/cv/daniel-brattan.pdf','cv_label':'CV (PDF)'
    },
    {
        'name':'Shuvayu Roy','role':'Postdoctoral researcher','email':'shuvayu.roy.physics@gmail.com',
        'bio':"Shuvayu's research spans relativistic hydrodynamics, effective field theories of gravity, and their inter-connections through holography. He began his PhD work on black-hole thermodynamics in higher-derivative theories of gravity and the fluid-gravity duality, before extending his interests to stability and causality in relativistic hydrodynamics through dispersion relations and field redefinitions. After completing his PhD at NISER, India, he worked on tidal deformations of black holes as a postdoctoral fellow at IIT Gandhinagar. At the STELLAR Lab, he works on hydrodynamic fluctuations in stable-causal theories of hydrodynamics and on a first-principles understanding of active-matter hydrodynamics using Schwinger-Keldysh effective field theory.",
        'img':'shuvayu.jpg','orcid':'0000-0002-5725-5712','website':None,
        'profile':None,'profile_label':None,
        'cv':'assets/cv/shuvayu-roy.pdf','cv_label':'CV (PDF)'
    },
    {
        'name':'Giorgos Batzios','role':'Postdoctoral researcher','email':'g.batzios@uva.nl',
        'bio':"Giorgos's research connects holography, effective field theory, hydrodynamics and generalized global symmetries. He completed his doctoral work at the Institute for Theoretical Physics at the University of Amsterdam, where he studied holographic duals of the N=1* gauge theory and related gravitational constructions. His subsequent work has explored higher-group symmetries and brane dynamics as well as the emergence of the chiral anomaly from spin hydrodynamics. At the STELLAR Lab, he works on hydrodynamic and holographic effective theories in which symmetry, anomaly structure and additional collective degrees of freedom constrain transport and long-distance dynamics.",
        'img':'giorgos.webp','orcid':'0009-0003-3955-4668','website':None,
        'profile':None,'profile_label':None
    },
    {
        'name':'Matteo Anselmi','role':'Doctoral candidate','email':'matteo.anselmi@ge.infn.it',
        'bio':"Matteo's research spans quantum field theory, hydrodynamics and non-equilibrium effective theory, with a particular interest in how infrared descriptions are related by duality and constrained by symmetry. During his Master's degree at the University of Genoa, he studied infrared dualities between three-dimensional quantum field theories, especially bosonisation dualities involving Majorana fermions and their connection to topological phases of matter. He is now a PhD candidate in theoretical physics at Genoa, where his work has included both relativistic and boost-agnostic hydrodynamics, the latter providing an effective description relevant to systems such as active matter. At the STELLAR Lab, he is developing Schwinger-Keldysh effective field theory for non-equilibrium physics, with current work on Maxwell-Cattaneo transport and the effective description of non-hydrodynamic poles and branch cuts.",
        'img':'matteo.png','orcid':'0009-0006-8268-6625','website':None,
        'profile':None,'profile_label':None,
        'cv':'assets/cv/matteo-anselmi.pdf','cv_label':'CV (PDF)'
    }
]

associates = [
    {
        'name':'Jewel Kumar Ghosh',
        'role':'STELLAR Associate · Assistant Professor, Independent University, Bangladesh',
        'email':'jewel.ghosh@iub.edu.bd',
        'bio':"Jewel's research spans holography, relativistic hydrodynamics, black-hole physics and quantum field theory. He completed his PhD in Paris in 2019 on holographic renormalisation-group flows on curved manifolds and subsequently held a postdoctoral fellowship at ICTS-TIFR before joining Independent University, Bangladesh. His work has developed from holographic RG flows and black holes toward anomalous transport, scale-invariant but non-conformal fluids, hydrostatics in multi-Weyl systems and fluctuating effective dynamics. As a STELLAR Associate, he collaborates with the group on holographic constraints on hydrodynamic effective theories, the analytic structure of response and the limits of hydrodynamic and hydrostatic expansions.",
        'img':'https://ccds.ai/api/media/file/Dr._Jewel_Kumar_Ghosh_-180x180.webp',
        'orcid':None,
        'website':'https://ccds.ai/people/jewel-kumar-ghosh',
        'website_label':'CCDS profile',
        'profile':'https://www.icts.res.in/people/jewel-kumar-ghosh',
        'profile_label':'ICTS profile'
    }
]

former = [
    {
        'name':'Alkistis Zervou','role':'Former postdoctoral researcher',
        'bio':"Alkistis's research spans strongly correlated condensed matter, phase competition and superconductivity. She completed her PhD at Loughborough University, where she studied competing orders near higher-order van Hove singularities using renormalisation-group methods. At STELLAR she worked on the superconductive field effect, developing numerical solutions of generalized Gor'kov equations in applied electric fields and connecting microscopic superconductivity to the group's strong-field programme.",
        'links':[('Research profile','https://www.researchgate.net/profile/Alkistis-Zervou')]
    },
    {
        'name':'Jonas Rongen','role':'Former doctoral researcher',
        'bio':"Jonas's doctoral research at the University of Genoa focused on quasihydrodynamics, anomalous transport and the effective description of response beyond the strictly hydrodynamic regime. His work with STELLAR included anomalous transport in Weyl semimetals, dissipative electrically driven fluids and the construction of linear effective theories with additional non-hydrodynamic poles. From December 2026 he joins TheoryLab at Shanghai Jiao Tong University in Shanghai, China, as a postdoctoral fellow in Matteo Baggioli's group.",
        'links':[('Next position','https://theorylab-sjtu.com/index.php/members/')]
    },
    {
        'name':'Luca Martinoia','role':'Former doctoral and postdoctoral researcher',
        'bio':"Luca completed his PhD in theoretical physics at the University of Genoa in 2024 with the thesis Developments in quasihydrodynamics. At STELLAR he worked on anomalous and relaxed hydrodynamics, Weyl-semimetal transport and the hydrodynamics of active matter, including exact scaling results for flocking systems. After a postdoctoral position at the LIPh Lab in Padua working on theoretical neuroscience, he moved into research and development and is now an algorithm developer at Rulex in Genoa.",
        'links':[('Personal website','https://lucamartinoia.github.io/')]
    },
    {
        'name':'Ioannis Matthaiakakis','role':'Former postdoctoral researcher',
        'bio':"Ioannis's research spans gravity, holography, quantum field theory and hydrodynamics, with an emphasis on applying high-energy methods to condensed-matter systems. He completed his PhD at the University of Wuerzburg in 2021 and joined the University of Genoa as a postdoctoral researcher, where he worked with STELLAR on anomalous and relaxed hydrodynamics, transport and superconductivity. In October 2023 he moved to the University of Southampton, where he is an STFC Research Fellow in mathematical and theoretical physics.",
        'links':[('Southampton profile','https://www.southampton.ac.uk/people/657ygy/doctor-ioannis-matthaiakakis')]
    },
    {
        'name':'Marcello Scanavino','role':'Former doctoral researcher',
        'bio':"Marcello completed his doctoral work at the University of Genoa on critical phenomena, conformal perturbation theory and holography, including quantitative tests of conformal methods against lattice gauge theory. His thesis, Perturbing critical phenomena: from CPT to Holography, connected the group's statistical-field-theory and gauge-gravity programmes. After leaving academic research he moved into the technology sector and now works at Accenture Italia.",
        'links':[('Professional profile','https://it.linkedin.com/in/marcello-scanavino-115a30131')]
    }
]

# Persistent scholarly-profile links. Where an exact INSPIRE or Web of Science
# author record is verified, link directly to it; otherwise use the service's author search
# rather than inventing an identifier.
SCHOLARLY_PROFILES = {
    'Andrea Amoretti': {
        'inspire':'https://inspirehep.net/authors/1258948',
        'arxiv':'https://arxiv.org/search/?query=Andrea+Amoretti&searchtype=author&abstracts=show&order=-announced_date_first&size=50',
        'wos':'https://www.webofscience.com/wos/author/record/ABI-3013-2020'},
    'Nicodemo Magnoli': {
        'inspire':'https://inspirehep.net/authors/1040503',
        'arxiv':'https://arxiv.org/search/?query=Nicodemo+Magnoli&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
    'Daniel K. Brattan': {
        'inspire':'https://inspirehep.net/authors/1270146',
        'arxiv':'https://arxiv.org/search/?query=Daniel+K.+Brattan&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
    'Shuvayu Roy': {
        'inspire':'https://inspirehep.net/authors/2140814',
        'arxiv':'https://arxiv.org/search/?query=Shuvayu+Roy&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
    'Giorgos Batzios': {
        'inspire':'https://inspirehep.net/authors?sort=bestmatch&size=25&page=1&q=Giorgos%20Batzios',
        'arxiv':'https://arxiv.org/search/?query=Giorgos+Batzios&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
    'Matteo Anselmi': {
        'inspire':'https://inspirehep.net/authors?sort=bestmatch&size=25&page=1&q=Matteo%20Anselmi',
        'arxiv':'https://arxiv.org/search/?query=Matteo+Anselmi&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
    'Jewel Kumar Ghosh': {
        'inspire':'https://inspirehep.net/authors?sort=bestmatch&size=25&page=1&q=Jewel%20Kumar%20Ghosh',
        'arxiv':'https://arxiv.org/search/?query=Jewel+Kumar+Ghosh&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
    'Alkistis Zervou': {
        'inspire':'https://inspirehep.net/authors?sort=bestmatch&size=25&page=1&q=Alkistis%20Zervou',
        'arxiv':'https://arxiv.org/search/?query=Alkistis+Zervou&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
    'Jonas Rongen': {
        'inspire':'https://inspirehep.net/authors?sort=bestmatch&size=25&page=1&q=Jonas%20Rongen',
        'arxiv':'https://arxiv.org/search/?query=Jonas+Rongen&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
    'Luca Martinoia': {
        'inspire':'https://inspirehep.net/authors?sort=bestmatch&size=25&page=1&q=Luca%20Martinoia',
        'arxiv':'https://arxiv.org/search/?query=Luca+Martinoia&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
    'Ioannis Matthaiakakis': {
        'inspire':'https://inspirehep.net/authors/1684074',
        'arxiv':'https://arxiv.org/search/?query=Ioannis+Matthaiakakis&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
    'Marcello Scanavino': {
        'inspire':'https://inspirehep.net/authors?sort=bestmatch&size=25&page=1&q=Marcello%20Scanavino',
        'arxiv':'https://arxiv.org/search/?query=Marcello+Scanavino&searchtype=author&abstracts=show&order=-announced_date_first&size=50',},
}

research_students = [
    {
        'year':'2025',
        'name':'Matteo Anselmi',
        'title':'Dualità infrarosse per fermioni di Majorana',
        'note':'Matteo’s Master’s thesis studied infrared dualities between three-dimensional quantum field theories, with particular emphasis on Majorana fermions, bosonisation and their relation to topological phases of matter.',
        'link':'https://unire.unige.it/handle/123456789/2598/recent-submissions?locale-attribute=it&offset=3960',
        'link_label':'UniRe thesis record'
    },
    {
        'year':'2025',
        'name':'Andrea Parodi',
        'title':'Quasihydrodynamic Perturbations about Electrically Driven Steady States',
        'note':'Andrea’s Master’s thesis developed the perturbative description of electrically driven stationary states in quasihydrodynamics, with particular emphasis on the gradient expansion and the response of holographic probe-brane steady states to spatially varying electric fields.',
        'link':'https://unire.unige.it/bitstream/handle/123456789/12874/tesi33968836.pdf?sequence=1',
        'link_label':'Master’s thesis (PDF)'
    },
    {
        'year':'2024',
        'name':'Emanuele Falchi',
        'title':'Effective quasihydrodynamics of the probe brane in the chiral symmetry broken phase',
        'note':'Emanuele’s Master’s work used holographic probe-brane dynamics to study quasihydrodynamic degrees of freedom and their effective description in a phase with broken chiral symmetry.',
        'link':'https://corsi.unige.it/sites/corsi.unige.it/files/2025-01/Laurea%20FISICA%20LM%20seduta%2011-02-2025%20h14%2C30.pdf',
        'link_label':'UniGe thesis defence record'
    },
    {
        'year':'2023',
        'name':'Francesco Puppo',
        'title':'A running Planck Mass. The connection between Adiabatic Renormalization and the Effective Field Theory of Dark Energy',
        'note':'Francesco’s Master’s project examined how a scale-dependent effective Planck mass appears in renormalised gravity and how that description connects to the effective field theory of dark energy.'
    },
    {
        'year':'2021',
        'name':'Luca Maranzana',
        'title':'Teoria effettiva olografica di una charge density wave termodinamicamente stabile',
        'note':'Luca’s Master’s thesis studied holographic charge-density-wave phases with spontaneously broken translations, including Ward identities and a Q-lattice construction in which the ordered phase is thermodynamically stable.',
        'link':'https://unire.unige.it/handle/123456789/4233',
        'link_label':'UniRe thesis record'
    },
    {
        'year':'2020',
        'name':'Luca Martinoia',
        'title':'Anomalous hydrodynamic description of thermoelectric transport in a Weyl semimetal',
        'note':'Luca’s Master’s thesis applied relativistic anomalous hydrodynamics to thermoelectric transport in Weyl semimetals, including the effects of the chiral anomaly, magnetic field and weak relaxation.',
        'link':'https://lucamartinoia.github.io/assets/pdf/papers/Thesis_LM_final.pdf',
        'link_label':'Master’s thesis (PDF)'
    }
]

publications = [
(2026,'When duality changes the poles: SL(2,ℤ) transformations of linear response EFTs','arXiv:2609.19075'),
(2026,'Schwinger-Keldysh effective actions for non-hydrodynamic poles and branch cuts','arXiv:2609.16164'),
(2026,'The price of locality: Maxwell-Cattaneo charge transport in Schwinger-Keldysh effective field theory','arXiv:2609.13378'),
(2026,'Staying positive: bounds for non-Gaussian noise in Schwinger-Keldysh effective field theory','arXiv:2609.12050'),
(2026,'Linear response beyond hydrodynamic poles','JHEP 07 (2026) 092'),
(2025,'A new web of dualities from Majorana Fermions','arXiv:2511.22261'),
(2025,'The Hamiltonian mechanics of exotic particles','Journal of Statistical Mechanics 12, 123201'),
(2025,'A note on the canonical approach to hydrodynamics and linear response theory','Acta Physica Polonica B 56, 1-A4'),
(2024,'Dissipative electrically driven fluids','JHEP 12, 114'),
(2024,'Thermodynamic constraints and exact scaling exponents of flocking matter','Physical Review E 110, 054108'),
(2024,'Relaxed hydrodynamic theory of electrically driven nonequilibrium steady states','Physical Review Research 6, 043097'),
(2024,'Confining strings in three-dimensional gauge theories beyond the Nambu-Gotō approximation','JHEP 08, 198'),
(2024,'Relaxation terms for anomalous hydrodynamic transport in Weyl semimetals from kinetic theory','JHEP 02, 071'),
(2023,'Restoring time-reversal covariance in relaxed hydrodynamics','Physical Review D 108'),
(2023,'Leading order magnetic field dependence of conductivities in anomalous hydrodynamics','Physical Review D 108'),
(2023,'Non-dissipative electrically driven fluids','JHEP 05, 218'),
(2022,'Destroying superconductivity in thin films with an electric field','Physical Review Research 4, 033211'),
(2022,'Superconductors in strong electric fields: Quantum Electrodynamics meets Superconductivity','Journal of Physics: Conference Series 2531, 012001'),
(2022,'On the hydrodynamics of (2 + 1)-dimensional strongly coupled relativistic theories in an external magnetic field','Modern Physics Letters A 37, 2230010'),
(2022,'Learning to predict target location with turbulent odor plumes','eLife'),
(2022,'Fine corrections in the effective string describing SU(2) Yang-Mills theory in three dimensions','JHEP 03, 115'),
(2021,'Hydrodynamic magneto-transport in holographic charge density wave states','JHEP 11, 011'),
(2021,'On the behaviour of the interquark potential in the vicinity of the deconfinement transition','38th International Symposium on Lattice Field Theory'),
(2021,'Hydrodynamic magneto-transport in charge density wave states','JHEP 2021(05):27'),
(2020,'Magneto-thermal transport implies an incoherent Hall conductivity','JHEP 08, 097'),
(2020,'Energy trapped Ising model','Physical Review D 102, 036018'),
(2020,'Sauter-Schwinger effect in a Bardeen-Cooper-Schrieffer superconductor','Physical Review Letters 126, 117001'),
(2020,'Hydrodynamical description for magneto-transport in the strange metal phase of Bi-2201','Physical Review Research 2, 023387'),
(2020,'How to construct a holographic EFT for phonons','Proceedings of Science 384'),
(2020,'Gapless and gapped holographic phonons','JHEP 01, 058'),
(2019,'Universal relaxation in a holographic metallic density wave phase','Physical Review Letters 123, 211602'),
(2019,'Diffusion and universal relaxation of holographic phonons','JHEP 10, 068'),
(2019,'Conformal perturbation theory confronts lattice results in the vicinity of a critical point','Physical Review D 100, 034512'),
(2018,'Effective holographic theory of charge density waves','Physical Review D 97, 086017'),
(2018,'DC resistivity of quantum critical, charge density wave states from gauge-gravity duality','Physical Review Letters 120, 171603'),
(2017,'Conformal perturbation theory','Physical Review D 96, 045016'),
(2016,'Conformal perturbation of off-critical correlators in the 3D Ising universality class','Physical Review D 94, 026005'),
(2016,'Chasing the cuprates with dilatonic dyons','JHEP 06, 113'),
(2015,'Bounds on charge and heat diffusivities in momentum dissipating holography','JHEP 07, 102'),
(2015,'Analytic dc thermoelectric conductivities in holography with massive gravitons','Physical Review D 91, 025002'),
(2014,'Thermo-electric transport in gauge/gravity models with momentum dissipation','JHEP 09, 160'),
(2014,'Holography in flat spacetime: 4D theories and electromagnetic duality on the border','Physical Review D 91, 025002'),
(2013,'Coexistence of two vector order parameters: a holographic model for ferromagnetic superconductivity','JHEP 01, 054'),
(2013,'3+1D Massless Weyl spinors from bosonic scalar-tensor duality','Advances in High Energy Physics 2014, 635286'),
(2013,'Duality and Dimensional Reduction of 5D BF Theory','European Physical Journal C 73, 2461'),
(2012,'The dynamics on the three-dimensional boundary of the 4D Topological BF model','New Journal of Physics 14, 113014'),
(2006,'Potts correlators and the static three-quark potential','Journal of Statistical Mechanics P03008'),
(2001,'Exact consequences of the trace anomaly in four-dimensions','Nuclear Physics B 618, 371-406'),
(1999,'Short distance behavior of correlators in the 2-D Ising model in a magnetic field','Nuclear Physics B 579, 635-666'),
(1997,'Vacuum expectation values from a variational approach','Physics Letters B 411, 127-133'),
(1996,'On the short distance behavior of the critical Ising model perturbed by a magnetic field','Nuclear Physics B 483, 563-579'),
(1995,'All order IR finite expansion for short distance behavior of massless theories perturbed by a relevant operator','Nuclear Physics B 471, 361-388'),
(1990,'Tests of QCD from jets on the Z0 peak','Physics Letters B 252, 271-281'),
(1990,'Duality and supersymmetry breaking in string theory','Physics Letters B 245, 409-416'),
(1988,'Spontaneous Breaking of Local Supersymmetry by Gravitational Instantons','Nuclear Physics B 309, 201'),
]


ARXIV = {
'When duality changes the poles: SL(2,ℤ) transformations of linear response EFTs':'2609.19075',
'Schwinger-Keldysh effective actions for non-hydrodynamic poles and branch cuts':'2609.16164',
'The price of locality: Maxwell-Cattaneo charge transport in Schwinger-Keldysh effective field theory':'2609.13378',
'Staying positive: bounds for non-Gaussian noise in Schwinger-Keldysh effective field theory':'2609.12050',
'Linear response beyond hydrodynamic poles':'2512.19694',
'A new web of dualities from Majorana Fermions':'2511.22261',
'The Hamiltonian mechanics of exotic particles':'2506.13848',
'A note on the canonical approach to hydrodynamics and linear response theory':'2408.10698',
'Dissipative electrically driven fluids':'2407.18856',
'Thermodynamic constraints and exact scaling exponents of flocking matter':'2405.02283',
'Relaxed hydrodynamic theory of electrically driven nonequilibrium steady states':'2404.05568',
'Confining strings in three-dimensional gauge theories beyond the Nambu-Gotō approximation':'2407.10678',
'Relaxation terms for anomalous hydrodynamic transport in Weyl semimetals from kinetic theory':'2309.05692',
'Restoring time-reversal covariance in relaxed hydrodynamics':'2304.01248',
'Leading order magnetic field dependence of conductivities in anomalous hydrodynamics':'2212.09761',
'Non-dissipative electrically driven fluids':'2211.05791',
'Destroying superconductivity in thin films with an electric field':'2202.00687',
'On the hydrodynamics of (2 + 1)-dimensional strongly coupled relativistic theories in an external magnetic field':'2209.11589',
'Learning to predict target location with turbulent odor plumes':'2106.08988',
'Fine corrections in the effective string describing SU(2) Yang-Mills theory in three dimensions':'2109.06212',
'Hydrodynamic magneto-transport in holographic charge density wave states':'2107.00519',
'On the behaviour of the interquark potential in the vicinity of the deconfinement transition':'2203.11504',
'Hydrodynamic magneto-transport in charge density wave states':'2101.05343',
'Magneto-thermal transport implies an incoherent Hall conductivity':'2005.09662',
'Energy trapped Ising model':'2007.07150',
'Sauter-Schwinger effect in a Bardeen-Cooper-Schrieffer superconductor':'2007.08323',
'Hydrodynamical description for magneto-transport in the strange metal phase of Bi-2201':'1909.07991',
'Gapless and gapped holographic phonons':'1910.11330',
'Universal relaxation in a holographic metallic density wave phase':'1812.08118',
'Diffusion and universal relaxation of holographic phonons':'1904.11445',
'Conformal perturbation theory confronts lattice results in the vicinity of a critical point':'1904.12749',
'Effective holographic theory of charge density waves':'1711.06610',
'DC resistivity of quantum critical, charge density wave states from gauge-gravity duality':'1712.07994',
'Conformal perturbation theory':'1705.03502',
'Conformal perturbation of off-critical correlators in the 3D Ising universality class':'1605.05133',
'Chasing the cuprates with dilatonic dyons':'1603.03029',
'Bounds on charge and heat diffusivities in momentum dissipating holography':'1411.6631',
'Analytic dc thermoelectric conductivities in holography with massive gravitons':'1407.0306',
'Thermo-electric transport in gauge/gravity models with momentum dissipation':'1406.4134',
'Holography in flat spacetime: 4D theories and electromagnetic duality on the border':'1401.7101',
'Coexistence of two vector order parameters: a holographic model for ferromagnetic superconductivity':'1309.5093',
'3+1D Massless Weyl spinors from bosonic scalar-tensor duality':'1308.6674',
'Duality and Dimensional Reduction of 5D BF Theory':'1301.3688',
'The dynamics on the three-dimensional boundary of the 4D Topological BF model':'1205.6156',
'Potts correlators and the static three-quark potential':'hep-th/0511168',
'Exact consequences of the trace anomaly in four-dimensions':'hep-th/0103237',
'Short distance behavior of correlators in the 2-D Ising model in a magnetic field':'hep-th/9909065',
'Vacuum expectation values from a variational approach':'hep-th/9706017',
'On the short distance behavior of the critical Ising model perturbed by a magnetic field':'hep-th/9606072',
'All order IR finite expansion for short distance behavior of massless theories perturbed by a relevant operator':'hep-th/9511209',
}

awards = [
('2025-2028','Further beyond hydrodynamics','PNRR Missione 4','CUP D33C25000470006','€300,000'),
('','Flow Lensing of Gravitational Waves','PNRR, Spoke 2 (PUB5)','','€120,000'),
('2021-2023','Beyond hydrodynamics','H2020 Marie Skłodowska-Curie Actions','Grant 101030915','€183,000'),
('2023','Gate-induced microscopic effects on superconducting quantum devices','PRIN 2022','','€80,000'),
('2023','Conformal Perturbation Theory: from Effective String Theory applications to Statistical Mechanics realizations','PRIN 2022','','€103,000'),
('2020','Superconductors in strong electric fields: paving the way to electrically controlled superconductive devices','Curiosity Driven Grant, Università di Genova','','€63,000'),
]

project_pubs = {'analytic': [('2026',
               'When duality changes the poles: SL(2,ℤ) transformations of linear response EFTs',
               'arXiv:2609.19075'),
              ('2026',
               'Schwinger-Keldysh effective actions for non-hydrodynamic poles and branch cuts',
               'arXiv:2609.16164'),
              ('2026', 'Linear response beyond hydrodynamic poles', 'JHEP 07 (2026) 092')],
 'critical': [('2025', 'A new web of dualities from Majorana Fermions', 'arXiv:2511.22261'),
              ('2024',
               'Confining strings in three-dimensional gauge theories beyond the Nambu-Gotō approximation',
               'JHEP 08, 198'),
              ('2022',
               'Fine corrections in the effective string describing SU(2) Yang-Mills theory in three dimensions',
               'JHEP 03, 115'),
              ('2021',
               'On the behaviour of the interquark potential in the vicinity of the deconfinement transition',
               '38th International Symposium on Lattice Field Theory'),
              ('2020', 'Energy trapped Ising model', 'Physical Review D 102, 036018'),
              ('2019',
               'Conformal perturbation theory confronts lattice results in the vicinity of a critical point',
               'Physical Review D 100, 034512'),
              ('2017', 'Conformal perturbation theory', 'Physical Review D 96, 045016')],
 'exotic': [('2025', 'The Hamiltonian mechanics of exotic particles', 'Journal of Statistical Mechanics 12, 123201')],
 'multiscale': [('2026',
                 'The price of locality: Maxwell-Cattaneo charge transport in Schwinger-Keldysh effective field theory',
                 'arXiv:2609.13378'),
                ('2026',
                 'Staying positive: bounds for non-Gaussian noise in Schwinger-Keldysh effective field theory',
                 'arXiv:2609.12050'),
                ('2025',
                 'A note on the canonical approach to hydrodynamics and linear response theory',
                 'Acta Physica Polonica B 56, 1-A4')],
 'relaxation': [('2024', 'Dissipative electrically driven fluids', 'JHEP 12, 114'),
                ('2024',
                 'Relaxed hydrodynamic theory of electrically driven nonequilibrium steady states',
                 'Physical Review Research 6, 043097'),
                ('2024',
                 'Relaxation terms for anomalous hydrodynamic transport in Weyl semimetals from kinetic theory',
                 'JHEP 02, 071'),
                ('2023', 'Restoring time-reversal covariance in relaxed hydrodynamics', 'Physical Review D 108'),
                ('2023',
                 'Leading order magnetic field dependence of conductivities in anomalous hydrodynamics',
                 'Physical Review D 108'),
                ('2023', 'Non-dissipative electrically driven fluids', 'JHEP 05, 218'),
                ('2019',
                 'Universal relaxation in a holographic metallic density wave phase',
                 'Physical Review Letters 123, 211602'),
                ('2019', 'Diffusion and universal relaxation of holographic phonons', 'JHEP 10, 068')],
 'flocks': [('2024',
             'Thermodynamic constraints and exact scaling exponents of flocking matter',
             'Physical Review E 110, 054108')],
 'superconductive': [('2022',
                      'Destroying superconductivity in thin films with an electric field',
                      'Physical Review Research 4, 033211'),
                     ('2022',
                      'Superconductors in strong electric fields: Quantum Electrodynamics meets Superconductivity',
                      'Journal of Physics: Conference Series 2531, 012001'),
                     ('2020',
                      'Sauter-Schwinger effect in a Bardeen-Cooper-Schrieffer superconductor',
                      'Physical Review Letters 126, 117001')]}

project_talks = {'analytic': [],
 'critical': [{'title': 'Critical systems and conformal perturbation theory',
              'type': 'Seminar',
              'presenter': 'Andrea Amoretti',
              'date': '14 March 2018',
              'venue': 'Universidade de Santiago de Compostela, Spain',
              'url': 'https://www-fp.usc.es/~theory/sem1718.html',
              'url_label': 'Seminar programme',
              'related_url': 'https://arxiv.org/abs/1705.03502',
              'related_label': 'Related review: Conformal perturbation theory'},
             {'title': '3D dynamics of 4D topological BF Theory with boundary',
              'type': 'Conference talk',
              'presenter': 'Andrea Amoretti',
              'conference': 'Workshop and Conference on Geometrical Aspects of Quantum States in Condensed Matter',
              'date': '3 July 2013',
              'venue': 'ICTP, Trieste, Italy',
              'programme': 'https://indico.ictp.it/event/a12192/material/5/0.pdf',
              'related_url': 'https://arxiv.org/abs/1205.6156',
              'related_label': 'Related paper: arXiv:1205.6156'}],
 'exotic': [{'title': 'The Hamiltonian mechanics of exotic particles',
             'type': 'Conference talk',
             'presenter': 'Daniel K. Brattan',
             'conference': 'SigmaPhi 2026 - International Conference on Statistical Physics',
             'conference_dates': '6-10 July 2026',
             'date': '6 July 2026',
             'time': '15:20-15:40',
             'venue': 'Kolymvari, Chania, Crete, Greece',
             'authors': 'Andrea Amoretti, Daniel K. Brattan and Luca Martinoia',
             'abstract': 'We develop Hamiltonian mechanics on Aristotelian manifolds, which lack local boost symmetry '
                         'and admit absolute time and space structures. We construct invariant phase space dynamics, '
                         'define free Hamiltonians, and establish a generalised Liouville theorem. Conserved '
                         'quantities are identified via lifted Killing vectors. Extending to kinetic theory, we show '
                         'that the charge current and stress tensor reproduce ideal hydrodynamics at a leading order, '
                         'with the ideal gas law emerging universally. Our framework provides a geometric and '
                         'dynamical foundation for systems where boost invariance is absent, with applications '
                         'including but not limited to: condensed matter, active matter and optimisation dynamics.',
             'abstract_note': 'Abstract from the SigmaPhi 2026 conference material.',
             'url': 'https://www.sigmaphi.polito.it/',
             'url_label': 'Conference website',
             'programme': 'https://www.sigmaphi.polito.it/index.php/program-2026',
             'abstract_url': 'https://www.sigmaphi.polito.it/images/2026/Abstracts/BrattanD.pdf',
             'abstract_label': 'Individual conference abstract',
             'related_url': 'https://doi.org/10.1088/1742-5468/ae1572',
             'related_label': 'Published paper: J. Stat. Mech. (2025) 123201',
             'related_links': [('SigmaPhi 2026 abstract booklet',
                                'http://sigmaphisrv.polito.it/images/2026/sigmaphi_2026_abstracts.pdf'),
                               ('arXiv:2506.13848', 'https://arxiv.org/abs/2506.13848')]}],
 'multiscale': [{'title': 'When is hydrodynamic noise really noise? Detailed balance and positivity in fluctuating hydrodynamics',
                 'type': 'Workshop talk',
                 'presenter': 'Andrea Amoretti',
                 'conference': 'FRAME2026 - Fluctuations and RAndomness in Many-body Evolution',
                 'conference_dates': '16-18 September 2026',
                 'date': '17 September 2026',
                 'time': '12:20-12:40',
                 'venue': 'Institut Pascal, Université Paris-Saclay, Orsay, France',
                 'abstract': 'Schwinger-Keldysh effective theories of dissipative hydrodynamics contain non-Gaussian noise couplings that are constrained by symmetry but need not define a positive probability distribution. Requiring the noise sector to admit a genuine probabilistic interpretation imposes additional, sharp inequalities between cumulants. The resulting bounds can be saturated by explicit positive distributions and provide a direct way of deciding when a formal stochastic effective theory can actually be sampled as noise.',
                 'abstract_note': 'Summary based on the related paper; the FRAME2026 programme lists the talk but does not publish a separate abstract.',
                 'url': 'https://indico.ijclab.in2p3.fr/event/13796/',
                 'url_label': 'Conference website',
                 'programme': 'https://indico.ijclab.in2p3.fr/event/13796/timetable/?view=standard_numbered',
                 'related_url': 'https://arxiv.org/abs/2609.12050',
                 'related_label': 'Related paper: arXiv:2609.12050'},
                {'title': 'Fluctuation-dissipation beyond hydrodynamics: nonlinear Maxwell-Cattaneo in the '
                          'Schwinger-Keldysh formalism',
                 'type': 'Workshop talk',
                 'presenter': 'Daniel K. Brattan',
                 'conference': 'FRAME2026 - Fluctuations and RAndomness in Many-body Evolution',
                 'conference_dates': '16-18 September 2026',
                 'date': '18 September 2026',
                 'time': '15:00-15:20',
                 'venue': 'Institut Pascal, Université Paris-Saclay, Orsay, France',
                 'abstract': 'We determine when nonlinear Maxwell-Cattaneo charge transport admits a local Gaussian '
                             'Schwinger-Keldysh embedding with a modified dynamical KMS symmetry. Treating the '
                             'additional vector mode as intrinsically dissipative changes the entropy-current '
                             'analysis: hydrostatics no longer fixes every allowed improvement, while KMS invariance '
                             'supplies further constraints that are invisible at the level of hydrodynamics alone. The '
                             'resulting construction gives a stochastic quasihydrodynamic interpretation of charge '
                             'transport beyond the purely hydrodynamic pole.',
                 'abstract_note': 'Summary based on the related paper; the FRAME2026 contribution page does not '
                                  'publish a separate abstract.',
                 'url': 'https://indico.ijclab.in2p3.fr/event/13796/',
                 'url_label': 'Conference website',
                 'programme': 'https://indico.ijclab.in2p3.fr/event/13796/timetable/?view=standard_numbered',
                 'contribution': 'https://indico.ijclab.in2p3.fr/event/13796/contributions/43254/',
                 'related_url': 'https://arxiv.org/abs/2609.13378',
                 'related_label': 'Related paper: arXiv:2609.13378'}],
 'relaxation': [{'title': 'Holographic driven steady states',
                 'type': 'Workshop talk',
                 'presenter': 'Daniel K. Brattan',
                 'conference': 'Holographic perspectives on chiral transport and spin dynamics',
                 'conference_dates': '24-28 March 2025',
                 'date': '28 March 2025',
                 'time': '11:30-11:50',
                 'venue': 'ECT*, Villazzano (Trento), Italy',
                 'abstract': 'We ask when hydrodynamics can describe slow, long-wavelength fluctuations around an '
                             'electrically driven non-equilibrium steady state. When the first non-hydrodynamic '
                             'excitation relaxes parametrically slowly, it must be retained as an additional gapped '
                             'mode, leading to a relaxed hydrodynamic theory. Gauge-gravity duality then provides a '
                             'controlled ultraviolet-complete example in which the steady state and its fluctuations '
                             'can be computed explicitly, giving a concrete test of hydrodynamics beyond thermal '
                             'equilibrium.',
                 'abstract_note': 'Summary based on the related publication; the workshop programme does not publish a '
                                  'separate abstract.',
                 'url': 'https://indico.ectstar.eu/event/230/',
                 'url_label': 'Conference website',
                 'programme': 'https://indico.ectstar.eu/event/230/timetable/?view=standard',
                 'slides': 'https://indico.ectstar.eu/event/230/contributions/5368/attachments/3635/5230/danny_brattan.pdf',
                 'related_url': 'https://arxiv.org/abs/2404.05568',
                 'related_label': 'Related paper: arXiv:2404.05568'},
                {'title': 'Relaxed hydrodynamics and anomalies (an overview)',
                 'type': 'Workshop talk',
                 'presenter': 'Andrea Amoretti',
                 'conference': 'Holographic perspectives on chiral transport and spin dynamics',
                 'conference_dates': '24-28 March 2025',
                 'date': '27 March 2025',
                 'time': '11:30-11:50',
                 'venue': 'ECT*, Villazzano (Trento), Italy',
                 'abstract': 'This overview examines how explicit relaxation can be incorporated into hydrodynamics '
                             'without losing the symmetry properties expected of equilibrium response. Generic energy, '
                             'charge and momentum relaxation can spoil time-reversal covariance even when '
                             'Onsager-looking relations survive, motivating a minimal relaxed framework that restores '
                             'the correct two-point-function structure. In anomalous transport, the same logic '
                             'strongly constrains the admissible relaxation channels: requiring charge conservation, '
                             'Onsager reciprocity and finite DC transport exposes the open-system character of simple '
                             'relaxation models and connects the hydrodynamic description to kinetic theory.',
                 'abstract_note': 'Summary based on the two related publications; the workshop programme does not '
                                  'publish a separate abstract.',
                 'url': 'https://indico.ectstar.eu/event/230/',
                 'url_label': 'Conference website',
                 'programme': 'https://indico.ectstar.eu/event/230/timetable/?view=standard',
                 'slides_page': 'https://indico.ectstar.eu/event/230/timetable/?print=1&view=standard_numbered',
                 'slides_page_label': 'Slides (presentation.pdf) on conference page',
                 'related_links': [('Time-reversal covariance: arXiv:2304.01248', 'https://arxiv.org/abs/2304.01248'),
                                   ('Anomalous relaxation from kinetic theory: arXiv:2309.05692',
                                    'https://arxiv.org/abs/2309.05692')]},
                {'title': 'Holography, hydrodynamics and condensed matter experiments: a critical overview',
                 'type': 'Online seminar',
                 'presenter': 'Andrea Amoretti',
                 'conference': 'HoloTube - Fall 2020',
                 'date': '3 November 2020',
                 'time': '16:00 CET',
                 'venue': 'Online',
                 'url': 'https://projects.ift.uam-csic.es/holotube/fall-2020/',
                 'url_label': 'HoloTube programme'},
                {'title': 'How to construct a holographic EFT for phonons',
                 'type': 'Lecture series',
                 'presenter': 'Andrea Amoretti',
                 'conference': 'XV Modave Summer School in Mathematical Physics',
                 'conference_dates': '8-14 September 2019',
                 'venue': 'Modave, Belgium',
                 'abstract': 'A five-lecture introduction to holographic methods for condensed-matter systems, culminating in the effective description of charge-density-wave phases with spontaneously or pseudo-spontaneously broken translations and their phonon dynamics.',
                 'abstract_note': 'Summary based on the published lecture notes.',
                 'related_url': 'https://pos.sissa.it/384/001/pdf',
                 'related_label': 'Published lecture notes'},
                {'title': 'Dissipative electrically driven fluids',
                 'type': 'Workshop talk',
                 'presenter': 'Jonas Rongen',
                 'conference': 'Holographic perspectives on chiral transport and spin dynamics',
                 'conference_dates': '24-28 March 2025',
                 'date': '25 March 2025',
                 'time': '14:20-14:40',
                 'venue': 'ECT*, Villazzano (Trento), Italy',
                 'abstract': 'We consider entropy-generating charged-fluid flows that reach a steady state under a '
                             'driving electric field. Once a stationarity constraint is chosen, energy and momentum '
                             'relaxation are no longer independent but are tied together by the steady-state '
                             'conditions. Imposing Onsager reciprocity further forces the incoherent conductivity to '
                             'vanish, so it makes no contribution to the observable AC or DC charge conductivity. The '
                             'result sharply constrains dissipative hydrodynamic descriptions of electrically driven '
                             'steady states.',
                 'abstract_note': 'Summary based on the related publication; the workshop programme does not publish a '
                                  'separate abstract.',
                 'url': 'https://indico.ectstar.eu/event/230/',
                 'url_label': 'Conference website',
                 'programme': 'https://indico.ectstar.eu/event/230/timetable/?view=standard',
                 'slides_page': 'https://indico.ectstar.eu/event/230/timetable/?print=1&view=standard_numbered',
                 'slides_page_label': 'Slides (electrically driven fluids.pdf) on conference page',
                 'related_url': 'https://arxiv.org/abs/2407.18856',
                 'related_label': 'Related paper: arXiv:2407.18856'}],
 'flocks': [],
 'superconductive': [{'title': 'Superconductors in strong electric field: Quantum Electrodynamics meets superconductivity',
                      'type': 'Conference talk',
                      'presenter': 'Andrea Amoretti',
                      'conference': 'APS March Meeting 2023',
                      'date': '8 March 2023',
                      'time': '13:30-13:42',
                      'url': 'https://meetings-archive.aps.org/mar/2023/n27/',
                      'url_label': 'APS session',
                      'related_links': [('Destroying superconductivity in thin films with an electric field', 'https://arxiv.org/abs/2202.00687'),
                                        ('Sauter-Schwinger effect in a BCS superconductor', 'https://arxiv.org/abs/2011.09667')]},
                     {'title': 'Superconductors in strong electric fields: Quantum Electrodynamics meets Superconductivity',
                      'type': 'Workshop talk',
                      'presenter': 'Andrea Amoretti',
                      'conference': 'Avenues of Quantum Field Theory in Curved Spacetime (AQFTCS 2022)',
                      'conference_dates': '14-16 September 2022',
                      'venue': 'Genoa, Italy',
                      'url': 'https://unige.iris.cineca.it/handle/11567/1127115',
                      'url_label': 'Conference proceedings',
                      'related_url': 'https://doi.org/10.1088/1742-6596/2531/1/012001',
                      'related_label': 'Published proceedings contribution'},
                     {'title': 'Static Electric Field effect on the Superconductor: a microscopic approach',
                      'type': 'Conference poster',
                      'conference': '2025 Superconductivity Gordon Research Conference - Role of Topology, '
                                    'Dimensionality and Correlations in Unconventional Superconductivity',
                      'conference_dates': '4-9 May 2025',
                      'date': '4-9 May 2025',
                      'venue': 'Eurotel Victoria, Les Diablerets, Switzerland',
                      'abstract': 'Strong electrostatic fields can weaken superconductivity in metallic BCS thin films '
                                  'even though ordinary screening arguments suggest that static electric fields should '
                                  'have little effect. A microscopic route to this behaviour follows from the analogy '
                                  'between Bogoliubov-de Gennes quasiparticles and relativistic Dirac fermions: '
                                  'sufficiently strong electric fields can excite quasiparticle pairs from the '
                                  'superconducting condensate, while related effective descriptions predict a '
                                  'field-driven suppression of the superconducting gap and, at strong enough fields, a '
                                  'transition toward the normal state. The programme connects this microscopic picture '
                                  'to experimentally accessible observables in gated superconducting films.',
                      'abstract_note': 'Project summary based on the related STELLAR work. The public GRC programme '
                                       'lists poster sessions but does not publish individual poster abstracts.',
                      'url': 'https://www.grc.org/superconductivity-conference/2025/',
                      'url_label': 'Conference website',
                      'related_url': 'https://arxiv.org/abs/2202.00687',
                      'related_label': 'Related paper: arXiv:2202.00687'}]}
project_links = {'analytic': [{'title': 'Wikipedia primers',
               'intro': 'Accessible introductions to the mathematical and physical structures that control the edge of '
                        'hydrodynamic validity.',
               'links': [('Quasinormal mode',
                          'https://en.wikipedia.org/wiki/Quasinormal_mode',
                          'Damped normal modes with complex frequencies; in holography these organise the '
                          'non-hydrodynamic excitation spectrum.'),
                         ("Green's function",
                          'https://en.wikipedia.org/wiki/Green%27s_function',
                          'The response functions whose poles, zeros and branch cuts encode the spectrum and analytic '
                          'structure of the theory.'),
                         ('Analytic continuation',
                          'https://en.wikipedia.org/wiki/Analytic_continuation',
                          'The mathematical continuation of response functions and dispersion relations away from real '
                          'frequency and momentum.'),
                         ('Branch point',
                          'https://en.wikipedia.org/wiki/Branch_point',
                          'A basic introduction to multi-valued analytic functions and the branch points that '
                          'terminate or connect spectral sheets.'),
                         ('Sturm-Liouville theory',
                          'https://en.wikipedia.org/wiki/Sturm%E2%80%93Liouville_theory',
                          'The eigenvalue framework relevant to static screening problems and variational control of '
                          'spatial spectra.')]},
              {'title': 'Reviews and research background',
               'intro': 'Papers that motivate the study of complex momentum, convergence radii, spectral sheets and '
                        'the non-hydrodynamic sector.',
               'links': [('Short-lived modes from hydrodynamic dispersion relations',
                          'https://arxiv.org/abs/1803.08058',
                          'Shows how analytic continuation of a hydrodynamic series through complex-momentum branch '
                          'cuts reveals non-hydrodynamic modes.'),
                         ('On the convergence of the gradient expansion in hydrodynamics',
                          'https://arxiv.org/abs/1904.01018',
                          'Studies finite radii of convergence and level crossings of holographic quasinormal modes at '
                          'complex momentum.'),
                         ('Hydrodynamic Gradient Expansion in Gauge Theory Plasmas',
                          'https://arxiv.org/abs/1302.0697',
                          'A foundational study of the high-order hydrodynamic gradient expansion in holographic '
                          'plasma.'),
                         ('Minkowski-space correlators in AdS/CFT correspondence',
                          'https://arxiv.org/abs/hep-th/0205051',
                          'The standard real-time holographic prescription linking bulk boundary conditions to '
                          'retarded field-theory correlators.'),
                         ('Quasinormal modes of black holes: from astrophysics to string theory',
                          'https://arxiv.org/abs/0905.2975',
                          'A broad review of quasinormal modes, including their role in black-hole physics and '
                          'gauge-gravity duality.')]}],
 'critical': [{'title': 'Wikipedia primers',
               'intro': 'Accessible starting points for the ideas that recur throughout this programme.',
               'links': [('Critical phenomena',
                          'https://en.wikipedia.org/wiki/Critical_phenomena',
                          'Scaling, universality, critical exponents and diverging correlation lengths near continuous '
                          'phase transitions.'),
                         ('Conformal field theory',
                          'https://en.wikipedia.org/wiki/Conformal_field_theory',
                          'Quantum and statistical field theories with conformal symmetry, central to the description '
                          'of many critical points.'),
                         ('Renormalisation group',
                          'https://en.wikipedia.org/wiki/Renormalization_group',
                          'How physical descriptions change with scale, and why fixed points organise universal '
                          'critical behaviour.'),
                         ('Conformal bootstrap',
                          'https://en.wikipedia.org/wiki/Conformal_bootstrap',
                          'A non-perturbative programme that constrains conformal field theories using symmetry, '
                          'unitarity and crossing consistency.'),
                         ('Topological quantum field theory',
                          'https://en.wikipedia.org/wiki/Topological_quantum_field_theory',
                          'Field theories whose observables capture topological information and which describe many '
                          'topologically ordered phases.'),
                         ('Monte Carlo methods in statistical physics',
                          'https://en.wikipedia.org/wiki/Monte_Carlo_method_in_statistical_physics',
                          'Numerical sampling methods used to study statistical systems and compare lattice '
                          'calculations with continuum predictions.')]},
              {'title': 'Reviews and lecture notes',
               'intro': 'Longer introductions for readers who want to go beyond the overview pages.',
               'links': [('Conformal Field Theory and Statistical Mechanics - John Cardy',
                          'https://arxiv.org/abs/0807.3472',
                          'Pedagogical lectures on two-dimensional CFT and its application to critical statistical '
                          'mechanics.'),
                         ('The Conformal Bootstrap: Theory, Numerical Techniques, and Applications',
                          'https://arxiv.org/abs/1805.04405',
                          'A broad review of modern analytic and numerical conformal-bootstrap methods and their '
                          'applications to critical systems.')]}],
 'exotic': [{'title': 'Wikipedia primers',
             'intro': 'Background on mechanics, phase-space dynamics, kinetic descriptions and computational search.',
             'links': [('Hamiltonian mechanics',
                        'https://en.wikipedia.org/wiki/Hamiltonian_mechanics',
                        'The phase-space formulation of classical mechanics that the boost-agnostic construction '
                        'generalises.'),
                       ('Phase space',
                        'https://en.wikipedia.org/wiki/Phase_space',
                        'The space of positions and momenta on which Hamiltonian flows and Liouville-type statements '
                        'are formulated.'),
                       ('Kinetic theory of gases',
                        'https://en.wikipedia.org/wiki/Kinetic_theory_of_gases',
                        'The bridge from particle dynamics and collisions to statistical mechanics and hydrodynamics.'),
                       ('First-hitting-time model',
                        'https://en.wikipedia.org/wiki/First-hitting-time_model',
                        'A simple entry point to first-passage observables used when measuring search and '
                        'maze-exploration performance.'),
                       ('Particle swarm optimization',
                        'https://en.wikipedia.org/wiki/Particle_swarm_optimization',
                        'A population-based optimisation method whose position-velocity update is the target of the '
                        'dispersion-engineering programme.')]},
            {'title': 'Research background and neighbouring approaches',
             'intro': 'Foundations for mechanics without boost symmetry, together with the closest search and '
                      'optimisation ideas that the current programme must distinguish itself from.',
             'links': [('Non-Boost Invariant Fluid Dynamics',
                        'https://arxiv.org/abs/2004.10759',
                        'A systematic hydrodynamic classification when no boost symmetry is assumed.'),
                       ('Perfect Fluids',
                        'https://arxiv.org/abs/1710.04708',
                        'Develops perfect-fluid thermodynamics without assuming relativistic or Galilean boost '
                        'symmetry.'),
                       ('Lifshitz Hydrodynamics',
                        'https://arxiv.org/abs/1304.7481',
                        'An early treatment of hydrodynamics with anisotropic Lifshitz scaling.'),
                       ('Active Brownian and run-and-tumble particles separate inside a maze',
                        'https://arxiv.org/abs/1611.00191',
                        'A neighbouring first-passage result showing that particle dynamics can strongly affect maze '
                        'exploration, which narrows the novelty claim for the present work.'),
                       ('Hamiltonian Descent Methods',
                        'https://arxiv.org/abs/1809.05042',
                        'Shows that deliberately changing kinetic energy can be useful in optimisation, an important '
                        'conceptual comparator for dispersion engineering.'),
                       ('Particle swarm optimization - original conference paper',
                        'https://doi.org/10.1109/ICNN.1995.488968',
                        'The original Kennedy-Eberhart particle-swarm algorithm and the baseline from which the '
                        'optimisation branch departs.')]}],
 'multiscale': [{'title': 'Wikipedia primers',
                 'intro': 'Accessible introductions to the statistical and field-theoretic ideas behind fluctuations, '
                          'memory and rare events.',
                 'links': [('Schwinger-Keldysh formalism',
                            'https://en.wikipedia.org/wiki/Keldysh_formalism',
                            'The closed-time-path formalism used to organise real-time response, fluctuations and '
                            'non-equilibrium dynamics.'),
                           ('Fluctuation-dissipation theorem',
                            'https://en.wikipedia.org/wiki/Fluctuation%E2%80%93dissipation_theorem',
                            'The equilibrium relation tying fluctuations to response, and the starting point for many '
                            "of the programme's KMS questions."),
                           ('Large deviations theory',
                            'https://en.wikipedia.org/wiki/Large_deviations_theory',
                            'The probability theory of exponentially rare fluctuations and rate functions.'),
                           ('Brownian motion',
                            'https://en.wikipedia.org/wiki/Brownian_motion',
                            'The archetypal stochastic dynamics of a degree of freedom coupled to an environment.'),
                           ('Mori-Zwanzig formalism',
                            'https://en.wikipedia.org/wiki/Mori%E2%80%93Zwanzig_formalism',
                            'A projection-operator framework showing how eliminating unresolved degrees of freedom '
                            'generates memory and noise.'),
                           ('Renormalisation group',
                            'https://en.wikipedia.org/wiki/Renormalization_group',
                            'The language of coarse graining and scale dependence used when matching stochastic '
                            'effective theories.'),
                           ('Kinetic theory',
                            'https://en.wikipedia.org/wiki/Kinetic_theory_of_gases',
                            'The mesoscopic bridge between microscopic dynamics and hydrodynamic descriptions.')]},
                {'title': 'Reviews and lecture notes',
                 'intro': 'Technical background for Schwinger-Keldysh effective theory, stochastic hydrodynamics and '
                          'rare-event physics.',
                 'links': [('Effective field theory of dissipative fluids',
                            'https://arxiv.org/abs/1511.03646',
                            'A foundational Schwinger-Keldysh formulation of dissipative and fluctuating hydrodynamics '
                            'with local KMS symmetry.'),
                           ('Keldysh Field Theory for Driven Open Quantum Systems',
                            'https://arxiv.org/abs/1512.00637',
                            'A systematic review of the Keldysh functional-integral approach to driven and dissipative '
                            'quantum many-body systems.'),
                           ('Macroscopic fluctuation theory',
                            'https://arxiv.org/abs/1404.6466',
                            'A comprehensive review of space-time fluctuations and rare events in driven diffusive '
                            'systems.'),
                           ('A basic introduction to large deviations',
                            'https://arxiv.org/abs/1106.4146',
                            'Pedagogical notes on rare-event probabilities, rate functions and their applications in '
                            'statistical physics.'),
                           ('Lectures on hydrodynamic fluctuations in relativistic theories',
                            'https://arxiv.org/abs/1205.5040',
                            'A pedagogical bridge between hydrodynamic modes, correlation functions and fluctuating '
                            'effective descriptions.'),
                           ('An introduction to relativistic kinetic theory on curved spacetimes',
                            'https://doi.org/10.1007/s10714-022-02916-x',
                            'A modern introduction to covariant kinetic theory and its geometric formulation.')]},
                {'title': 'Other resources',
                 'intro': 'Additional material already associated with this programme.',
                 'links': [('Quantum Nonlinear Waves',
                            'https://qnlw.info/',
                            'An external resource on nonlinear and non-equilibrium wave phenomena.')]}],
 'relaxation': [{'title': 'Wikipedia primers',
                 'intro': 'Background on holography, hydrodynamics and systems maintained away from equilibrium.',
                 'links': [('AdS/CFT correspondence',
                            'https://en.wikipedia.org/wiki/AdS/CFT_correspondence',
                            'An introduction to gauge-gravity duality and the idea of describing strongly coupled '
                            'field theories through gravitational systems.'),
                           ('Non-equilibrium thermodynamics',
                            'https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics',
                            'Macroscopic descriptions of transport, fluxes and systems outside global thermodynamic '
                            'equilibrium.'),
                           ('Fluid dynamics',
                            'https://en.wikipedia.org/wiki/Fluid_dynamics',
                            'The continuum description of flowing matter that provides the long-wavelength language '
                            'used throughout the programme.'),
                           ('Fluctuation-dissipation theorem',
                            'https://en.wikipedia.org/wiki/Fluctuation%E2%80%93dissipation_theorem',
                            'The equilibrium relation between spontaneous fluctuations and linear response, and a '
                            'useful reference point for driven systems.')]},
                {'title': 'Reviews and research background',
                 'intro': 'Key papers and pedagogical material behind quasihydrodynamics, fluid-gravity duality and '
                          'long-lived modes.',
                 'links': [('Holography and hydrodynamics with weakly broken symmetries',
                            'https://arxiv.org/abs/1810.10016',
                            'A systematic introduction to quasihydrodynamics and approximately conserved quantities, '
                            'including holographic constructions.'),
                           ('Nonlinear Fluid Dynamics from Gravity',
                            'https://arxiv.org/abs/0712.2456',
                            'A foundational derivation of nonlinear boundary fluid dynamics from gravitational '
                            'dynamics in AdS.'),
                           ('Lectures on hydrodynamic fluctuations in relativistic theories',
                            'https://arxiv.org/abs/1205.5040',
                            'Pedagogical notes on hydrodynamic correlation functions, fluctuations, effective actions '
                            'and the derivative expansion.'),
                           ('Gauge/String Duality, Hot QCD and Heavy Ion Collisions',
                            'https://arxiv.org/abs/1101.0618',
                            'A broad introduction to gauge-string duality with extensive discussion of strong-coupling '
                            'transport and hydrodynamics.')]}],
 'flocks': [{'title': 'Wikipedia primers',
             'intro': 'Entry points for active matter, flocking models and the optimisation ideas connected to the '
                      'programme.',
             'links': [('Active matter',
                        'https://en.wikipedia.org/wiki/Active_matter',
                        'Systems whose constituents consume energy to move or exert forces, placing the collective '
                        'dynamics intrinsically out of equilibrium.'),
                       ('Active fluid',
                        'https://en.wikipedia.org/wiki/Active_fluid',
                        'Continuum descriptions of dense active systems such as bacterial suspensions and synthetic '
                        'self-propelled particles.'),
                       ('Vicsek model',
                        'https://en.wikipedia.org/wiki/Vicsek_model',
                        'A minimal particle model of self-propulsion, alignment, noise and the transition to '
                        'collective motion.'),
                       ('Mermin-Wagner theorem',
                        'https://en.wikipedia.org/wiki/Mermin%E2%80%93Wagner_theorem',
                        'The equilibrium theorem whose assumptions help highlight why two-dimensional active flocks '
                        'can behave very differently from equilibrium magnets.'),
                       ('Particle swarm optimisation',
                        'https://en.wikipedia.org/wiki/Particle_swarm_optimization',
                        'A population-based optimisation method inspired by collective motion, and a computational '
                        "application of the group's dispersion-engineering ideas.")]},
            {'title': 'Reviews and research background',
             'intro': 'Broader reviews connecting microscopic active-particle models to continuum hydrodynamics and '
                      'collective behaviour.',
             'links': [('Hydrodynamics of soft active matter',
                        'https://doi.org/10.1103/RevModPhys.85.1143',
                        'A classic review of active-matter hydrodynamics across biological and synthetic systems.'),
                       ('Self-aligning polar active matter',
                        'https://doi.org/10.1103/RevModPhys.97.015007',
                        'A recent review of self-alignment, collective motion and emergent organisation in polar '
                        'active systems.'),
                       ('Flocks, herds, and schools: a quantitative theory of flocking',
                        'https://doi.org/10.1103/PhysRevE.58.4828',
                        'The Toner-Tu hydrodynamic theory of flocking, a central continuum reference for the '
                        'programme.')]}],
 'superconductive': [{'title': 'Wikipedia primers',
                      'intro': 'Background on conventional superconductivity and the quantum-field-theory analogy used '
                               'in this project.',
                      'links': [('Superconductivity',
                                 'https://en.wikipedia.org/wiki/Superconductivity',
                                 'A broad introduction to zero resistance, the Meissner effect and the phenomenology '
                                 'of superconducting phases.'),
                                ('BCS theory',
                                 'https://en.wikipedia.org/wiki/BCS_theory',
                                 'The microscopic theory of conventional superconductivity based on Cooper pairing.'),
                                ('Ginzburg-Landau theory',
                                 'https://en.wikipedia.org/wiki/Ginzburg%E2%80%93Landau_theory',
                                 'The order-parameter field theory describing superconductivity near the transition '
                                 'temperature.'),
                                ('Josephson effect',
                                 'https://en.wikipedia.org/wiki/Josephson_effect',
                                 'Macroscopic phase-coherent tunnelling between superconductors and the basis of many '
                                 'superconducting devices.'),
                                ('Schwinger effect',
                                 'https://en.wikipedia.org/wiki/Schwinger_effect',
                                 'Strong-field pair production in quantum electrodynamics, which motivates one of the '
                                 'analogies explored in the project.')]},
                     {'title': 'Experiments, reviews and related laboratories',
                      'intro': 'Experimental context for electrostatic control of superconducting thin films and '
                               'Josephson structures.',
                      'links': [('Metallic supercurrent field-effect transistor',
                                 'https://doi.org/10.1038/s41565-018-0190-3',
                                 'The 2018 experiment reporting electrostatic suppression of the supercurrent in '
                                 'all-metallic superconducting field-effect devices.'),
                                ('Field-effect control of metallic superconducting systems',
                                 'https://doi.org/10.1116/1.5129364',
                                 'An open review of experiments on gate control of metallic superconductors and '
                                 'superconducting quantum devices.'),
                                ('Superconducting Quantum Electronics Lab (SQEL)',
                                 'https://web.nano.cnr.it/sqel/',
                                 'The CNR-NANO laboratory working on superconducting quantum electronics and '
                                 'field-effect devices.')]}]}

CSS = r'''
:root{
  --navy:#16243f; --navy-2:#22375f; --blue:#315d8d; --sky:#dce9f4;
  --gold:#d59b4a; --gold-soft:#f3e4cb; --ink:#19212d; --muted:#637083;
  --paper:#ffffff; --soft:#f5f7fa; --line:#dfe5ec; --max:1180px;
  --radius:18px; --shadow:0 20px 55px rgba(18,36,63,.10);
}
*{box-sizing:border-box} html{scroll-behavior:smooth} body{margin:0;background:var(--paper);color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6}
a{color:inherit} img{max-width:100%;display:block} button,input,select{font:inherit}
.skip{position:absolute;left:-9999px;top:auto}.skip:focus{left:16px;top:16px;z-index:999;background:#fff;padding:10px 14px;border-radius:8px}
.site-header{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.94);backdrop-filter:blur(14px);border-bottom:1px solid rgba(223,229,236,.95)}
.header-inner{max-width:var(--max);margin:auto;min-height:78px;padding:0 26px;display:flex;align-items:center;gap:26px}.brand{display:flex;align-items:center;gap:12px;text-decoration:none;font-weight:800;letter-spacing:.01em;color:var(--navy)}.brand img{width:48px;height:48px;object-fit:contain}.brand-copy{display:flex;flex-direction:column;line-height:1.05}.brand-copy small{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-top:5px}
.nav{margin-left:auto;display:flex;align-items:center;gap:3px}.nav a,.nav button{border:0;background:transparent;text-decoration:none;color:#39475b;padding:28px 9px 23px;border-bottom:3px solid transparent;font-size:13px;cursor:pointer;white-space:nowrap}.nav a:hover,.nav button:hover,.nav .active{color:var(--blue);border-bottom-color:var(--gold)}
.dropdown{position:relative}.dropdown-menu{display:none;position:absolute;top:67px;right:0;width:min(470px,90vw);max-height:74vh;overflow:auto;background:white;border:1px solid var(--line);border-radius:14px;box-shadow:var(--shadow);padding:8px}.dropdown.open .dropdown-menu{display:block}.dropdown-menu a{display:block;padding:10px 12px;border:0;border-radius:9px;white-space:normal}.dropdown-menu a:hover{background:var(--soft);border:0}.dropdown-menu .sub{padding-left:28px;color:var(--muted);font-size:12px}.dropdown-group-label{padding:11px 11px 5px;color:rgba(255,255,255,.62);font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;border-top:1px solid rgba(255,255,255,.14);margin-top:5px}.dropdown-group-label:first-of-type{border-top:0;margin-top:0}
.menu-toggle{display:none;margin-left:auto;border:1px solid var(--line);background:#fff;border-radius:10px;padding:8px 10px;color:var(--navy)}
.hero{position:relative;overflow:hidden;background:var(--navy);color:#fff}.hero-grid{max-width:var(--max);margin:auto;min-height:520px;padding:78px 26px;display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center}.hero h1{font-size:clamp(44px,6vw,78px);line-height:.97;margin:0 0 24px;letter-spacing:-.045em}.hero p{font-size:20px;max-width:700px;color:#e7edf5;margin:0}.hero .eyebrow{color:#f6d7a4}.hero-art{filter:drop-shadow(0 30px 60px rgba(0,0,0,.25))}.hero-logo{width:min(440px,92%);justify-self:center}.hero:after{content:"";position:absolute;width:520px;height:520px;border:1px solid rgba(255,255,255,.10);border-radius:50%;right:-260px;top:-180px}
.eyebrow{text-transform:uppercase;letter-spacing:.15em;font-size:12px;font-weight:800;color:var(--blue);margin:0 0 13px}.section{max-width:var(--max);margin:auto;padding:76px 26px}.section.narrow{max-width:940px}.section h1,.section h2,.section h3{color:var(--navy);letter-spacing:-.025em}.section h1{font-size:clamp(38px,5vw,58px);line-height:1.02;margin:0 0 24px}.section h2{font-size:clamp(28px,3.4vw,40px);line-height:1.1;margin:0 0 22px}.section h3{font-size:22px;line-height:1.2}.lead{font-size:20px;color:#425069;max-width:820px}.muted{color:var(--muted)}.band{background:var(--soft)}
.button-row{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px}.btn{display:inline-flex;align-items:center;gap:8px;text-decoration:none;border-radius:999px;padding:11px 16px;font-size:14px;font-weight:700;border:1px solid var(--line);background:white;color:var(--navy)}.btn.primary{background:var(--gold);border-color:var(--gold);color:#20180d}.btn:hover{transform:translateY(-1px);box-shadow:0 8px 20px rgba(22,36,63,.08)}
.three-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}.card{background:white;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:0 2px 4px rgba(22,36,63,.03)}.card-media{background:var(--navy);aspect-ratio:16/9;overflow:hidden}.card-media img{width:100%;height:100%;object-fit:cover}.card-body{padding:25px}.card-body p{color:#526077;margin-bottom:0}.card .kicker{font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--blue)}
.project-list{display:grid;gap:18px}.project-row{display:grid;grid-template-columns:240px 1fr;gap:26px;padding:22px;border:1px solid var(--line);border-radius:var(--radius);background:white}.project-row img{width:100%;height:100%;min-height:165px;object-fit:cover;border-radius:13px;background:var(--navy)}.project-row h3{margin:2px 0 8px}.project-row p{margin:0;color:#536178}.project-row .btn{margin-top:16px}.status-badge{display:inline-flex;align-items:center;border-radius:999px;padding:6px 10px;font-size:11px;font-weight:850;letter-spacing:.08em;text-transform:uppercase;margin:0 0 10px}.status-active{background:#eaf3ef;color:#285d49;border:1px solid #c8dfd4}.status-hiatus{background:#f8edd8;color:#79531b;border:1px solid #e6cfa9}
.page-hero{background:linear-gradient(135deg,var(--navy),var(--navy-2));color:white}.page-hero .section{padding-top:62px;padding-bottom:62px}.page-hero h1{color:#fff}.page-hero .lead{color:#e1e8f2}.breadcrumbs{font-size:13px;color:#bec9d9;margin-bottom:20px}.breadcrumbs a{color:#fff;text-decoration:none}.breadcrumbs span{opacity:.7;margin:0 7px}
.project-hero-grid{display:grid;grid-template-columns:1fr 380px;gap:50px;align-items:center}.project-hero-grid img{width:100%;border-radius:20px;box-shadow:0 24px 45px rgba(0,0,0,.22)}
.resource-nav{display:flex;flex-wrap:wrap;gap:9px;margin-top:24px}.resource-nav a{display:inline-block;text-decoration:none;border-radius:999px;border:1px solid rgba(255,255,255,.25);padding:8px 12px;font-size:13px;color:#fff}.resource-nav a:hover{background:rgba(255,255,255,.12)}
.question-list{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:25px}.question{border-top:4px solid var(--gold);background:var(--soft);padding:20px;border-radius:0 0 14px 14px;color:#43516a}.programme-strands{margin:24px 0 0;padding:0;list-style:none;border-top:1px solid var(--line)}.programme-strands li{position:relative;padding:14px 8px 14px 30px;border-bottom:1px solid var(--line);font-family:Georgia,"Times New Roman",serif;font-size:18px;color:#2f4058}.programme-strands li:before{content:"•";position:absolute;left:9px;color:var(--gold);font-size:23px;line-height:1}.content-grid{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:48px}.aside{border-left:1px solid var(--line);padding-left:24px}.aside h3{margin-top:0}.aside a{display:block;margin:9px 0;color:var(--blue)}
.team-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}.person{display:grid;grid-template-columns:96px 1fr;gap:18px;border:1px solid var(--line);border-radius:var(--radius);padding:22px;background:#fff}.avatar{width:96px;height:96px;border-radius:50%;overflow:hidden;background:var(--soft);border:3px solid #fff;box-shadow:0 0 0 1px var(--line)}.avatar img{width:100%;height:100%;object-fit:cover;display:block}.role{color:var(--blue);font-weight:700;font-size:13px}.person h3{margin:0 0 2px}.person p{font-size:14px;color:#526077;margin:10px 0}.mail{font-size:12px;color:var(--muted);word-break:break-word}
.simple-list{display:grid;gap:12px}.simple-item{padding:18px 20px;border:1px solid var(--line);border-radius:14px;background:white}.simple-item h3{margin:0 0 4px}.simple-item p{margin:0;color:#58667b}
.pub-controls{display:flex;gap:10px;flex-wrap:wrap;margin:26px 0}.pub-controls input,.pub-controls select{border:1px solid var(--line);border-radius:12px;padding:10px 12px;background:#fff;color:var(--ink)}.pub-controls input{min-width:min(430px,100%);flex:1}.pub-list{border-top:1px solid var(--line)}.pub{display:grid;grid-template-columns:72px 1fr;gap:20px;padding:18px 0;border-bottom:1px solid var(--line)}.pub-year{font-weight:800;color:var(--blue)}.pub h3{font-size:17px;margin:0 0 4px;color:var(--navy)}.pub h3 a{color:inherit;text-decoration:none}.pub h3 a:hover{text-decoration:underline}.pub-links{display:flex;gap:12px;flex-wrap:wrap;margin-top:7px}.pub-link{font-size:12px;font-weight:800;color:var(--blue);text-decoration:none}.pub-link:hover{text-decoration:underline}.pub p{margin:0;color:var(--muted);font-size:14px}.pub.hidden{display:none}.result-count{color:var(--muted);font-size:13px}
.grant{display:grid;grid-template-columns:140px 1fr 110px;gap:18px;align-items:start;padding:20px 0;border-bottom:1px solid var(--line)}.grant-year{font-weight:800;color:var(--blue)}.grant-amount{font-weight:800;color:var(--navy);text-align:right}.grant h3{margin:0 0 4px}.grant p{margin:0;color:var(--muted)}
.callout{background:linear-gradient(135deg,#fff7e7,#f8edd8);border:1px solid #ead2aa;border-left:5px solid var(--gold);padding:22px 24px;border-radius:14px}.callout strong{color:#6f4b17}.closed-callout{background:#edf1f6;border-color:#cbd4df;border-left-color:var(--navy)}.closed-callout strong{color:var(--navy)}.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:22px}.contact-card{padding:26px;border:1px solid var(--line);border-radius:var(--radius);background:white}.contact-card h3{margin-top:0}.address-art{background:var(--navy);border-radius:var(--radius);padding:34px;color:white;min-height:310px;position:relative;overflow:hidden}.address-art:after{content:"";position:absolute;width:270px;height:270px;border:1px solid rgba(255,255,255,.2);border-radius:50%;right:-90px;bottom:-110px}.address-art .pin{width:62px;height:62px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:var(--gold);display:grid;place-items:center;margin-bottom:30px}.address-art .pin:after{content:"";width:20px;height:20px;background:var(--navy);border-radius:50%}.address-art h3,.address-art p{position:relative;z-index:2;color:white}
.external-list{display:grid;gap:12px}.external-list a{display:flex;justify-content:space-between;gap:20px;padding:17px 18px;border:1px solid var(--line);border-radius:13px;text-decoration:none;background:#fff;color:var(--navy)}.external-list a:after{content:"↗";color:var(--gold);font-weight:900}.empty{padding:34px;border:1px dashed #c8d0da;border-radius:16px;color:var(--muted);text-align:center;background:var(--soft)}
.further-info-intro{font-family:Georgia,"Times New Roman",serif;font-size:19px;line-height:1.55;color:#46556b;max-width:760px;margin:0 0 36px}.resource-section{margin:0 0 46px}.resource-section:last-child{margin-bottom:0}.resource-section h2{font-size:28px;margin:0 0 7px;padding-bottom:9px;border-bottom:3px double var(--navy)}.resource-section-intro{font-family:Georgia,"Times New Roman",serif;color:#5a6678;font-size:16px;line-height:1.5;margin:0 0 15px;max-width:760px}.resource-list a{display:grid;grid-template-columns:minmax(220px,.7fr) minmax(0,1.3fr) auto;align-items:start}.resource-link-title{font-family:Georgia,"Times New Roman",serif;font-size:17px;line-height:1.3;color:var(--navy)}.resource-description{font-family:Georgia,"Times New Roman",serif;font-size:15px;line-height:1.45;color:#5c6879}.resource-list a:after{grid-column:3;grid-row:1 / span 2}
.site-footer{margin-top:58px;background:var(--navy);color:#dbe3ef}.footer-inner{max-width:var(--max);margin:auto;padding:42px 26px;display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:42px}.site-footer a{color:#fff;text-decoration:none}.site-footer h3{color:#fff;margin:0 0 13px;font-size:14px}.site-footer p,.site-footer li{font-size:13px;color:#bdc8d9}.site-footer ul{list-style:none;padding:0;margin:0}.site-footer li{margin:6px 0}.footer-brand{display:flex;align-items:center;gap:13px}.footer-brand img{width:54px;height:54px}.footer-bottom{border-top:1px solid rgba(255,255,255,.11);padding:16px 26px;color:#9eacc0;font-size:11px}.footer-bottom>div{max-width:var(--max);margin:auto;display:flex;justify-content:space-between;gap:15px;flex-wrap:wrap}
@media(max-width:1050px){.nav a,.nav button{font-size:12px;padding-left:6px;padding-right:6px}.brand-copy small{display:none}}
@media(max-width:900px){.menu-toggle{display:block}.nav{display:none;position:absolute;left:0;right:0;top:78px;background:white;border-bottom:1px solid var(--line);padding:12px 20px 22px;flex-direction:column;align-items:stretch;max-height:calc(100vh - 78px);overflow:auto}.nav.open{display:flex}.nav a,.nav button{padding:12px 7px;border-bottom:1px solid var(--line);text-align:left}.dropdown-menu{position:static;width:auto;max-height:none;box-shadow:none;border:0;padding:6px 0}.hero-grid,.project-hero-grid,.content-grid{grid-template-columns:1fr}.hero-grid{min-height:auto}.hero-art{max-width:560px}.project-hero-grid img{max-width:520px}.aside{border-left:0;border-top:1px solid var(--line);padding:22px 0 0}.three-grid,.question-list{grid-template-columns:1fr}.team-grid{grid-template-columns:1fr}.grant{grid-template-columns:100px 1fr}.grant-amount{grid-column:2;text-align:left}.footer-inner{grid-template-columns:1fr 1fr}.footer-inner>div:first-child{grid-column:1/-1}}
@media(max-width:650px){.header-inner,.section,.footer-inner{padding-left:18px;padding-right:18px}.brand-copy{font-size:14px}.brand img{width:42px;height:42px}.hero-grid{padding:58px 18px}.cards,.contact-grid{grid-template-columns:1fr}.project-row{grid-template-columns:1fr}.project-row img{height:auto}.pub{grid-template-columns:54px 1fr}.person{grid-template-columns:72px 1fr}.avatar{width:72px;height:72px}.footer-inner{grid-template-columns:1fr}.footer-inner>div:first-child{grid-column:auto}.grant{grid-template-columns:1fr}.grant-amount{grid-column:1}.question-list{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
'''

CSS += r'''
/* v4 - visual treatment aligned with the approved homepage concept */
body{font-family:Georgia,"Times New Roman",serif;background:#fbfaf7;color:#17233a}
body p,body li,body input,body select,body button,.role,.mail,.identity-links,.person-links,.kicker,.eyebrow,.status-badge{font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.site-header{background:#122b49;border-bottom:1px solid rgba(255,255,255,.10);backdrop-filter:none}
.header-inner{min-height:98px;max-width:1536px;padding:0 36px;gap:26px}
.brand{color:#fff;font-family:Georgia,"Times New Roman",serif;font-size:29px;font-weight:500;gap:16px}
.brand img{width:70px;height:70px}
.brand-copy{display:block}.brand-copy small{display:none}
.nav a,.nav button{color:#fff;font-family:Georgia,"Times New Roman",serif;font-size:17px;padding:35px 14px 26px;border-bottom:3px solid transparent}
.nav a:hover,.nav button:hover,.nav .active{color:#fff;border-bottom-color:#e6bd6d}
.dropdown-menu{top:78px;background:#122b49;border-color:rgba(255,255,255,.16);box-shadow:0 18px 45px rgba(0,0,0,.24)}
.dropdown-menu a,.dropdown-menu .sub{color:#fff}.dropdown-menu a:hover{background:rgba(255,255,255,.08)}
.menu-toggle{border-color:rgba(255,255,255,.32);background:transparent;color:#fff}
.hero{background:#fbfaf7;color:var(--navy);border-bottom:1px solid #ece9e2}
.hero:after{display:none}
.hero-grid{max-width:1536px;min-height:365px;padding:42px 38px 34px;display:grid;grid-template-columns:360px minmax(0,1fr);gap:48px;align-items:center;position:relative}
.hero-logo{width:320px;max-height:320px;object-fit:contain;justify-self:start;filter:none;z-index:2}
.hero-copy{position:relative;z-index:2;max-width:860px}
.hero h1{font-family:Georgia,"Times New Roman",serif;font-size:clamp(44px,4.4vw,68px);line-height:.98;margin:0 0 24px;letter-spacing:-.035em;color:#132d51}
.hero p{font-family:Georgia,"Times New Roman",serif;font-size:21px;line-height:1.52;color:#183153;max-width:810px}
.hero .eyebrow{color:#315d8d}
.hero-mesh{position:absolute;right:-58px;top:0;width:510px;height:100%;object-fit:cover;object-position:left center;opacity:.34;mix-blend-mode:multiply;z-index:1;pointer-events:none}
.hero-copy>*{position:relative;z-index:2}
.section{max-width:1460px}.section h1,.section h2,.section h3{font-family:Georgia,"Times New Roman",serif}
.band{background:#f2f0ec}
.research-programme-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.programme-card{border:1px solid #e2e0db;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 6px 18px rgba(18,43,73,.045)}
.programme-card .card-media{aspect-ratio:1.38/1;background:#102c4b}
.programme-card .card-media img{width:100%;height:100%;object-fit:cover}
.programme-card .card-body{padding:19px 20px 22px}
.programme-card h3{font-size:25px;margin:5px 0 8px;line-height:1.08}
.programme-card p{font-family:Georgia,"Times New Roman",serif;font-size:17px;line-height:1.35;color:#2b405f;margin:0 0 18px}
.programme-card .btn{font-family:Georgia,"Times New Roman",serif;border:0;padding:0;background:transparent;color:#1d4f94;font-weight:400;border-radius:0;box-shadow:none}
.programme-card .btn:hover{box-shadow:none;text-decoration:underline;transform:none}
.toolkit-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.toolkit-grid .card{border-radius:8px}.toolkit-grid .card-media{aspect-ratio:1.55/1}
.project-row img,.project-hero-grid img{background:#102c4b}
.person{grid-template-columns:118px 1fr;align-items:start}
.avatar{width:118px;height:118px}
.person-heading{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}.person-heading h3{margin:0}
.identity-links{display:flex;flex-wrap:wrap;gap:7px;margin:4px 0 0}
.identity-link,.person-link{display:inline-flex;align-items:center;gap:4px;border:1px solid #cbd6e2;border-radius:999px;padding:3px 8px;text-decoration:none;color:#285486;font-size:11px;font-weight:700;background:#f8fafc}
.identity-link:hover,.person-link:hover{background:#edf3f9}
.person-links{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.mail{display:block;margin-top:8px;color:#657286}
.talk-list{display:grid;gap:18px}.talk-card{border:1px solid var(--line);border-radius:16px;background:#fff;padding:24px}.talk-card h3{margin:2px 0 14px;font-size:23px}.talk-type{font-family:Inter,ui-sans-serif,sans-serif!important;font-size:11px!important;font-weight:800!important;letter-spacing:.12em;text-transform:uppercase;color:var(--blue)!important;margin:0 0 5px!important}.talk-meta{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 26px;margin:16px 0 19px;padding:14px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.talk-meta div{min-width:0}.talk-meta dt{font-family:Inter,ui-sans-serif,sans-serif;font-size:10px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:2px}.talk-meta dd{margin:0;font-family:Georgia,"Times New Roman",serif;color:var(--navy);line-height:1.35}.talk-abstract h4{font-family:Inter,ui-sans-serif,sans-serif;font-size:11px;letter-spacing:.11em;text-transform:uppercase;color:var(--navy);margin:0 0 7px}.talk-card p{margin:5px 0;color:#56657a}.talk-abstract>p{font-size:16px;line-height:1.58;color:#34445b}.talk-source-note{font-family:Inter,ui-sans-serif,sans-serif!important;font-size:11px!important;line-height:1.45!important;color:var(--muted)!important;margin-top:9px!important}.talk-links{display:flex;flex-wrap:wrap;gap:10px 16px;margin-top:16px}.talk-links a{font-family:Inter,ui-sans-serif,sans-serif;font-size:12px;font-weight:750;color:#315d8d;text-decoration:none}.talk-links a:hover{text-decoration:underline}
@media(max-width:1120px){.nav a,.nav button{font-size:14px;padding-left:7px;padding-right:7px}.brand{font-size:23px}.brand img{width:56px;height:56px}.hero-mesh{opacity:.22}}
@media(max-width:900px){.nav{top:98px;background:#122b49;border-color:rgba(255,255,255,.12)}.nav a,.nav button{color:#fff;border-bottom-color:rgba(255,255,255,.13)}.dropdown-menu{background:transparent}.hero-grid{grid-template-columns:240px 1fr;gap:24px;padding:36px 24px}.hero-logo{width:230px}.hero-mesh{display:none}.research-programme-grid,.toolkit-grid{grid-template-columns:1fr}.person{grid-template-columns:96px 1fr}.avatar{width:96px;height:96px}}
@media(max-width:650px){.header-inner{min-height:76px;padding:0 18px}.brand{font-size:19px}.brand img{width:46px;height:46px}.nav{top:76px}.hero-grid{grid-template-columns:1fr;padding:32px 20px}.hero-logo{width:220px;justify-self:center}.hero-copy{text-align:left}.person{grid-template-columns:76px 1fr}.avatar{width:76px;height:76px}}
'''

CSS += r"""
/* v5 - editorial typesetting pass: restrained, newspaper-like hierarchy */
:root{
  --paper:#fbfaf6; --soft:#f3f0e8; --ink:#182033; --muted:#687184;
  --navy:#122b49; --navy-2:#1c3a60; --blue:#275889; --gold:#c99745;
  --line:#d8d4cb; --line-dark:#a9a59c; --max:1260px; --radius:2px;
  --shadow:none;
}
html{font-size:16px}
body{background:var(--paper);color:var(--ink);font-family:Georgia,"Times New Roman",serif;line-height:1.55;text-rendering:optimizeLegibility}
p{max-width:72ch} a{text-underline-offset:2px}
body p,body li{font-family:Georgia,"Times New Roman",serif}
body input,body select,body button,.eyebrow,.status-badge,.role,.mail,.identity-links,.person-links,.pub-year,.pub-link,.result-count,.grant-year,.grant-amount,.talk-event,.talk-links,.kicker{font-family:Arial,Helvetica,sans-serif}
.site-header{background:var(--navy);border-bottom:3px double rgba(232,217,183,.58);position:sticky;top:0}
.header-inner{max-width:1320px;min-height:82px;padding:0 30px;gap:22px}
.brand{font-size:26px;font-weight:500;letter-spacing:-.015em;gap:13px}.brand img{width:58px;height:58px}
.nav{gap:0}.nav a,.nav button{font-family:Georgia,"Times New Roman",serif;font-size:15px;padding:29px 10px 24px;border-bottom-width:2px}
.nav a:hover,.nav button:hover,.nav .active{border-bottom-color:#e7c77f}
.dropdown-menu{top:68px;border-radius:0;border:1px solid rgba(255,255,255,.20);padding:5px;background:var(--navy)}.dropdown-menu a{border-radius:0;padding:9px 11px}
.hero{background:var(--paper);color:var(--ink);border-bottom:4px double var(--line-dark)}
.hero-grid{max-width:1260px;min-height:0;padding:44px 30px 40px;grid-template-columns:285px minmax(0,1fr);gap:50px;align-items:center}
.hero-logo{width:268px;max-height:268px;justify-self:start}.hero-copy{max-width:810px}
.hero h1{font-size:clamp(46px,5vw,70px);line-height:.96;letter-spacing:-.045em;color:var(--navy);margin:0 0 20px;text-wrap:balance}
.hero p{font-size:20px;line-height:1.5;color:#263b58;max-width:70ch;margin:0}.hero .eyebrow{font-size:11px;letter-spacing:.19em;color:var(--blue);margin-bottom:12px}.hero-mesh{display:none!important}
.section{max-width:var(--max);padding:58px 30px}.section.narrow{max-width:1040px}
.section h1,.section h2,.section h3{letter-spacing:-.025em;color:var(--navy)}.section h1{font-size:clamp(42px,4.8vw,62px);line-height:.98}.section h2{font-size:clamp(30px,3.1vw,42px);line-height:1.04;margin:0 0 18px}.section h3{font-size:22px;line-height:1.14}
.eyebrow{font-size:10px;letter-spacing:.18em;margin-bottom:9px;color:var(--blue)}.lead{font-family:Georgia,"Times New Roman",serif;font-size:19px;line-height:1.52;color:#35465e;max-width:72ch}.band{background:#f4f1ea;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.section-heading{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:28px;align-items:end;border-top:4px double var(--navy);padding-top:12px;margin-bottom:24px}.section-heading .eyebrow{margin-bottom:5px}.section-heading h2{margin:0}.section-heading .section-deck{max-width:46ch;margin:0 0 4px;color:#536075;font-size:16px;line-height:1.4}.section-heading .text-link{align-self:end;margin-bottom:4px;text-decoration:none;color:var(--blue);font-size:16px;white-space:nowrap}.section-heading .text-link:hover{text-decoration:underline}
.toolkit-section{background:#f4f1ea;border-bottom:4px double var(--line-dark)}
.toolkit-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.toolkit-grid .card{border:0;border-radius:0;box-shadow:none;background:transparent;overflow:visible;padding:0 22px 24px}.toolkit-grid .card:first-child{padding-left:0}.toolkit-grid .card:last-child{padding-right:0}.toolkit-grid .card+.card{border-left:1px solid var(--line)}
.toolkit-grid .card-media{aspect-ratio:1.62/1;margin:0 -1px 18px;background:var(--navy);border-bottom:1px solid var(--line)}.toolkit-grid .card-body{padding:0 4px}.toolkit-grid .card h3{font-size:25px;margin:0 0 8px}.toolkit-grid .card p{font-size:16.5px;line-height:1.48;color:#42516a;margin:0}
.active-projects{padding-top:54px;padding-bottom:66px}.research-programme-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.programme-card{border:0;border-radius:0;box-shadow:none;background:transparent;overflow:visible;padding:0 22px 28px}.programme-card:first-child{padding-left:0}.programme-card:last-child{padding-right:0}.programme-card+.programme-card{border-left:1px solid var(--line)}
.programme-card .card-media{aspect-ratio:1.5/1;margin:0 -1px 18px;background:var(--navy);border-bottom:1px solid var(--line)}.programme-card .card-body{padding:0 4px}.programme-card h3{font-size:26px;line-height:1.08;margin:6px 0 10px}.programme-card p{font-family:Georgia,"Times New Roman",serif;font-size:16.5px;line-height:1.48;color:#41506a;margin:0 0 18px}
.status-badge{border-radius:0;padding:3px 6px;margin:0 0 4px;font-size:9px;letter-spacing:.11em;background:transparent}.status-active{border-color:#8db5a2;color:#2d624c}.status-hiatus{border-color:#caa86e;color:#76531d}
.programme-card .btn,.card .btn{border:0;border-radius:0;padding:0;background:transparent;box-shadow:none;font-family:Georgia,"Times New Roman",serif;font-size:16px;font-weight:400;color:var(--blue)}.programme-card .btn:hover,.card .btn:hover{transform:none;box-shadow:none;text-decoration:underline}
.page-hero{background:var(--paper);color:var(--ink);border-bottom:4px double var(--line-dark)}.page-hero .section{padding-top:38px;padding-bottom:34px}.page-hero h1{color:var(--navy);margin:0 0 14px;max-width:18ch}.page-hero .lead{color:#40506a;margin:0}.page-hero .eyebrow{color:var(--blue)}
.breadcrumbs{font-family:Arial,Helvetica,sans-serif;font-size:11px;color:#6b7485;margin-bottom:14px;text-transform:uppercase;letter-spacing:.06em}.breadcrumbs a{color:var(--blue)}
.project-hero-grid{grid-template-columns:minmax(0,1fr) 390px;gap:44px;align-items:start}.project-hero-grid img{border-radius:0;box-shadow:none;border:1px solid var(--line);margin-top:6px}
.resource-nav{gap:0;margin-top:22px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);width:max-content;max-width:100%}.resource-nav a{font-family:Arial,Helvetica,sans-serif;border:0;border-right:1px solid var(--line);border-radius:0;padding:8px 12px;color:var(--blue);font-size:11px;text-transform:uppercase;letter-spacing:.04em}.resource-nav a:first-child{padding-left:0}.resource-nav a:last-child{border-right:0}.resource-nav a:hover{background:transparent;text-decoration:underline}
.question-list{gap:0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.question{border:0;border-top:3px solid var(--gold);border-radius:0;background:transparent;padding:18px 20px 20px;font-size:17px;line-height:1.48;color:#364761}.question+.question{border-left:1px solid var(--line)}
.cards{gap:30px 34px}.cards .card{border:0;border-top:3px solid var(--navy);border-bottom:1px solid var(--line);border-radius:0;box-shadow:none;background:transparent}.cards .card-media{aspect-ratio:1.55/1;border-bottom:1px solid var(--line)}.cards .card-body{padding:18px 0 24px}.cards .card-body p{font-family:Georgia,"Times New Roman",serif;font-size:16.5px;line-height:1.48;color:#45546b}.cards .card h3{font-size:25px;margin:4px 0 10px}
.project-row{border:0;border-top:3px solid var(--navy);border-bottom:1px solid var(--line);border-radius:0;background:transparent;padding:18px 0}.project-row img{border-radius:0}
.simple-list{gap:0;border-top:1px solid var(--line)}.simple-item{border:0;border-bottom:1px solid var(--line);border-radius:0;background:transparent;padding:16px 0}.simple-item h3{font-size:20px}
.team-grid{gap:0;grid-template-columns:repeat(2,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.person{grid-template-columns:108px 1fr;gap:19px;border:0;border-radius:0;border-bottom:1px solid var(--line);background:transparent;padding:22px 24px 24px 0}.person:nth-child(even){border-left:1px solid var(--line);padding-left:24px;padding-right:0}.person:nth-last-child(-n+2){border-bottom:0}
.avatar{width:108px;height:108px;border-radius:0;border:1px solid var(--line);box-shadow:none;background:#eee}.person-heading{display:block}.person-heading h3{font-size:22px;margin:0 0 2px}.identity-links{margin:5px 0 0;gap:6px}.identity-link,.person-link{border:0;border-bottom:1px solid #9fb2c7;border-radius:0;background:transparent;padding:1px 0;font-size:10px;color:var(--blue)}.identity-link:hover,.person-link:hover{background:transparent;border-bottom-color:var(--blue)}.role{font-size:11px;letter-spacing:.03em;text-transform:uppercase;color:var(--blue)}.person p{font-family:Georgia,"Times New Roman",serif;font-size:15px;line-height:1.45;color:#45546b;margin:10px 0}.mail{font-size:11px;color:#6e7786}
.pub-controls{margin:8px 0 20px;padding:14px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.pub-controls input,.pub-controls select{border:1px solid var(--line-dark);border-radius:0;background:#fff;padding:9px 10px;font-family:Arial,Helvetica,sans-serif}.pub-list{border-top:3px solid var(--navy)}
.pub{grid-template-columns:78px 1fr;gap:22px;padding:17px 0;border-bottom:1px solid var(--line)}.pub-year{font-size:12px;letter-spacing:.06em;color:var(--blue);padding-top:3px}.pub h3{font-family:Georgia,"Times New Roman",serif;font-size:19px;line-height:1.23;margin:0 0 4px;color:var(--navy)}.pub p{font-family:Georgia,"Times New Roman",serif;font-size:14.5px;line-height:1.4;color:#687184}.pub-link{font-size:10px;letter-spacing:.04em}
.talk-list{gap:0;border-top:3px solid var(--navy)}.talk-card{border:0;border-bottom:1px solid var(--line);border-radius:0;background:transparent;padding:21px 0}.talk-card h3{font-size:25px;line-height:1.15}.talk-card p{font-family:Georgia,"Times New Roman",serif;color:#526077}.grant{border-bottom:1px solid var(--line);padding:18px 0}
.callout,.contact-card,.address-art{border-radius:0;box-shadow:none}.contact-card{background:transparent;border:1px solid var(--line-dark)}.external-list{gap:0;border-top:1px solid var(--line)}.external-list a{border:0;border-bottom:1px solid var(--line);border-radius:0;background:transparent;padding:13px 0}.empty{border-radius:0;background:transparent}
.btn{border-radius:0;border:1px solid var(--line-dark);font-family:Arial,Helvetica,sans-serif;font-size:12px;letter-spacing:.02em;padding:9px 12px;background:transparent}.btn.primary{background:var(--navy);border-color:var(--navy);color:white}.btn:hover{transform:none;box-shadow:none;background:#f0ede6}.btn.primary:hover{background:#1c3a60}
.site-footer{margin-top:44px;background:var(--navy);border-top:4px double #e0c589}.footer-inner{max-width:1260px;padding:34px 30px;gap:50px}.footer-brand img{filter:brightness(0) invert(1);opacity:.9}.site-footer h3{font-family:Georgia,"Times New Roman",serif;font-size:15px}.site-footer p,.site-footer li{font-family:Georgia,"Times New Roman",serif;font-size:13px;line-height:1.45}.footer-bottom{font-family:Arial,Helvetica,sans-serif}
@media(max-width:1050px){.header-inner{padding:0 22px}.nav a,.nav button{font-size:13px;padding-left:7px;padding-right:7px}.brand{font-size:22px}.brand img{width:52px;height:52px}.hero-grid{grid-template-columns:235px minmax(0,1fr);gap:34px}.hero-logo{width:220px}.hero h1{font-size:clamp(42px,5.2vw,58px)}.project-hero-grid{grid-template-columns:minmax(0,1fr) 330px}}
@media(max-width:900px){.nav{top:82px}.hero-grid,.project-hero-grid{grid-template-columns:1fr}.hero-grid{padding:34px 24px}.hero-logo{width:205px;justify-self:center}.hero h1{font-size:48px}.toolkit-grid,.research-programme-grid{grid-template-columns:1fr;border-bottom:0}.toolkit-grid .card,.programme-card{padding:0 0 26px;border-bottom:1px solid var(--line)}.toolkit-grid .card+.card,.programme-card+.programme-card{border-left:0;padding-top:24px}.toolkit-grid .card-media,.programme-card .card-media{max-width:640px}.team-grid{grid-template-columns:1fr}.person,.person:nth-child(even){border-left:0;padding-left:0;padding-right:0}.person:nth-last-child(-n+2){border-bottom:1px solid var(--line)}.person:last-child{border-bottom:0}.question-list{grid-template-columns:1fr}.question+.question{border-left:0;border-top:1px solid var(--line);box-shadow:inset 0 3px 0 var(--gold)}}
@media(max-width:650px){.header-inner{min-height:72px;padding:0 16px}.nav{top:72px}.brand{font-size:18px}.brand img{width:44px;height:44px}.section{padding:44px 18px}.hero-grid{padding:28px 18px 32px}.hero-logo{width:180px}.hero h1{font-size:39px;line-height:.99}.hero p{font-size:18px}.section-heading{grid-template-columns:1fr;gap:8px}.section-heading .text-link{justify-self:start}.section-heading .section-deck{margin-top:0}.person{grid-template-columns:82px 1fr;gap:15px}.avatar{width:82px;height:82px}.person-heading h3{font-size:20px}.pub{grid-template-columns:50px 1fr;gap:13px}.pub h3{font-size:17px}.resource-nav{width:100%;display:grid}.resource-nav a{border-right:0;border-bottom:1px solid var(--line);padding:8px 0}.resource-nav a:last-child{border-bottom:0}.resource-list a{grid-template-columns:1fr auto;gap:5px 14px}.resource-description{grid-column:1}.resource-list a:after{grid-column:2;grid-row:1 / span 2}.resource-section h2{font-size:24px}}

"""

CSS += r'''
/* v6 - simplified landing masthead and publication abstracts */
.hero-grid{display:block;max-width:1260px;min-height:0;padding:52px 30px 46px}
.hero-copy{max-width:990px}
.hero h1{max-width:15ch}
.toolkit-section .section-heading{grid-template-columns:1fr}
.pub-venue{margin-bottom:0}
.pub-abstract{max-width:78ch;margin-top:12px;padding-top:10px;border-top:1px dotted var(--line-dark)}
.pub-abstract>span{display:block;margin-bottom:5px;font-family:Arial,Helvetica,sans-serif;font-size:10px;font-weight:700;line-height:1.2;letter-spacing:.11em;text-transform:uppercase;color:var(--blue)}
.pub-abstract p{margin:0!important;max-width:76ch;color:#405064!important;font-size:14px!important;line-height:1.54!important}
@media(max-width:1050px){.hero-grid{display:block;padding:42px 22px}.hero h1{font-size:clamp(42px,5.2vw,58px)}}
@media(max-width:900px){.hero-grid{display:block;padding:34px 24px}.hero h1{font-size:48px}}
@media(max-width:650px){.hero-grid{display:block;padding:28px 18px 32px}.hero h1{font-size:39px;max-width:none}.pub-abstract p{font-size:13.5px!important;line-height:1.5!important}}
@media(max-width:600px){.talk-meta{grid-template-columns:1fr}}
'''

JS = r'''
(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  const drop = document.querySelector('.dropdown');
  const dropButton = document.querySelector('.dropdown-toggle');
  if (toggle && nav) toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  if (dropButton && drop) dropButton.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = drop.classList.toggle('open');
    dropButton.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('click', (e) => {
    if (drop && !drop.contains(e.target)) {
      drop.classList.remove('open');
      if (dropButton) dropButton.setAttribute('aria-expanded','false');
    }
  });

  const q = document.querySelector('#pub-search');
  const y = document.querySelector('#pub-year');
  const pubs = [...document.querySelectorAll('.pub[data-year]')];
  const count = document.querySelector('#pub-count');
  function filterPubs(){
    if (!pubs.length) return;
    const needle = (q?.value || '').toLowerCase().trim();
    const year = y?.value || 'all';
    let shown = 0;
    pubs.forEach(p => {
      const okText = !needle || p.textContent.toLowerCase().includes(needle);
      const okYear = year === 'all' || p.dataset.year === year;
      p.classList.toggle('hidden', !(okText && okYear));
      if(okText && okYear) shown++;
    });
    if(count) count.textContent = `${shown} publication${shown===1?'':'s'}`;
  }
  q?.addEventListener('input', filterPubs);
  y?.addEventListener('change', filterPubs);
  filterPubs();
})();
'''

# Simple, fully local vector branding.
LOGO = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" role="img" aria-labelledby="t"><title id="t">STELLAR Lab mark</title><rect width="120" height="120" rx="24" fill="#16243f"/><circle cx="60" cy="60" r="31" fill="none" stroke="#d59b4a" stroke-width="4"/><path d="M60 17v86M17 60h86M30 30l60 60M90 30L30 90" stroke="#dce9f4" stroke-width="2" opacity=".8"/><circle cx="60" cy="60" r="10" fill="#d59b4a"/><circle cx="60" cy="17" r="4" fill="#fff"/><circle cx="103" cy="60" r="4" fill="#fff"/><circle cx="30" cy="90" r="4" fill="#fff"/></svg>'''
HERO = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 620"><defs><linearGradient id="g" x1="0" x2="1"><stop stop-color="#315d8d"/><stop offset="1" stop-color="#d59b4a"/></linearGradient></defs><rect width="800" height="620" rx="40" fill="#1f3458"/><g fill="none" stroke="#dce9f4" opacity=".38"><path d="M65 420c140-180 230-250 352-190s126 254 310 166" stroke-width="7"/><path d="M82 160c144 75 206 15 329 83s160 185 300 135" stroke-width="2"/><circle cx="395" cy="312" r="185"/><circle cx="395" cy="312" r="112"/><circle cx="395" cy="312" r="45"/></g><g fill="url(#g)"><circle cx="132" cy="420" r="17"/><circle cx="272" cy="296" r="12"/><circle cx="397" cy="312" r="28"/><circle cx="536" cy="402" r="15"/><circle cx="680" cy="356" r="20"/></g><g fill="#fff"><circle cx="174" cy="153" r="6"/><circle cx="640" cy="148" r="7"/><circle cx="585" cy="245" r="5"/><circle cx="250" cy="488" r="5"/></g><path d="M110 535h580" stroke="#d59b4a" stroke-width="4"/><text x="112" y="574" fill="#fff" font-family="Arial,sans-serif" font-size="30" font-weight="700" letter-spacing="6">STELLAR</text></svg>'''

SVGS = {
'flocks.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450"><rect width="800" height="450" fill="#16243f"/><g fill="#dce9f4" opacity=".9"><path d="M80 190l20 -10 -8 15 15 7 -20 3z"/><path d="M150 140l20 -10 -8 15 15 7 -20 3z"/><path d="M220 235l20 -10 -8 15 15 7 -20 3z"/><path d="M290 175l20 -10 -8 15 15 7 -20 3z"/><path d="M360 120l20 -10 -8 15 15 7 -20 3z"/><path d="M420 250l20 -10 -8 15 15 7 -20 3z"/><path d="M500 180l20 -10 -8 15 15 7 -20 3z"/><path d="M565 120l20 -10 -8 15 15 7 -20 3z"/><path d="M640 220l20 -10 -8 15 15 7 -20 3z"/><path d="M705 155l20 -10 -8 15 15 7 -20 3z"/><path d="M170 300l20 -10 -8 15 15 7 -20 3z"/><path d="M325 325l20 -10 -8 15 15 7 -20 3z"/><path d="M520 320l20 -10 -8 15 15 7 -20 3z"/><path d="M665 305l20 -10 -8 15 15 7 -20 3z"/></g><path d="M45 365c190-140 330-140 710-30" fill="none" stroke="#d59b4a" stroke-width="5"/></svg>',
'relaxation.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450"><defs><marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#d59b4a"/></marker></defs><rect width="800" height="450" fill="#16243f"/><g stroke="#d59b4a" stroke-width="4" marker-end="url(#arr)" opacity=".96"><path d="M134 110 H186"/><path d="M279 92 H315"/><path d="M413 128 H479"/><path d="M595 98 H635"/><path d="M712 142 H746"/><path d="M190 232 H230"/><path d="M344 215 H404"/><path d="M502 245 H545"/><path d="M676 235 H734"/><path d="M127 342 H175"/><path d="M301 330 H337"/><path d="M455 350 H517"/><path d="M620 332 H662"/><path d="M733 345 H764"/></g><g><circle cx="110" cy="110" r="12" fill="#6fa3d2"/><circle cx="106" cy="106" r="3" fill="white" opacity=".35"/><circle cx="250" cy="92" r="17" fill="#dce9f4"/><circle cx="246" cy="88" r="4" fill="white" opacity=".35"/><circle cx="390" cy="128" r="11" fill="#dce9f4"/><circle cx="386" cy="124" r="2" fill="white" opacity=".35"/><circle cx="565" cy="98" r="18" fill="#6fa3d2"/><circle cx="561" cy="94" r="4" fill="white" opacity=".35"/><circle cx="690" cy="142" r="10" fill="#dce9f4"/><circle cx="686" cy="138" r="2" fill="white" opacity=".35"/><circle cx="160" cy="232" r="18" fill="#dce9f4"/><circle cx="156" cy="228" r="4" fill="white" opacity=".35"/><circle cx="320" cy="215" r="12" fill="#6fa3d2"/><circle cx="316" cy="211" r="3" fill="white" opacity=".35"/><circle cx="470" cy="245" r="20" fill="#dce9f4"/><circle cx="466" cy="241" r="5" fill="white" opacity=".35"/><circle cx="650" cy="235" r="14" fill="#dce9f4"/><circle cx="646" cy="231" r="3" fill="white" opacity=".35"/><circle cx="105" cy="342" r="10" fill="#6fa3d2"/><circle cx="101" cy="338" r="2" fill="white" opacity=".35"/><circle cx="270" cy="330" r="19" fill="#dce9f4"/><circle cx="266" cy="326" r="4" fill="white" opacity=".35"/><circle cx="430" cy="350" r="13" fill="#dce9f4"/><circle cx="426" cy="346" r="3" fill="white" opacity=".35"/><circle cx="590" cy="332" r="18" fill="#6fa3d2"/><circle cx="586" cy="328" r="4" fill="white" opacity=".35"/><circle cx="710" cy="345" r="11" fill="#dce9f4"/><circle cx="706" cy="341" r="2" fill="white" opacity=".35"/></g><path d="M55 401 H745" stroke="#dce9f4" opacity=".18"/><text x="58" y="426" fill="#dce9f4" opacity=".78" font-family="Arial,sans-serif" font-size="19" letter-spacing="2">DRIVE →     RELAXATION →     STEADY STATE</text></svg>',
'superconductive.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450">\n<defs><marker id="ea" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#d59b4a"/></marker><linearGradient id="film" x1="0" x2="1"><stop stop-color="#6fa3d2"/><stop offset=".5" stop-color="#dce9f4"/><stop offset="1" stop-color="#6fa3d2"/></linearGradient></defs>\n<rect width="800" height="450" fill="#16243f"/>\n<rect x="210" y="235" width="380" height="70" rx="14" fill="url(#film)" stroke="#dce9f4" stroke-width="3"/><rect x="72" y="248" width="138" height="44" rx="8" fill="none" stroke="#d59b4a" stroke-width="4"/><rect x="590" y="248" width="138" height="44" rx="8" fill="none" stroke="#d59b4a" stroke-width="4"/>\n<rect x="250" y="72" width="300" height="34" rx="8" fill="none" stroke="#d59b4a" stroke-width="4"/><text x="557" y="99" fill="#f3e4cb" font-family="Arial,sans-serif" font-size="22">V<tspan baseline-shift="sub" font-size="14">g</tspan></text>\n<g stroke="#d59b4a" stroke-width="4" marker-end="url(#ea)"><path d="M300 125 V210"/><path d="M400 125 V210"/><path d="M500 125 V210"/></g><text x="520" y="178" fill="#f3e4cb" font-family="Arial,sans-serif" font-size="24">E</text>\n<path d="M96 270 H185" stroke="#dce9f4" stroke-width="3"/><path d="M615 270 H704" stroke="#dce9f4" stroke-width="3"/><text x="315" y="278" fill="#16243f" font-family="Arial,sans-serif" font-size="21" font-weight="700">SUPERCONDUCTING FILM</text>\n<g fill="none" stroke="#ffffff" opacity=".34"><path d="M255 330 C315 380 485 380 545 330"/><path d="M278 335 C330 365 470 365 522 335"/></g>\n</svg>',
'critical.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450"><defs><marker id="rg" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#dce9f4"/></marker></defs><rect width="800" height="450" fill="#16243f"/>\n<g stroke="#dce9f4" opacity=".24"><path d="M90 360 H730"/><path d="M130 405 V55"/></g><g fill="#dce9f4" opacity=".75" font-family="Arial,sans-serif" font-size="20"><text x="705" y="390">g₁</text><text x="98" y="75">g₂</text></g>\n<g fill="none" stroke="#dce9f4" stroke-width="4" marker-end="url(#rg)" opacity=".9"><path d="M190 95 C270 95 350 125 438 205"/><path d="M220 350 C300 322 362 275 438 215"/><path d="M670 88 C595 125 520 162 455 207"/><path d="M670 340 C595 320 515 275 455 222"/><path d="M350 60 C390 105 420 145 445 202"/></g><circle cx="447" cy="214" r="17" fill="#d59b4a"/><circle cx="447" cy="214" r="34" fill="none" stroke="#d59b4a" opacity=".45"/><text x="474" y="207" fill="#f3e4cb" font-family="Arial,sans-serif" font-size="22">fixed point</text><text x="494" y="237" fill="#dce9f4" opacity=".72" font-family="Arial,sans-serif" font-size="18">scale invariance</text></svg>',
'multiscale.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450"><rect width="800" height="450" fill="#16243f"/><g fill="none" stroke="#dce9f4"><circle cx="200" cy="225" r="92"/><circle cx="400" cy="225" r="62"/><circle cx="600" cy="225" r="36"/><path d="M292 225h46M462 225h102" stroke-width="4"/></g><g fill="#d59b4a"><circle cx="165" cy="185" r="10"/><circle cx="230" cy="250" r="10"/><circle cx="400" cy="225" r="17"/><circle cx="600" cy="225" r="13"/></g></svg>',
'statistical.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450"><rect width="800" height="450" fill="#16243f"/><g fill="none" stroke="#dce9f4" opacity=".18" stroke-width="2"><path d="M45 120 C170 40 260 185 385 115 S620 70 755 145"/><path d="M45 220 C170 130 285 305 410 215 S635 150 755 255"/><path d="M45 330 C185 235 290 410 430 315 S635 250 755 350"/></g><circle cx="85" cy="85" r="13" fill="#d59b4a" opacity=".95"/><circle cx="140" cy="85" r="13" fill="#d59b4a" opacity=".95"/><circle cx="195" cy="85" r="13" fill="#d59b4a" opacity=".95"/><circle cx="250" cy="85" r="13" fill="#d59b4a" opacity=".95"/><circle cx="305" cy="85" r="13" fill="#d59b4a" opacity=".95"/><circle cx="360" cy="85" r="13" fill="#d59b4a" opacity=".72"/><circle cx="415" cy="85" r="10" fill="#d59b4a" opacity=".72"/><circle cx="470" cy="85" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="525" cy="85" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="580" cy="85" r="13" fill="#d59b4a" opacity=".95"/><circle cx="635" cy="85" r="13" fill="#d59b4a" opacity=".95"/><circle cx="690" cy="85" r="13" fill="#d59b4a" opacity=".95"/><circle cx="85" cy="143" r="13" fill="#d59b4a" opacity=".95"/><circle cx="140" cy="143" r="13" fill="#d59b4a" opacity=".95"/><circle cx="195" cy="143" r="13" fill="#d59b4a" opacity=".95"/><circle cx="250" cy="143" r="13" fill="#d59b4a" opacity=".95"/><circle cx="305" cy="143" r="13" fill="#d59b4a" opacity=".95"/><circle cx="360" cy="143" r="10" fill="#d59b4a" opacity=".72"/><circle cx="415" cy="143" r="10" fill="#dce9f4" opacity=".72"/><circle cx="470" cy="143" r="13" fill="#dce9f4" opacity=".72"/><circle cx="525" cy="143" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="580" cy="143" r="13" fill="#d59b4a" opacity=".95"/><circle cx="635" cy="143" r="13" fill="#d59b4a" opacity=".95"/><circle cx="690" cy="143" r="13" fill="#d59b4a" opacity=".95"/><circle cx="85" cy="201" r="10" fill="#dce9f4" opacity=".72"/><circle cx="140" cy="201" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="195" cy="201" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="250" cy="201" r="10" fill="#d59b4a" opacity=".72"/><circle cx="305" cy="201" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="360" cy="201" r="13" fill="#dce9f4" opacity=".95"/><circle cx="415" cy="201" r="13" fill="#dce9f4" opacity=".95"/><circle cx="470" cy="201" r="13" fill="#dce9f4" opacity=".95"/><circle cx="525" cy="201" r="13" fill="#dce9f4" opacity=".72"/><circle cx="580" cy="201" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="635" cy="201" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="690" cy="201" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="85" cy="259" r="13" fill="#dce9f4" opacity=".95"/><circle cx="140" cy="259" r="13" fill="#dce9f4" opacity=".72"/><circle cx="195" cy="259" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="250" cy="259" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="305" cy="259" r="13" fill="#dce9f4" opacity=".72"/><circle cx="360" cy="259" r="13" fill="#dce9f4" opacity=".95"/><circle cx="415" cy="259" r="13" fill="#dce9f4" opacity=".95"/><circle cx="470" cy="259" r="13" fill="#dce9f4" opacity=".95"/><circle cx="525" cy="259" r="13" fill="#dce9f4" opacity=".95"/><circle cx="580" cy="259" r="13" fill="#dce9f4" opacity=".95"/><circle cx="635" cy="259" r="10" fill="#dce9f4" opacity=".72"/><circle cx="690" cy="259" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="85" cy="317" r="13" fill="#dce9f4" opacity=".95"/><circle cx="140" cy="317" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="195" cy="317" r="13" fill="#d59b4a" opacity=".72"/><circle cx="250" cy="317" r="10" fill="#d59b4a" opacity=".72"/><circle cx="305" cy="317" r="13" fill="#dce9f4" opacity=".72"/><circle cx="360" cy="317" r="13" fill="#dce9f4" opacity=".95"/><circle cx="415" cy="317" r="13" fill="#dce9f4" opacity=".95"/><circle cx="470" cy="317" r="13" fill="#dce9f4" opacity=".95"/><circle cx="525" cy="317" r="13" fill="#dce9f4" opacity=".95"/><circle cx="580" cy="317" r="13" fill="#dce9f4" opacity=".72"/><circle cx="635" cy="317" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="690" cy="317" r="13" fill="#d59b4a" opacity=".72"/><circle cx="85" cy="375" r="10" fill="#d59b4a" opacity=".72"/><circle cx="140" cy="375" r="13" fill="#d59b4a" opacity=".95"/><circle cx="195" cy="375" r="13" fill="#d59b4a" opacity=".95"/><circle cx="250" cy="375" r="13" fill="#d59b4a" opacity=".95"/><circle cx="305" cy="375" r="10" fill="#d59b4a" opacity=".72"/><circle cx="360" cy="375" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="415" cy="375" r="10" fill="#6fa3d2" opacity=".72"/><circle cx="470" cy="375" r="10" fill="#dce9f4" opacity=".72"/><circle cx="525" cy="375" r="10" fill="#dce9f4" opacity=".72"/><circle cx="580" cy="375" r="10" fill="#d59b4a" opacity=".72"/><circle cx="635" cy="375" r="13" fill="#d59b4a" opacity=".95"/><circle cx="690" cy="375" r="13" fill="#d59b4a" opacity=".95"/><rect x="58" y="58" width="674" height="332" rx="18" fill="none" stroke="#dce9f4" opacity=".28"/><text x="72" y="418" fill="#dce9f4" opacity=".82" font-family="Arial,sans-serif" font-size="20" letter-spacing="3">CORRELATED FIELD FLUCTUATIONS</text></svg>',
'holography.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450">\n<defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6fa3d2" stop-opacity=".85"/><stop offset="1" stop-color="#16243f" stop-opacity=".05"/></linearGradient></defs>\n<rect width="800" height="450" fill="#16243f"/>\n<path d="M95 82 C190 48 610 48 705 82 C626 154 600 308 400 392 C200 308 174 154 95 82 Z" fill="url(#hg)" stroke="#dce9f4" stroke-width="3" opacity=".98"/>\n<g fill="none" stroke="#dce9f4" opacity=".46" stroke-width="2">\n<path d="M115 94 C208 70 592 70 685 94"/><path d="M143 124 C232 105 568 105 657 124"/><path d="M177 164 C255 150 545 150 623 164"/><path d="M217 214 C282 205 518 205 583 214"/><path d="M258 264 C309 260 491 260 542 264"/><path d="M304 316 C345 317 455 317 496 316"/><path d="M352 358 C375 362 425 362 448 358"/>\n<path d="M165 78 C220 168 260 294 400 392"/><path d="M240 68 C280 176 310 305 400 392"/><path d="M320 62 C340 184 360 316 400 392"/><path d="M480 62 C460 184 440 316 400 392"/><path d="M560 68 C520 176 490 305 400 392"/><path d="M635 78 C580 168 540 294 400 392"/>\n</g>\n<path d="M72 72 H728" stroke="#d59b4a" stroke-width="5"/><text x="610" y="58" fill="#f3e4cb" font-family="Arial,sans-serif" font-size="22">boundary</text><circle cx="400" cy="392" r="8" fill="#d59b4a"/>\n</svg>'
}

CSS += r'''
.toolkit-card{display:block;text-decoration:none;color:inherit;transition:transform .15s ease}.toolkit-card:hover{transform:translateY(-2px)}.toolkit-card:hover h3{text-decoration:underline}.topic-link{display:inline-block;margin-top:14px;font-family:Georgia,"Times New Roman",serif;font-size:16px;color:var(--blue)}
.topic-essay{max-width:900px}.topic-essay p{font-family:Georgia,"Times New Roman",serif;font-size:19px;line-height:1.72;color:#253954;margin:0 0 30px}.topic-essay p:last-child{margin-bottom:0}.topic-essay strong{color:var(--navy)}
@media(max-width:650px){.topic-essay p{font-size:17.5px;line-height:1.65}}
'''

(ASSETS/'css'/'site.css').write_text(CSS, encoding='utf-8')
(ASSETS/'js'/'site.js').write_text(JS, encoding='utf-8')
(ASSETS/'img'/'logo.svg').write_text(LOGO, encoding='utf-8')
(ASSETS/'img'/'hero.svg').write_text(HERO, encoding='utf-8')
for name,data in SVGS.items(): (ASSETS/'img'/name).write_text(data, encoding='utf-8')


def nav(prefix='', active=''):
    p = prefix
    grouped=[]
    last_group=None
    for x in ordered_projects:
        status=x.get('status','Active')
        group='Active' if status.lower() in ('active','open') else ('On hiatus' if 'hiatus' in status.lower() else ('Closed' if status.lower()=='closed' else status))
        if group != last_group:
            grouped.append(f'<div class="dropdown-group-label">{escape(group)}</div>')
            last_group=group
        grouped.append(f'''<a href="{p}projects/{x['slug']}.html">{escape(x['title'])}</a>
      <a class="sub" href="{p}projects/{x['slug']}-talks.html">Talks, presentations and posters</a>
      <a class="sub" href="{p}projects/{x['slug']}-publications.html">Publications</a>
      <a class="sub" href="{p}projects/{x['slug']}-links.html">Further info</a>''')
    proj_links = ''.join(grouped)
    def cls(key): return ' class="active"' if active == key else ''
    return f'''
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="{p}index.html"><img src="{p}assets/img/star-mark-white.png" alt="STELLAR Lab star mark"><span class="brand-copy">STELLAR Lab</span></a>
    <button class="menu-toggle" aria-label="Open navigation" aria-expanded="false">Menu</button>
    <nav class="nav" aria-label="Main navigation">
      <a href="{p}index.html"{cls('home')}>Home</a>
      <a href="{p}team.html"{cls('team')}>Our Team</a>
      <div class="dropdown">
        <button class="dropdown-toggle" aria-expanded="false">Projects ▾</button>
        <div class="dropdown-menu">
          <a href="{p}projects.html">All projects</a>
          {proj_links}
        </div>
      </div>
      <a href="{p}publications.html"{cls('publications')}>Publications</a>
      <a href="{p}positions.html"{cls('positions')}>Positions</a>
      <a href="{p}awards.html"{cls('awards')}>Awards</a>
      <a href="https://www.youtube.com/@stellarlabge" target="_blank" rel="noopener">StellarTube</a>
      <a href="{p}contact.html"{cls('contact')}>Contact</a>
    </nav>
  </div>
</header>'''


def footer(prefix=''):
    p=prefix
    return f'''
<footer class="site-footer">
 <div class="footer-inner">
   <div><div class="footer-brand"><img src="{p}assets/img/star-mark.png" alt=""><div><strong>The STELLAR Lab</strong><p>{TAGLINE}<br>University of Genova</p></div></div></div>
   <div><h3>Explore</h3><ul><li><a href="{p}team.html">Our Team</a></li><li><a href="{p}projects.html">Projects</a></li><li><a href="{p}publications.html">Publications</a></li><li><a href="{p}positions.html">Available positions</a></li></ul></div>
   <div><h3>Contact</h3><ul><li>Via Dodecaneso 33</li><li>16146 Genova GE, Italy</li><li><a href="mailto:{CONTACT}">{CONTACT}</a></li><li><a href="tel:+390103355111">+39 010 335 5111</a></li></ul></div>
 </div>
 <div class="footer-bottom"><div><span>© 2026 The STELLAR Lab</span><span>Self-hosted static site · no cookies or analytics included by default</span></div></div>
</footer>'''


def layout(title, content, *, prefix='', active='', description=''):
    css = prefix+'assets/css/site.css'
    js = prefix+'assets/js/site.js'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} · {SITE_NAME}</title><meta name="description" content="{escape(description or TAGLINE)}"><link rel="icon" href="{prefix}assets/img/star-mark.png"><link rel="stylesheet" href="{css}"></head>
<body><a class="skip" href="#content">Skip to content</a>{nav(prefix,active)}<main id="content">{content}</main>{footer(prefix)}<script src="{js}" defer></script></body></html>'''


def pagehero(title, lead='', crumbs=None, prefix=''):
    bc=''
    if crumbs:
        chunks=[]
        for label, href in crumbs:
            chunks.append(f'<a href="{href}">{escape(label)}</a>')
        bc='<div class="breadcrumbs">'+'<span>›</span>'.join(chunks)+'</div>'
    return f'''<section class="page-hero"><div class="section">{bc}<h1>{escape(title)}</h1>{f'<p class="lead">{escape(lead)}</p>' if lead else ''}</div></section>'''

def status_badge(project):
    status=project.get('status','Active')
    cls='status-hiatus' if status.lower()=='on hiatus' else 'status-active'
    return f'<span class="status-badge {cls}">{escape(status)}</span>'


def publication_html(year, title, venue, include_abstract=False):
    aid=ARXIV.get(title)
    if aid:
        url='https://arxiv.org/abs/'+aid
        title_html=f'<a href="{url}" target="_blank" rel="noopener">{escape(title)}</a>'
        links=f'<div class="pub-links"><a class="pub-link" href="{url}" target="_blank" rel="noopener">arXiv:{escape(aid)} ↗</a></div>'
    else:
        title_html=escape(title)
        links=''
    abstract_html=''
    if include_abstract:
        abstract=ABSTRACTS.get(title)
        if abstract:
            abstract_html=f'<div class="pub-abstract"><span>Abstract</span><p>{escape(abstract)}</p></div>'
    return f'<article class="pub" data-year="{year}"><div class="pub-year">{year}</div><div><h3>{title_html}</h3><p class="pub-venue">{escape(venue)}</p>{links}{abstract_html}</div></article>'


# Home
home_cards = [
('Statistical field theory','Universal behaviour, collective phenomena, non-equilibrium systems and active matter.','statistical-toolkit.png','statistical-field-theory.html'),
('Hydrodynamics','Effective theories of conserved and approximately conserved quantities, transport and driven steady states.','hydrodynamics-toolkit.png','hydrodynamics.html'),
('Holography','Gauge-gravity duality as a laboratory for strongly coupled matter and transport.','holography-concept.png','holography.html')]
cards_html=''.join(f'''<a class="card toolkit-card" href="{href}" aria-label="Read our overview of {escape(t)}"><div class="card-media"><img src="assets/img/{img}" alt="Illustration for {escape(t)}"></div><div class="card-body"><h3>{escape(t)}</h3><p>{escape(d)}</p><span class="topic-link">Read overview →</span></div></a>''' for t,d,img,href in home_cards)
active_projects=[p for p in ordered_projects if p.get('status','Active').lower() in ('active','open')]
project_preview=''.join(f'''<article class="programme-card"><div class="card-media"><img src="assets/img/{p['img']}" alt="Illustration for {escape(p['title'])}"></div><div class="card-body">{status_badge(p)}<h3>{escape(p['title'])}</h3><p>{escape(p['summary'])}</p><a class="btn" href="projects/{p['slug']}.html">Project page →</a></div></article>''' for p in active_projects)
home = f'''
<section class="hero"><div class="hero-grid"><div class="hero-copy"><p class="eyebrow">Department of Physics · University of Genova</p><h1>Statistical field theory,<br>hydrodynamics and holography</h1><p>The STELLAR Lab at the University of Genova explores collective behaviour in many-body systems using tools from statistical field theory, hydrodynamics and holography, bridging analytic, numerical and computational approaches across physics.</p></div></div></section>
<section class="toolkit-section" id="toolkits"><div class="section"><div class="section-heading"><div><p class="eyebrow">How we work</p><h2>Three overlapping toolkits</h2></div></div><div class="toolkit-grid">{cards_html}</div></div></section>
<section class="section active-projects"><div class="section-heading"><div><p class="eyebrow">Research programmes</p><h2>Selected active projects</h2></div><a class="text-link" href="projects.html">View all projects →</a></div><div class="research-programme-grid">{project_preview}</div></section>'''
(ROOT/'index.html').write_text(layout('Home',home,active='home',description='STELLAR Lab at the University of Genova: statistical field theory, hydrodynamics and holography.'),encoding='utf-8')

# Broad research-topic overviews linked from the landing page.
topic_pages = [
    {
        'slug':'statistical-field-theory',
        'title':'Statistical field theory',
        'eyebrow':'Collective behaviour · criticality · fluctuations',
        'image':'statistical-toolkit.png',
        'description':'An introduction to statistical field theory, modern developments, and the STELLAR Lab contributions.',
        'paragraphs':[
            'Statistical field theory is the language we use when the microscopic description of a many-body system contains far more information than is needed to understand its large-scale behaviour. The basic move is to replace the individual degrees of freedom by coarse-grained fields - an order parameter, a density, a phase, a current - and to ask which effective theory governs their fluctuations. Near a continuous phase transition this leads naturally to universality: microscopically different systems can share the same long-distance physics because the renormalisation group removes details that are irrelevant at large scales. Fixed points, scaling dimensions and relevant deformations then organise the problem, while correlation functions encode the observable fluctuations. Statistical field theory is therefore not simply quantum field theory with the word statistical added to it. It is a general framework for turning the hierarchy of scales in a many-body problem into a controlled description of collective phenomena, whether the system is at equilibrium, close to a critical point, or driven away from equilibrium.',
            'The modern subject has become both more precise and substantially broader. At criticality, the conformal bootstrap can determine scaling dimensions and operator-product data without relying on a weak-coupling expansion, while conformal perturbation theory provides a systematic way of using this information away from the fixed point. Renormalisation-group methods remain central, but they are now routinely combined with lattice calculations, Monte Carlo methods and high-precision numerical information. At the same time, statistical field theory has moved decisively into non-equilibrium physics. Martin-Siggia-Rose and Schwinger-Keldysh formulations allow noise, response and dissipation to be treated directly at the level of an action, while active matter forces us to confront field theories in which detailed balance is absent from the outset. Large-deviation methods and stochastic effective theories add a complementary description of rare fluctuations. The important point is that these are not disconnected developments: they are different ways of asking which parts of microscopic dynamics survive coarse graining and which constraints continue to control the infrared theory.',
            'Our contributions sit on both sides of this equilibrium and non-equilibrium divide. We have developed and applied conformal perturbation theory to extract off-critical observables from critical data and confronted those predictions with lattice results, while related work has studied confinement and effective strings in three-dimensional gauge theories. We have also used duality and topological field theory to understand phases and infrared equivalences that are not captured by ordinary Landau symmetry breaking. On the non-equilibrium side, our work on flocking matter has identified thermodynamic constraints and exact scaling information, and our broader programme uses statistical field theory to connect active matter, fluctuating hydrodynamics and stochastic effective descriptions. Across these projects the aim is the same: not to write down the most general field theory that symmetry permits, but to determine which structures are actually forced by universality, probability, thermodynamics or the underlying microscopic dynamics, and then to test those structures against analytical, numerical or lattice information.'
        ]
    },
    {
        'slug':'hydrodynamics',
        'title':'Hydrodynamics',
        'eyebrow':'Conservation laws · transport · effective theory',
        'image':'hydrodynamics-toolkit.png',
        'description':'An introduction to hydrodynamics, modern developments, and the STELLAR Lab contributions.',
        'paragraphs':[
            'Hydrodynamics is the effective theory of a many-body system on distances and times long compared with its microscopic relaxation scales. Its starting point is unusually economical: identify the quantities that are conserved, or sufficiently slowly relaxing, and write the most general constitutive relations compatible with symmetry and thermodynamics. Energy, momentum and charge then obey conservation equations, while transport coefficients such as viscosity, conductivity and diffusion constants determine how the system returns towards equilibrium. The derivative expansion makes this statement quantitative by ordering corrections according to the number of spacetime gradients. Nothing in this construction requires a weakly interacting gas or long-lived quasiparticles, which is why hydrodynamics can apply equally well to ordinary fluids, quark-gluon plasma, strongly correlated electronic matter and many other systems. Its power is also its limitation: hydrodynamics is universal because it forgets most microscopic information, so one must understand both the constraints that make the effective theory consistent and the scales at which the hydrodynamic description ceases to be reliable.',
            'Several developments have changed what we now mean by hydrodynamic theory. Gauge-gravity duality made it possible to calculate transport and real-time response in strongly coupled quantum field theories and, through the fluid-gravity correspondence, showed directly how relativistic fluid dynamics emerges from black-hole dynamics in an appropriate long-wavelength limit. Schwinger-Keldysh effective field theory has supplied a complementary advance: dissipation and thermal noise can be placed in a single action, with dynamical KMS symmetry encoding fluctuation-dissipation relations and higher-point constraints. Relativistic hydrodynamics has also been pushed beyond naive first-order formulations by stable and causal theories with additional relaxation scales. More generally, quasihydrodynamics treats approximately conserved quantities and other long-lived modes on the same footing as the ordinary conserved densities. These ideas are now meeting questions about fluctuations, memory, branch cuts, active matter and driven steady states, so the frontier is no longer simply the computation of another transport coefficient. It is the problem of identifying the correct degrees of freedom and the correct analytic structure of response beyond the strict hydrodynamic limit.',
            'Hydrodynamics is the central thread joining much of our work. We have studied anomalous and magnetohydrodynamic transport in strongly correlated systems, including Weyl semimetals and charge-density-wave phases, and developed relaxed and quasihydrodynamic descriptions of electrically driven non-equilibrium steady states. We have worked on hydrodynamics without boost symmetry, both as a general theoretical framework and because it is directly relevant to systems such as active matter. A second strand asks where the hydrodynamic expansion fails: we study pole collisions, the radius of convergence of gradient expansions, the relation between static and dynamical scales, and effective descriptions in which non-hydrodynamic poles or branch cuts are retained explicitly. A third strand concerns fluctuations. Using Schwinger-Keldysh effective theory, we have investigated Maxwell-Cattaneo transport, local descriptions of additional relaxation modes, and the positivity constraints that must be imposed on non-Gaussian noise if the effective action is to admit a genuine stochastic interpretation. The common aim is to turn hydrodynamics from a formal derivative expansion into a controlled effective theory with a clear domain of validity.'
        ]
    },
    {
        'slug':'holography',
        'title':'Holography',
        'eyebrow':'Gauge-gravity duality · strong coupling · real-time response',
        'image':'holography-concept.png',
        'description':'An introduction to holography, modern developments, and the STELLAR Lab contributions.',
        'paragraphs':[
            'Holography, in the sense used in our work, is the gauge-gravity duality: the statement that certain quantum field theories can be described equivalently by a gravitational theory in one higher dimension. The best understood examples arise from AdS/CFT, where a strongly coupled field theory lives on the boundary of an asymptotically anti-de Sitter spacetime. The dictionary is useful because difficult many-body questions on the field-theory side can become classical boundary-value problems in gravity. At finite temperature the dual geometry contains a black hole, sources for field-theory operators are encoded in boundary values of bulk fields, and the quasinormal modes of the black hole determine poles of retarded correlation functions. This gives access to thermodynamics, transport and real-time relaxation in regimes where ordinary perturbation theory is ineffective. Holography is not a claim that every strongly correlated material literally possesses a simple gravitational dual. Its value is that it supplies controlled strongly coupled theories in which general ideas about transport, collective modes and effective descriptions can be calculated and tested explicitly.',
            'The subject has moved well beyond the original calculation of equilibrium observables. Holographic models now provide laboratories for momentum relaxation, strange-metal transport, superconductivity, charge-density waves, phonons and other phases with broken symmetries. Real-time response has become increasingly important: quasinormal spectra let one follow the transition from hydrodynamic poles to non-hydrodynamic relaxation, while the analytic continuation of correlators exposes pole collisions, branch structure and the limits of low-frequency effective theories. Duality transformations can reorganise the same response in nontrivial ways by exchanging poles and zeros. Holography has also become intertwined with effective field theory rather than standing apart from it. One can derive hydrodynamic coefficients from gravity, identify additional long-lived degrees of freedom, and then ask which part of the gravitational answer can be reproduced by a local or quasihydrodynamic action. This is a more demanding use of the correspondence than simply producing a transport curve: the gravitational model becomes a microscopic benchmark against which the assumptions of an infrared theory can be tested.',
            'Our holographic work has followed precisely this route. We have studied transport in systems with momentum relaxation, magnetic fields and charge-density-wave order, including holographic phonons and the emergence of universal relaxation scales. We have used probe-brane systems and electromagnetic duality to understand strongly coupled quantum matter, including cases in which changing the quantisation or applying an SL(2,Z) transformation changes the pole content that an infrared effective theory must retain. Holography also provides a controlled setting for our work on driven steady states and quasihydrodynamics, where forcing is balanced by relaxation and additional slow modes modify ordinary hydrodynamic response. More recently, we have used black-hole quasinormal modes and holographic correlators to study the analytic structure that ultimately limits hydrodynamic expansions. In all of these applications the gravitational construction is not the final objective. We use it to obtain exact or numerically controlled information at strong coupling, and then ask which features are universal enough to survive in an effective description that can be compared across holography, quantum field theory and condensed-matter systems.'
        ]
    }
]

for topic in topic_pages:
    paras=''.join(f'<p>{escape(par)}</p>' for par in topic['paragraphs'])
    content=f'''<section class="page-hero"><div class="section project-hero-grid"><div><div class="breadcrumbs"><a href="index.html">Home</a><span>›</span><a href="index.html#toolkits">Three overlapping toolkits</a></div><p class="eyebrow">{escape(topic['eyebrow'])}</p><h1>{escape(topic['title'])}</h1></div><img src="assets/img/{escape(topic['image'])}" alt="Illustration for {escape(topic['title'])}"></div></section><section class="section narrow topic-essay">{paras}</section>'''
    (ROOT/f"{topic['slug']}.html").write_text(layout(topic['title'],content,active='home',description=topic['description']),encoding='utf-8')

# Team
def obfuscated_email(email):
    if '@' not in email:
        return email
    local,domain=email.split('@',1)
    return f'{local} [AT] {domain}'

def team_card(person):
    name=person['name']
    orcid=person.get('orcid')
    heading=f'<div class="person-heading"><h3>{escape(name)}</h3>'
    if orcid:
        heading+=f'<a class="identity-link" href="https://orcid.org/{escape(orcid)}" target="_blank" rel="noopener" aria-label="ORCID for {escape(name)}">{escape(orcid)} ↗</a>'
    heading+='</div>'
    links=[]
    if person.get('website'):
        links.append(f'<a class="person-link" href="{escape(person["website"])}" target="_blank" rel="noopener">{escape(person.get("website_label") or "Personal website")} ↗</a>')
    if person.get('profile'):
        links.append(f'<a class="person-link" href="{escape(person["profile"])}" target="_blank" rel="noopener">{escape(person.get("profile_label") or "Profile")} ↗</a>')
    if person.get('cv'):
        cv=person['cv']
        if cv.startswith(('http://','https://')):
            raise ValueError(f"CVs must be self-hosted, not external: {person['name']} -> {cv}")
        cv_path = ROOT / cv
        if not cv_path.exists():
            raise FileNotFoundError(f"Missing self-hosted CV for {person['name']}: {cv_path}")
        links.append(f'<a class="person-link" href="{escape(cv)}">{escape(person.get("cv_label") or "CV")} ↓</a>')
    scholarly=SCHOLARLY_PROFILES.get(name, {})
    for key,label in [('inspire','INSPIRE'),('arxiv','arXiv'),('wos','Web of Science')]:
        if scholarly.get(key):
            links.append(f'<a class="person-link scholarly-link" href="{escape(scholarly[key])}" target="_blank" rel="noopener">{label} ↗</a>')
    link_html=f'<div class="person-links">{"".join(links)}</div>' if links else ''
    img=person['img']
    img_src=img if img.startswith(('http://','https://')) else f'assets/img/team/{img}'
    mail_html=''
    if person.get('email'):
        mail_html=f'<span class="mail">{escape(obfuscated_email(person["email"]))}</span>'
    return f'''<article class="person"><div class="avatar"><img src="{escape(img_src)}" alt="Portrait of {escape(name)}"></div><div>{heading}<div class="role">{escape(person['role'])}</div><p>{escape(person['bio'])}</p>{mail_html}{link_html}</div></article>'''

team_cards=''.join(team_card(person) for person in team)
associate_cards=''.join(team_card(person) for person in associates)

def former_card(person):
    links=list(person.get('links', []))
    scholarly=SCHOLARLY_PROFILES.get(person['name'], {})
    links.extend((label,scholarly[key]) for key,label in [('inspire','INSPIRE'),('arxiv','arXiv'),('wos','Web of Science')] if scholarly.get(key))
    link_html=''
    if links:
        link_html='<div class="person-links">'+''.join(
            f'<a class="person-link" href="{escape(url)}" target="_blank" rel="noopener">{escape(label)} ↗</a>'
            for label,url in links
        )+'</div>'
    return f'''<div class="simple-item"><h3>{escape(person['name'])}</h3><div class="role">{escape(person['role'])}</div><p>{escape(person['bio'])}</p>{link_html}</div>'''

former_html=''.join(former_card(person) for person in former)
def student_card(student):
    title=f'<em>{escape(student["title"])}</em>'
    note=f'{escape(student["name"].split()[0])}’s Master’s thesis, {title}, {escape(student["note"].split(" thesis ",1)[-1] if " thesis " in student["note"] else student["note"])}'
    # The note fields are already complete prose; use them directly to avoid duplicating the title.
    note=escape(student['note'])
    links=''
    if student.get('link'):
        links=f'<div class="person-links"><a class="person-link" href="{escape(student["link"])}" target="_blank" rel="noopener">{escape(student.get("link_label") or "Thesis record")} ↗</a></div>'
    return f'''<div class="simple-item"><div class="role">{escape(student['year'])}</div><h3>{escape(student['name'])}</h3><p><strong>{title}</strong><br>{note}</p>{links}</div>'''

students_html=''.join(student_card(student) for student in research_students)
team_page=pagehero('Our Team','Researchers working across statistical field theory, hydrodynamics, holography and condensed-matter theory.')+f'''<section class="section"><p class="eyebrow">Current members</p><div class="team-grid">{team_cards}</div></section><section class="band"><div class="section"><p class="eyebrow">Collaborators</p><h2>STELLAR Associates</h2><p class="lead alumni-intro">Researchers outside the group who work closely with STELLAR on shared scientific problems.</p><div class="team-grid">{associate_cards}</div></div></section><section class="section"><p class="eyebrow">Alumni</p><h2>Former group members</h2><p class="lead alumni-intro">Where known, we record the next position taken after leaving STELLAR.</p><div class="simple-list">{former_html}</div></section><section class="band"><div class="section"><p class="eyebrow">Research students</p><h2>Student projects</h2><div class="simple-list">{students_html}</div></div></section>'''
(ROOT/'team.html').write_text(layout('Our Team',team_page,active='team'),encoding='utf-8')

# Projects overview
proj_cards=''.join(f'''<article class="card"><div class="card-media"><img src="assets/img/{p['img']}" alt=""></div><div class="card-body">{status_badge(p)}<div class="kicker">{escape(p['kicker'])}</div><h3>{escape(p['title'])}</h3><p>{escape(p['summary'])}</p><div class="button-row"><a class="btn" href="projects/{p['slug']}.html">Open project →</a></div></div></article>''' for p in ordered_projects)
projects_page=pagehero('Projects','Seven connected research programmes spanning critical phenomena, exotic dynamics, non-equilibrium fluctuations, hydrodynamics, holography and superconductivity. Two programmes are currently on hiatus.')+f'''<section class="section"><div class="cards">{proj_cards}</div></section>'''
(ROOT/'projects.html').write_text(layout('Projects',projects_page,active='projects'),encoding='utf-8')

# Publications
years=sorted({y for y,_,_ in publications}, reverse=True)
opts=''.join(f'<option value="{y}">{y}</option>' for y in years)
pubs_html=''.join(publication_html(y,title,venue,include_abstract=True) for y,title,venue in publications)
pubs_page=pagehero('All publications','Publications by STELLAR Lab members and collaborators, with direct arXiv links where an arXiv record is available.')+f'''<section class="section narrow"><div class="pub-controls"><input id="pub-search" type="search" placeholder="Search titles or journals" aria-label="Search publications"><select id="pub-year" aria-label="Filter by year"><option value="all">All years</option>{opts}</select></div><div id="pub-count" class="result-count"></div><div class="pub-list">{pubs_html}</div></section>'''
(ROOT/'publications.html').write_text(layout('Publications',pubs_page,active='publications'),encoding='utf-8')

# Positions
positions=pagehero('Available positions','There are currently no open positions advertised by the STELLAR Lab.')+f'''<section class="section narrow"><div class="callout closed-callout"><strong>Closed.</strong> The postdoctoral call below is no longer accepting applications. It is retained here as an archive of the previous opportunity.</div><p class="eyebrow" style="margin-top:42px">Archived postdoctoral call</p><h2>One or two postdoctoral positions</h2><p class="lead">This call is closed. The original advert described one or two postdoctoral positions, initially for two years with the possibility of a further two years subject to performance and funding.</p><div class="content-grid"><div><h3>Research fit</h3><p>The call sought researchers working in areas including active matter, simulations of large numbers of interacting particles, numerical fluid dynamics, particle-swarm optimisation, critical phenomena and Schwinger-Keldysh approaches to hydrodynamics.</p><h3>Application material</h3><p>The original application requested a research statement, a CV including publications, and two recommendation letters.</p><div class="button-row"><a class="btn" href="https://academicjobsonline.org/ajo?joblist---4325-30562" target="_blank" rel="noopener">Archived advert ↗</a><a class="btn" href="mailto:{CONTACT}">Contact the lab</a></div></div><aside class="aside"><h3>Archived terms</h3><p><strong>Status</strong><br>Closed</p><p><strong>Original duration</strong><br>2 years initially</p><p><strong>Possible extension</strong><br>Up to 2 further years, subject to funding and performance</p><p><strong>Indicative net salary</strong><br>Approx. €1,900/month plus benefits</p><p><strong>Group heads</strong><br>Andrea Amoretti<br>Daniel K. Brattan<br>Nicodemo Magnoli</p></aside></div></section>'''
(ROOT/'positions.html').write_text(layout('Available positions',positions,active='positions'),encoding='utf-8')

# Awards
grant_html=''.join(f'''<article class="grant"><div class="grant-year">{escape(year or '—')}</div><div><h3>{escape(title)}</h3><p>{escape(source)}{(' · '+escape(detail)) if detail else ''}</p></div><div class="grant-amount">{escape(amount)}</div></article>''' for year,title,source,detail,amount in awards)
awards_page=pagehero('Awards and grants','Selected funding supporting the lab and its research programmes.')+f'''<section class="section narrow"><div>{grant_html}</div></section>'''
(ROOT/'awards.html').write_text(layout('Awards and grants',awards_page,active='awards'),encoding='utf-8')

# Contact
contact_page=pagehero('Contact','Find the lab at the Department of Physics, University of Genova.')+f'''<section class="section"><div class="contact-grid"><div class="address-art"><div class="pin" aria-hidden="true"></div><h3>The STELLAR Lab</h3><p>Via Dodecaneso, 33<br>16146 Genova GE<br>Italy</p></div><div class="contact-card"><p class="eyebrow">Get in touch</p><h2>Contact the group</h2><p><strong>Email</strong><br><a href="mailto:{CONTACT}">{CONTACT}</a></p><p><strong>Telephone</strong><br><a href="tel:+390103355111">(+39) 010 335 5111</a></p><div class="button-row"><a class="btn primary" href="mailto:{CONTACT}">Email STELLAR</a><a class="btn" href="https://www.openstreetmap.org/search?query=Via%20Dodecaneso%2033%20Genova" target="_blank" rel="noopener">Open map ↗</a></div></div></div></section>'''
(ROOT/'contact.html').write_text(layout('Contact',contact_page,active='contact'),encoding='utf-8')

# Project pages and their three local resource pages.
for p in ordered_projects:
    slug=p['slug']
    prefix='../'
    crumbs=[('Home','../index.html'),('Projects','../projects.html'),(p['title'],f'{slug}.html')]
    qhtml=''.join(f'<div class="question">{escape(q)}</div>' for q in p['questions'])
    resource=f'''<div class="resource-nav"><a href="{slug}-talks.html">Talks, presentations and posters</a><a href="{slug}-publications.html">Publications</a><a href="{slug}-links.html">Further info</a></div>'''
    hero=f'''<section class="page-hero"><div class="section project-hero-grid"><div><div class="breadcrumbs"><a href="../index.html">Home</a><span>›</span><a href="../projects.html">Projects</a></div>{status_badge(p)}<p class="eyebrow">{escape(p['kicker'])}</p><h1>{escape(p['title'])}</h1><p class="lead">{escape(p['summary'])}</p>{resource}</div><img src="../assets/img/{p['img']}" alt="Abstract illustration for {escape(p['title'])}"></div></section>'''
    strand_html=''.join(f'<li>{escape(item)}</li>' for item in p.get('strands', []))
    strand_section=f'''<section class="band"><div class="section narrow"><p class="eyebrow">Programme strands</p><h2>What is currently in this programme</h2><ul class="programme-strands">{strand_html}</ul></div></section>''' if strand_html else ''
    body=hero+f'''<section class="section"><p class="eyebrow">Research questions</p><h2>What we are trying to understand</h2><div class="question-list">{qhtml}</div></section>'''+strand_section+f'''<section class="band"><div class="section narrow"><p class="eyebrow">Why it matters</p><h2>Impact and connections</h2><p class="lead">{escape(p['impact'])}</p></div></section>'''
    (ROOT/'projects'/f'{slug}.html').write_text(layout(p['title'],body,prefix='../',active='projects'),encoding='utf-8')

    talks=project_talks[slug]
    if talks:
        items=[]
        for talk in talks:
            if isinstance(talk, dict):
                links=[]
                if talk.get('url'): links.append(f'<a href="{escape(talk["url"])}" target="_blank" rel="noopener">{escape(talk.get("url_label","Conference website"))} ↗</a>')
                if talk.get('programme'): links.append(f'<a href="{escape(talk["programme"])}" target="_blank" rel="noopener">Programme ↗</a>')
                if talk.get('contribution'): links.append(f'<a href="{escape(talk["contribution"])}" target="_blank" rel="noopener">Contribution page ↗</a>')
                if talk.get('abstract_url'): links.append(f'<a href="{escape(talk["abstract_url"])}" target="_blank" rel="noopener">{escape(talk.get("abstract_label","Official abstract"))} ↗</a>')
                if talk.get('slides'): links.append(f'<a href="{escape(talk["slides"])}" target="_blank" rel="noopener">Slides ↗</a>')
                if talk.get('slides_page'): links.append(f'<a href="{escape(talk["slides_page"])}" target="_blank" rel="noopener">{escape(talk.get("slides_page_label","Slides on conference page"))} ↗</a>')
                if talk.get('video'): links.append(f'<a href="{escape(talk["video"])}" target="_blank" rel="noopener">{escape(talk.get("video_label","StellarTube video"))} ↗</a>')
                if talk.get('related_url'): links.append(f'<a href="{escape(talk["related_url"])}" target="_blank" rel="noopener">{escape(talk.get("related_label","Related paper"))} ↗</a>')
                for label,url in talk.get('related_links',[]):
                    links.append(f'<a href="{escape(url)}" target="_blank" rel="noopener">{escape(label)} ↗</a>')
                meta=[]
                for label,key in [('Presenter','presenter'),('Authors','authors'),('Conference','conference'),('Conference dates','conference_dates'),('Presentation date','date'),('Time','time'),('Venue','venue')]:
                    if talk.get(key): meta.append(f'<div><dt>{label}</dt><dd>{escape(talk[key])}</dd></div>')
                meta_html=f'<dl class="talk-meta">{"".join(meta)}</dl>' if meta else ''
                abstract_html=''
                if talk.get('abstract'):
                    note=f'<p class="talk-source-note">{escape(talk["abstract_note"])}</p>' if talk.get('abstract_note') else ''
                    abstract_html=f'<div class="talk-abstract"><h4>Abstract</h4><p>{escape(talk["abstract"])}</p>{note}</div>'
                link_html=f'<div class="talk-links">{"".join(links)}</div>' if links else ''
                items.append(f'<article class="talk-card"><p class="talk-type">{escape(talk.get("type","Presentation"))}</p><h3>{escape(talk["title"])}</h3>{meta_html}{abstract_html}{link_html}</article>')
            else:
                t,where,date=talk
                items.append(f'<article class="talk-card"><h3>{escape(t)}</h3><p>{escape(where)} · {escape(date)}</p></article>')
        inner=''.join(items)
    else:
        inner='<div class="empty">Nothing to display at present.</div>'
    tpage=pagehero('Talks, presentations and posters',p['title'],crumbs=[('Projects','../projects.html'),(p['title'],f'{slug}.html'),('Talks','#')],prefix='../')+f'''<section class="section narrow"><div class="talk-list">{inner}</div></section>'''
    (ROOT/'projects'/f'{slug}-talks.html').write_text(layout(f"Talks - {p['title']}",tpage,prefix='../',active='projects'),encoding='utf-8')

    ph=''.join(publication_html(y,t,v,include_abstract=True) for y,t,v in project_pubs[slug])
    ppage=pagehero('Publications',p['title'],crumbs=[('Projects','../projects.html'),(p['title'],f'{slug}.html'),('Publications','#')],prefix='../')+f'''<section class="section narrow"><div class="pub-list">{ph}</div><div class="button-row"><a class="btn" href="../publications.html">Browse all lab publications</a></div></section>'''
    (ROOT/'projects'/f'{slug}-publications.html').write_text(layout(f"Publications - {p['title']}",ppage,prefix='../',active='projects'),encoding='utf-8')

    link_groups=project_links[slug]
    if link_groups:
        sections=[]
        for group in link_groups:
            items=[]
            for item in group.get('links',[]):
                if len(item)==3:
                    label,url,desc=item
                else:
                    label,url=item
                    desc=''
                desc_html=f'<span class="resource-description">{escape(desc)}</span>' if desc else ''
                items.append(f'<a href="{escape(url)}" target="_blank" rel="noopener"><span class="resource-link-title">{escape(label)}</span>{desc_html}</a>')
            intro=f'<p class="resource-section-intro">{escape(group["intro"])}</p>' if group.get('intro') else ''
            sections.append(f'<section class="resource-section"><h2>{escape(group["title"])}</h2>{intro}<div class="external-list resource-list">{"".join(items)}</div></section>')
        linner=''.join(sections)
    else:
        linner='<div class="empty">No additional links are currently listed for this project.</div>'
    lpage=pagehero('Further info',p['title'],crumbs=[('Projects','../projects.html'),(p['title'],f'{slug}.html'),('Further info','#')],prefix='../')+f'''<section class="section narrow"><p class="further-info-intro">A curated set of accessible background pages, reviews and lecture notes related to this research programme.</p>{linner}</section>'''
    (ROOT/'projects'/f'{slug}-links.html').write_text(layout(f"Further info - {p['title']}",lpage,prefix='../',active='projects'),encoding='utf-8')

# 404, robots, sitemap and README.
(ROOT/'talks.html').unlink(missing_ok=True)
notfound=pagehero('Page not found','The requested page is not part of this static site.')+'''<section class="section narrow"><a class="btn primary" href="index.html">Return home</a></section>'''
(ROOT/'404.html').write_text(layout('404',notfound),encoding='utf-8')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n',encoding='utf-8')

all_html=sorted([x.relative_to(ROOT).as_posix() for x in ROOT.rglob('*.html')])
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>https://YOUR-DOMAIN.example/{escape(x)}</loc></url>\n' for x in all_html)+'</urlset>\n',encoding='utf-8')

README = '''# STELLAR Lab self-hosted website\n\nThis folder is a complete static replacement for the former Google Sites website. It uses plain HTML, CSS and a very small amount of JavaScript. There is no framework, database, cookie banner, external font, image CDN or build step.\n\n## Preview locally\n\nFrom this folder, run:\n\n    python3 -m http.server 8000\n\nThen open `http://localhost:8000/`. You can also open `index.html` directly in a browser.\n\n## Deploy\n\nUpload the *contents of this folder* to any static host (GitHub Pages, GitLab Pages, Netlify, Cloudflare Pages, university web space, Apache or Nginx). `index.html` is the site entry point.\n\nFor GitHub Pages, push this folder to a repository and publish the repository root. For Netlify/Cloudflare Pages, use this folder as the publish directory and leave the build command empty.\n\n## Edit the site\n\n- Global styles: `assets/css/site.css`\n- Mobile menu and publication filter: `assets/js/site.js`\n- Local artwork/logo: `assets/img/`\n- Main pages: root `.html` files\n- Project and resource pages: `projects/`\n\nThe HTML already uses relative URLs, so it can be hosted under a subdirectory as well as at a domain root.\n\n## Before launch\n\n1. Replace `YOUR-DOMAIN.example` in `sitemap.xml` with the real domain.\n2. Review `positions.html`: the migrated postdoc advert includes a priority date that has already passed.\n3. The approved homepage concept artwork and the lab branding are stored locally in `assets/img/`; no image depends on Google Sites.\n4. Add analytics only if you actually want it; none is included now.\n\n## Content provenance\n\nThe structure and research content were migrated from the STELLAR Lab's public Google Site in October 2026 and rewritten for a cleaner self-hosted presentation.\n'''
(ROOT/'README.md').write_text(README,encoding='utf-8')
print(f'Built {len(all_html)} HTML pages in {ROOT}')
