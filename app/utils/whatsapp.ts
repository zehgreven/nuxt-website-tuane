const WHATSAPP_NUMBER = '554491075497';
const WHATSAPP_MESSAGE =
  'Olá, Tuane. Entrei em contato pelo site e gostaria de obter mais informações sobre o acompanhamento nutricional.';

export function buildWhatsappUrl(message: string) {
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
}

export const whatsappUrl = buildWhatsappUrl(WHATSAPP_MESSAGE);
