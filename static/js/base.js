const fixFooter = () => {
  if ($('body').height() > $(window).height()) {
    $('footer').removeClass('footer-fixed');
    console.log('alo');
  } else {
    $('footer').addClass('footer-fixed');
  }
};

$(() => {
  fixFooter();
  $(window).on('resize', () => fixFooter());

  $('#fast-creation-form').on('shown.bs.collapse', () => {
    fixFooter();
  });

  $('#fast-creation-form').on('hidden.bs.collapse', () => {
    fixFooter();
  });
});