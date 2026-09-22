const WHATSAPP_NUMBER = '554491075497';
const WHATSAPP_MESSAGE =
  'Olá, Tuane. Entrei em contato pelo site e gostaria de obter mais informações sobre o acompanhamento nutricional.';

export const whatsappUrl = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(WHATSAPP_MESSAGE)}`;
