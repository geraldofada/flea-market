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

  $('#fast-creation-collapse').on('shown.bs.collapse', () => {
    fixFooter();
  });

  $('#fast-creation-collapse').on('hidden.bs.collapse', () => {
    fixFooter();
  });
});