package com.addada123.opcua.demoserver.node;

import org.eclipse.milo.opcua.stack.core.types.builtin.unsigned.UShort;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder(toBuilder = true)
@AllArgsConstructor
@NoArgsConstructor
public class NodeEntity {
    private Integer index;
    private String identifier;
    private String value;
    private String type;
    private Integer clientHandle;
    public UShort getIndex() {
        return null;
    }
}
