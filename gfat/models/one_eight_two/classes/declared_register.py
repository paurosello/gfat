# coding=utf-8
from one_eight_two import DECLARATION_MODEL


class DeclaredRegister:
    """Declared Register Model on 18/01/2018
        http://www.agenciatributaria.es/static_files/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Ayuda/Disenyos_de_registro/Ayudas/DR_100_a_199/ficheros/DR182_2016.pdf

        Attributes
            exercise:
                Las  cuatro  cifras  del  ejercicio  fiscal  al  que  corresponde la declaración.

            declaring_id:
                Se consignará el N.I.F. del declarante, de acuerdocon lasreglas   previstas   en   el Reglamento
                General   de   lasactuaciones y los procedimientos de gestión e inspeccióntributaria  y de  desarrollo
                de  las  normas  comunes  delosprocedimientos  de  aplicación  de  los  tributos, aprobadopor el Real
                Decreto 1065/2007, de 27 de julio (BOEdel 5de septiembre)

            declared_id:
                Si es una persona física se consignará el N.I.F. deldeclarado de acuerdo con las reglas
                previstas en elReglamento General de las actuaciones y losprocedimientos de gestión e inspección
                tributaria ydedesarrollo de las normas comunes de los procedimientosde aplicación de los tributos,
                aprobado por el RealDecreto 1065/2007, de 27 de julio (BOE de 5 deseptiembre).Si el declarado es una
                persona jurídica o una entidad enrégimen de atribución de rentas (comunidad de bienes,sociedad civil,
                herencia yacente, etc.), se consignará elnúmero de identificación fiscal correspondiente a la misma.Para
                la identificación de los menores de 14 años ensusrelaciones de naturaleza o con trascendencia
                tributariahabrán de figurar tanto los datos de la persona menor de14 años, incluido su número de
                identificación fiscal, comoel número de identificación fiscal de su representantelegal.Este campo deberá
                estar ajustado a la derecha, siendo laúltima posición el carácter de control y rellenandocon ceroslas
                posiciones a la izquierda.

            legal_representative_id:
                Si el declarado es menor de 14 años, se consignaráeneste campo el número de identificación fiscal de
                surepresentante legal (padre, madre o tutor).Si el declarado es menor de 14 años se consignará en
                estecampo el número de identificación fiscal de surepresentante legal (padre, madre o tutor), de acuerdo
                conlas reglas previstas en el Reglamento General de lasactuaciones y los procedimientos de gestión e
                inspeccióntributaria y de desarrollo de las normas comunes delosprocedimientos de aplicación de los
                tributos, aprobadopor el Real Decreto 1065/2007, de 27 de julio (BOEde 5de septiembre).Asimismo,
                tratándose de contribuyentes por el Impuestosobre la Renta de no Residentes que no dispongan deN.I.F.,
                deberá consignar en este campo, en su caso,elnúmero de identificación fiscal de quien ostente
                larepresentación del mismo, de acuerdo con lo establecidoen el artículo 10 del Texto Refundido de la
                LeydelImpuesto sobre la Renta de no Residentes.Este campo deberá estar ajustado a la derecha,
                siendo laúltima posición el carácter de control y rellenandocon ceroslas posiciones a la izquierda.En
                cualquier otro caso el contenido de este campo serellenará a espacios

            declared_name:
                Para  personas  físicas  se  consignará  el  primer  apellido,  unespacio,  el  segundo
                apellido,  un  espacio  y  el  nombrecompleto, necesariamente en este mismo orden.Si el declarado es
                menor de edad, se consignarán enestecampo los apellidos y nombre del menor de edad.Tratándose  de
                personas  jurídicas  y  entidades  en  régimende  atribución  de  rentas,  se  consignará    la  razón
                social  odenominación completa de la entidad, sin anagramas.

            province_code:
                Se consignarán los dos dígitos numéricos quecorrespondan a la provincia o, en su caso,
                ciudadautónoma del domicilio del declarado, según la relación queconsta a continuación. Cuando el
                declarado sea un no residente sin establecimiento permanente en territorioespañol se hará constar como
                código de provincia el 99.

            key:
                Deberá rellenarse por las entidades acogidas al régimende deducciones recogidas en el Título III de
                la Ley49/2002, de 23 de diciembre, según el siguiente detalle:
                    A. Donativos no incluidos en las actividades o programasprioritarios de mecenazgo establecidos por
                        la Ley dePresupuestos Generales del Estado.
                    B. Donativos incluidos en las actividades o programas prioritarios de mecenazgo establecidos por la
                        Ley de Presupuestos Generales del Estado.

                Tratándose de aportaciones o disposiciones relativas a patrimonios protegidos, deberá consignarse alguna
                de las siguientes claves:
                    C. Aportación al patrimonio de discapacitados.
                    D. Disposición del patrimonio de discapacitados.
                    E. Gasto de dinero y consumo de bienes fungibles aportados al patrimonio protegido en el año natural
                        al quese refiere la declaración informativa o en los cuatro anteriores para atender las
                        necesidades vitales delbeneficiario y que no deban considerarse como disposición de bienes o
                        derechos a efectos de lodispuesto en el artículo 54.5 de la Ley 35/2006, de 28 denoviembre, del
                        Impuesto sobre la Renta de las PersonasFísicas.Los Partidos Políticos,

                Federaciones, Coaliciones o Agrupaciones de Electores consignarán las siguientesclaves:
                    F: cuotas de afiliación y aportaciones previstas en elartículo 2.Dos.a) de la Ley Orgánica 8/2007,
                        de 4 de julio,sobre financiación de los partidos políticos.
                    G: resto de donaciones y aportaciones percibidas.
    """

    #Contants
    register_type = "2"
    declaration_model = DECLARATION_MODEL

    #Variables
    exercise = None
    declaring_id = None
    declared_id = None
    declared_name = None
    province_code = None
    key = None
    #TODO: document attributes below
    percentage_deduction = None
    amount = None
    in_kind_donation = None
    territory_deduction = None
    territory_deduction_percentage = None
    declared_type = None
    revocation = None
    revocation_date = None
    goods_type = None
    goods_identification = None
    donation_recurrence = None


    def __init__(self):
        return
