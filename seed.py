from app import db
from models import Pet

db.drop_all()
db.create_all()

p = Pet(name="Porky",
         species="porcupine",
         photo_url="https://t3.ftcdn.net/jpg/02/76/86/86/360_F_276868673_t79Oz5JNkoBQnzXrLyr48iafDs27irVR.jpg",
         age=5,
         notes="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut.",
         available=True)
db.session.add(p)
db.session.commit()

p = Pet(name="Crackle",
         species="cat",
         photo_url="https://nationalzoo.si.edu/sites/default/files/animals/caracal-002.jpg",
         age=12,
         notes="Epsum factorial non deposit quid pro quo hic escorol. Olypian quarrels et gorilla congolium sic.",
         available=False)
db.session.add(p)
db.session.commit()

p = Pet(name="Titan",
         species="dog",
         photo_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F11%2F16%2Fboston-terrier-1166523625-2000.jpg",
         age=3,
         notes="Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por.",
         available=True)
db.session.add(p)
db.session.commit()

p = Pet(name="Bart",
         species="cat",
         photo_url="https://i2-prod.examinerlive.co.uk/incoming/article18110990.ece/ALTERNATES/s615/0_Ikiru-1.jpg",
         age=7,
         notes="Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam.",
         available=True)
db.session.add(p)
db.session.commit()

p = Pet(name="Hoss",
         species="porcupine",
         photo_url="https://cdn.mos.cms.futurecdn.net/jFpJp5sJzEeeKtjAnHRM8K-1200-80.jpg",
         age=10,
         notes="Epsum factorial non deposit quid pro quo hic escorol. Olypian quarrels et gorilla congolium sic.",
         available=False)
db.session.add(p)
db.session.commit()
