defaultTypeSystem = """<?xml version="1.0" encoding="UTF-8"?>
<typeSystemDescription xmlns="http://uima.apache.org/resourceSpecifier">
        
    <types>
                
        <typeDescription>
                        
            <name>uima.tcas.DocumentAnnotation</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>language</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.coref.type.CoreferenceChain</name>
                        
            <description/>
                        
            <supertypeName>uima.cas.AnnotationBase</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>first</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>de.tudarmstadt.ukp.dkpro.core.api.coref.type.CoreferenceLink</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.coref.type.CoreferenceLink</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>next</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>de.tudarmstadt.ukp.dkpro.core.api.coref.type.CoreferenceLink</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>referenceType</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>referenceRelation</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.morph.Morpheme</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>morphTag</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.morph.MorphologicalFeatures</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>gender</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>number</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>case</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>degree</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>verbForm</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>tense</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>mood</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>voice</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>definiteness</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>person</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>aspect</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>animacy</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>negative</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>numType</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>possessive</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>pronType</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>reflex</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>transitivity</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>PosValue</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>coarseValue</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_ADJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_ADP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_ADV</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_AUX</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_CONJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_DET</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_INTJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_NOUN</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_NUM</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_PART</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_PRON</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_PROPN</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_PUNCT</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_SCONJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_SYM</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_VERB</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_X</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.tweet.POS_AT</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_X</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.tweet.POS_DM</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_X</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.tweet.POS_EMO</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_X</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.tweet.POS_HASH</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_X</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.tweet.POS_INT</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_X</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.tweet.POS_NNV</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_NOUN</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.tweet.POS_NPV</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_NOUN</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.tweet.POS_URL</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS_X</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.metadata.type.DocumentMetaData</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.DocumentAnnotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>documentTitle</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>documentId</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>documentUri</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>collectionId</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>documentBaseUri</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>isLastSegment</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.Boolean</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.metadata.type.MetaDataStringField</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>key</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.metadata.type.TagDescription</name>
                        
            <description/>
                        
            <supertypeName>uima.cas.TOP</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>name</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.metadata.type.TagsetDescription</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>layer</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>name</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>tags</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.FSArray</rangeTypeName>
                                        
                    <elementType>de.tudarmstadt.ukp.dkpro.core.api.metadata.type.TagDescription</elementType>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>componentName</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>modelLocation</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>modelVariant</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>modelLanguage</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>modelVersion</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>input</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.Boolean</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>identifier</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Nationality</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Norp</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Ordinal</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.OrgDesc</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Organization</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.PerDesc</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Percent</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Person</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Plant</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Product</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.ProductDesc</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Quantity</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Substance</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Time</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.WorkOfArt</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Compound</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>splits</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.FSArray</rangeTypeName>
                                        
                    <elementType>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Split</elementType>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Div</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>divType</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>id</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Document</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Div</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Heading</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Div</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Lemma</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.LexicalPhrase</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>text</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.NGram</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>text</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Paragraph</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Div</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Sentence</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>id</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Split</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>splits</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.FSArray</rangeTypeName>
                                        
                    <elementType>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Split</elementType>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Stem</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.StopWord</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.SurfaceForm</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Token</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>parent</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.tcas.Annotation</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>lemma</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Lemma</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>stem</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Stem</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>pos</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>morph</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.morph.MorphologicalFeatures</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>id</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>form</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.TokenForm</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>syntacticFunction</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>order</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.Integer</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.TokenForm</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.semantics.type.SemArg</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.semantics.type.SemArgLink</name>
                        
            <description/>
                        
            <supertypeName>uima.cas.TOP</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>role</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>target</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>de.tudarmstadt.ukp.dkpro.core.api.semantics.type.SemArg</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.semantics.type.SemPred</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>arguments</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.FSArray</rangeTypeName>
                                        
                    <elementType>de.tudarmstadt.ukp.dkpro.core.api.semantics.type.SemArgLink</elementType>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>category</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.semantics.type.SemanticArgument</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>role</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.semantics.type.SemanticField</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.semantics.type.SemanticPredicate</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>category</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>arguments</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.FSArray</rangeTypeName>
                                        
                    <elementType>de.tudarmstadt.ukp.dkpro.core.api.semantics.type.SemanticArgument</elementType>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.semantics.type.WordSense</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.structure.type.Field</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>name</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.PennTree</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>PennTree</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>TransformationNames</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>chunkValue</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.INTJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.LST</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.NC</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.O</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.PC</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.PRT</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.VC</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>constituentType</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>parent</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.tcas.Annotation</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>children</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.FSArray</rangeTypeName>
                                        
                    <elementType>uima.tcas.Annotation</elementType>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>syntacticFunction</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.FRAG</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.INTJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.LST</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.NAC</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.NP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.NX</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.PARN</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.PP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.PRP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.PRT</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.QP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.ROOT</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.RRC</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.S</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.SBAR</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.SBARQ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.SINV</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.SQ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.UCP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.VP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.WHADJP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.WHADVP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.WHNP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.WHPP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.X</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>Governor</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Token</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>Dependent</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Token</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>DependencyType</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>flavor</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.EXPL</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.INFMOD</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.IOBJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.MARK</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.MEASURE</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.MWE</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.NEG</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.NN</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.NPADVMOD</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.NSUBJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.NSUBJPASS</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.NUM</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.NUMBER</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PARATAXIS</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PARTMOD</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PCOMP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.POBJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.POSS</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.POSSESSIVE</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PRECONJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PRED</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PREDET</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PREP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PREPC</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PRT</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PUNCT</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.PURPCL</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.QUANTMOD</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.RCMOD</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.REF</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.REL</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.ROOT</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.TMOD</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.XCOMP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.XSUBJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.transform.type.SofaChangeAnnotation</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>operation</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>reason</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>org.dkpro.core.api.xml.type.XmlAttribute</name>
                        
            <description/>
                        
            <supertypeName>uima.cas.TOP</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>uri</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>localName</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>value</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>qName</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>valueType</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>org.dkpro.core.api.xml.type.XmlDocument</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>root</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>org.dkpro.core.api.xml.type.XmlElement</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>org.dkpro.core.api.xml.type.XmlNode</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>parent</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>org.dkpro.core.api.xml.type.XmlElement</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>org.dkpro.core.api.xml.type.XmlTextNode</name>
                        
            <description/>
                        
            <supertypeName>org.dkpro.core.api.xml.type.XmlNode</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>text</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>captured</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.Boolean</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Animal</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Cardinal</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.ContactInfo</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Date</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Disease</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Event</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Fac</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.FacDesc</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Game</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Gpe</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.GpeDesc</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Language</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Law</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Location</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.ner.type.Money</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.ner.type.NamedEntity</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.CompoundPart</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Split</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.LinkingMorpheme</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Split</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.ADJC</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.ADVC</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.CONCJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.chunk.Chunk</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.ADJP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.ADVP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.CONJP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.constituent.Constituent</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.ABBREV</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.ACOMP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.ADVCL</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.ADVMOD</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.AGENT</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.AMOD</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.APPOS</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.ATTR</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.AUX0</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.AUXPASS</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.CC</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.CCOMP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.COMPLM</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.CONJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.CONJP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.CONJ_YET</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.COP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.CSUBJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.CSUBJPASS</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.DEP</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.DET</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.DOBJ</name>
                        
            <description/>
                        
            <supertypeName>de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency</supertypeName>
                    
        </typeDescription>
                
        <typeDescription>
                        
            <name>org.dkpro.core.api.xml.type.XmlElement</name>
                        
            <description/>
                        
            <supertypeName>org.dkpro.core.api.xml.type.XmlNode</supertypeName>
                        
            <features>
                                
                <featureDescription>
                                        
                    <name>uri</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>localName</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>attributes</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.FSArray</rangeTypeName>
                                        
                    <elementType>org.dkpro.core.api.xml.type.XmlAttribute</elementType>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>children</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.FSArray</rangeTypeName>
                                        
                    <elementType>org.dkpro.core.api.xml.type.XmlNode</elementType>
                                    
                </featureDescription>
                                
                <featureDescription>
                                        
                    <name>qName</name>
                                        
                    <description/>
                                        
                    <rangeTypeName>uima.cas.String</rangeTypeName>
                                    
                </featureDescription>
                            
            </features>
                    
        </typeDescription>

        <typeDescription>
                        
            <name>webanno.custom.SentenceLayer</name>
                        
            <description/>
                        
            <supertypeName>uima.tcas.Annotation</supertypeName>

        </typeDescription>
      <typeDescription>
    </types>
    
</typeSystemDescription>
"""