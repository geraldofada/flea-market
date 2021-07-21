const validateCpf = (cpf) => {
  const numbers = [...cpf].map(n => parseInt(n, 10));

  let sum = 0;
  for (let i=0; i<9; i++)
    sum += numbers[i] * (i + 1);
  let fst_dig = sum % 11;

  sum = 0;
  for (let i=0; i<10; i++)
    sum += numbers[i] * i;
  let sec_dig = sum % 11;

  if (fst_dig === 10) fst_dig = 0;
  if (sec_dig === 10) sec_dig = 0;

  if (numbers[9] === fst_dig && numbers[10] === sec_dig)
    return true;
  else
    return false;
};

const toProduct = (products) => {
  const res = [];
  for (p of products) {
    const newUser = new User(
      p.owner.name,
      p.owner.cpf,
      p.owner.email,
      p.owner.nickname
    );

    const newProduct = new Product(
      p.name,
      p.cat,
      p.price,
      newUser,
      p.description,
      p.img
    );

    res.push(newProduct);
  }

  return res;
};

function Product(name, cat, price, owner, description, img) {
  this.name = name;
  this.cat = cat;
  this.owner = owner;
  this.description = description;
  this.img = img;

  // uses the set method
  this.price = price;
}

Object.defineProperties(Product.prototype, {
  price: {
    get: function() {
      return 'R$ ' + this._price;
    },
    set: function(price) {
      this._price = price;
    }
  }
});

function User(name, cpf, email, nickname) {
  this.name = name;
  this.email = email;
  this.nickname = nickname;

  // uses the set method
  this.cpf = cpf;
}

Object.defineProperties(User.prototype, {
  cpf: {
    get: function() {
      const c = this._cpf;
      return `
        ${c.substring(0,3)}.${c.substring(3,6)}.${c.substring(6,9)}-${c.substring(9,11)}
      `;
    }, 
    set: function(cpf) {
      if (!validateCpf(cpf)) throw new Error('invalid field cpf');

      this._cpf = cpf;
    }
  }
})

const productList = [
  {
    name: 'Jordan',
    cat: 'Roupas / Tênis',
    price: '2000,00',
    owner: {
      name: 'Jorgin',
      cpf: '91145355722',
      email: 'jorgin@email.com',
      nickname: 'jorgin1112'
    },
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque imperdiet.',
    img: './assets/jordan.jpg',
  },
  {
    name: 'Saco de Arroz 5kg',
    cat: 'Comida',
    price: '40,00',
    owner: {
      name: 'Jorgin',
      cpf: '91145355722',
      email: 'jorgin@email.com',
      nickname: 'jorgin1112'
    },
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque imperdiet.',
    img: './assets/arroz.jpg',
  },
  {
    name: 'Criado mudo',
    cat: 'Móveis',
    price: '600,00',
    owner: {
      name: 'Jorgin',
      cpf: '91145355722',
      email: 'jorgin@email.com',
      nickname: 'jorgin1112'
    },
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque imperdiet.',
    img: './assets/criadomudo.jpg',
  },
  {
    name: 'RTX 3070',
    cat: 'Eletrônicos / GPUs',
    price: '5670,00',
    owner: {
      name: 'Jorgin',
      cpf: '91145355722',
      email: 'jorgin@email.com',
      nickname: 'jorgin1112'
    },
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque imperdiet.',
    img: './assets/rtx.jpg',
  },
];

const productListObjs = toProduct(productList);

const productListCards = productListObjs.map((p) => {
  const hotChance = Math.floor(Math.random() * 5);
  const likes = Math.floor(Math.random() * 10);
  const dislikes = Math.floor(Math.random() * 10);
  console.log(hotChance);

  const card = $(`<div class="card" data-dislikes="${dislikes}" data-likes="${likes}">`);
  const img = $(`<img src="${p.img}" class="card-img-top" alt="...">`);
  const body = $('<div class="card-body">');
  const title = $('<h5 class="card-title">');

  let titleName = null;
  if (hotChance === 0)
    titleName = $(`<span class="badge badge-danger">Hot</span> ${p.name}`);
  else
    titleName = `${p.name}`;
  
  const cat = $(`<h6 class="card-subtitle mb-2 text-muted">${p.cat}</h6>`);
  const description = $(`<p class="card-text">${p.description}</p>`);
  const price = $(`<h5 class="mb-4">${p.price}</h5>`);

  const linkAndLikes = $(`<div class="row">`)
  // for now this will be hardcoded
  const link = $(`<a href="./prod_jordan.html" class="ml-4 col-6 btn btn-primary">Ver Produto</a>`);
  const thumbs = $(`
    <div class="col-5">
      <div class="row">
        <p class="col-1">${likes}</p>
        
        <div class="col-1">
          <i class="clickable far fa-thumbs-up" onclick="giveLike(event);"></i>
        </div>

        <div class="col-1">
          <i class="clickable far fa-thumbs-down" onclick="giveDislike(event);"></i>
        </div>

        <p class="col-1">${dislikes}</p>
      </div>
    </div>
  `);

  linkAndLikes.append(link, thumbs);

  title.append(titleName);
  body.append(
    title,
    cat,
    description,
    price,
    linkAndLikes,
  );
  card.append(img, body);

  return card;
});

productListCards.forEach(p => $('.card-columns.home').append(p));


function giveLike(e) {
  const card = $(e.target).closest('.card');
  const likeP = $(e.target).parent().prev();
  const thumbDown = $(e.target).parent().next().children();
  const dislikeP = thumbDown.parent().next();
  const thumb = $(e.target);

  const numberLikes = card.data('likes');
  const numberDislikes = card.data('dislikes');

  if (thumb.hasClass('far')) {
    card.data('likes', numberLikes + 1);
    thumb.toggleClass('far fas');
    likeP.text(numberLikes + 1);

    if (thumbDown.hasClass('fas')) {
      card.data('dislikes', numberDislikes - 1);
      thumbDown.toggleClass('far fas');
      dislikeP.text(numberDislikes - 1);
    }
  }
}

function giveDislike(e) {
  const card = $(e.target).closest('.card');
  const dislikeP = $(e.target).parent().next();
  const thumbUp = $(e.target).parent().prev().children();
  const likeP = thumbUp.parent().prev();
  const thumb = $(e.target);

  const numberLikes = card.data('likes');
  const numberDislikes = card.data('dislikes');

  if (thumb.hasClass('far')) {
    card.data('dislikes', numberDislikes + 1);
    thumb.toggleClass('far fas');
    dislikeP.text(numberDislikes + 1);

    if (thumbUp.hasClass('fas')) {
      card.data('likes', numberLikes - 1);
      thumbUp.toggleClass('far fas');
      likeP.text(numberLikes - 1);
    }
  }
}
